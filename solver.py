
#import time
from typing import List
from Models.container_item import ContainerItem
from Models.package_item import PackageItem
from Models.point3d import Point3d
from Models.positioned_package import PositionedPackage
from Models.solved_container import SolvedContainer
from Models.solver_input import SolverInput
from Models.solver_output import SolverOutput

from Algorithms.Enzoruiz_py3dbp import Packer as py3dbpPacker
from Algorithms.Enzoruiz_py3dbp import Bin as py3dbpBin
from Algorithms.Enzoruiz_py3dbp import Item as py3dbpItem

#import Algorithms.Custom1 as cust1
#import Algorithms.Custom2 as cust1
import Algorithms.Custom3 as cust1

import Models.Templates.warehouse_templates as wh

def find_solution(input: SolverInput, algorithm: str="") -> SolverOutput:
  #start_time = time.time()
  # hack: return warehouse example in certain cases no matter the actual input.
  is_warehouse, warehouse = wh.is_warehouse(container_item=input.container_items[0], package_items=input.package_items)
  if is_warehouse:
    return warehouse.to_solver_output()

  # truncate input if too many items
  max_limit = 100
  skipped_items: List[PackageItem] = []

  if len(input.package_items) > max_limit:
    skipped_items = input.package_items[max_limit:]
    input.package_items = input.package_items[:max_limit]

  if algorithm == "custom1":
    res = solve_custom1(input=input)
  elif algorithm == "enzoruiz":
    res = solve_enzoruiz_py3dbp(input=input)
  else:
    res = solve_custom1(input=input)

  if len(skipped_items) > 0:
    res.not_fitted_package_items += skipped_items
    res.num_items_unfitted = len(res.not_fitted_package_items)

  #end_time = time.time()
  #print(f"find_solution time={end_time - start_time}")

  return res

def solve_enzoruiz_py3dbp(input: SolverInput) -> SolverOutput:
  packer = py3dbpPacker()
  for cont in input.container_items:
    packer.add_bin(py3dbpBin(
          name=cont.name,
          width=cont.width,
          height=cont.height,
          depth=cont.length,
          max_weight=10000000)
          )

  for pack in input.package_items:
    packer.add_item(py3dbpItem(
          name=pack.name,
          width=pack.width,
          height=pack.height,
          depth=pack.length,
          weight=0)
          )

  packer.pack(bigger_first=True)

  res = SolverOutput()
  if len(packer.bins) < 1:
    return res

  bin1 = packer.bins[0]

  cont1 = SolvedContainer(
    container_item=ContainerItem(name=bin1.name, height=bin1.height, width=bin1.width, length=bin1.depth),
    solution = [PositionedPackage.create_from_back_bottom_left_corner(
                                      package_item=PackageItem(
                                                    name=i.name,
                                                    height=i.height,
                                                    width=i.width,
                                                    length=i.depth
                                                    ),
                                      back_bottom_left_corner=Point3d(
                                              x=i.position[0],
                                              y=i.position[1],
                                              z=i.position[2])
                                              ) for i in bin1.items ]
    )

  cont1.set_calculated_props()

  res.solved_containers = [cont1]

  res.not_fitted_package_items = [PackageItem(
                                              name = i.name,
                                              height = i.height,
                                              width = i.width,
                                              length = i.depth
                                              ) for i in bin1.unfitted_items]

  res.num_items_total = len(input.package_items)
  res.num_items_fitted = sum(len(c.solution) for c in res.solved_containers)
  res.num_items_unfitted = len(res.not_fitted_package_items)
  res.num_items_fitted_ratio = 0 if res.num_items_total == 0 else res.num_items_fitted / res.num_items_total
  res.total_fill_ratio = 0 if len(res.solved_containers) == 0 else sum(c.get_fill_ratio() for c in res.solved_containers) / len(res.solved_containers)

  return res

def solve_custom1(input: SolverInput) -> SolverOutput:
  cont = input.container_items[0]
  bin1 = cust1.Bin(
          name=cont.name,
          width=cont.width,
          height=cont.height,
          depth=cont.length,
          max_weight=10000000)

  items = [cust1.Item(
                name=pack.name,
                width=pack.width,
                height=pack.height,
                depth=pack.length,
                weight=0)
              for pack in input.package_items]


  packer = cust1.Packer(bin=bin1, items=items)

  num_items = len(input.package_items)
  num_iterations = 250
  if num_items > 80:
    num_iterations = 20
  elif num_items > 60:
    num_iterations = 30
  elif num_items > 40:
    num_iterations = 60
  elif num_items > 20:
    num_iterations = 150

  iterative_packer = cust1.IterativePacker(
      num_iterations=num_iterations,
      num_restarts=2,
      pack_unfitted_again=True
    )

  packer = iterative_packer.pack(packer=packer)

  res = SolverOutput()

  bin1 = packer.get_bin()

  cont1 = SolvedContainer(
    container_item=ContainerItem(name=bin1.name, height=bin1.height, width=bin1.width, length=bin1.depth),
    solution = [PositionedPackage.create_from_back_bottom_left_corner(
                                      package_item=PackageItem(
                                                    name=i.name,
                                                    height=i.height,
                                                    width=i.width,
                                                    length=i.depth
                                                    ),
                                      back_bottom_left_corner=Point3d(
                                              x=i.position[0],
                                              y=i.position[1],
                                              z=i.position[2])
                                              ) for i in bin1.items ]
    )

  cont1.set_calculated_props()

  res.solved_containers = [cont1]

  res.not_fitted_package_items = [PackageItem(
                                              name = i.name,
                                              height = i.height,
                                              width = i.width,
                                              length = i.depth
                                              ) for i in packer.unfitted_items]

  res.num_items_total = len(input.package_items)
  res.num_items_fitted = sum(len(c.solution) for c in res.solved_containers)
  res.num_items_unfitted = len(res.not_fitted_package_items)
  res.num_items_fitted_ratio = 0 if res.num_items_total == 0 else round(res.num_items_fitted / res.num_items_total, 4)
  res.total_fill_ratio = 0 if len(res.solved_containers) == 0 else round(sum(c.get_fill_ratio() for c in res.solved_containers) / len(res.solved_containers), 4)
  res.is_success = True if res.total_fill_ratio > 0.99 else False

  if res.num_items_total != res.num_items_fitted + res.num_items_unfitted:
    duplicate_names = list(set([x.name for x in bin1.items if bin1.items.count(x.name) > 1]))
    num_duplicates = len(duplicate_names)
    if num_duplicates > 0:
      print("-" * 50)
      print(f"num_duplicates={num_duplicates}")
      print(f"duplicate_package_items={duplicate_names}")

    not_fitted_json = [i.json() for i in res.not_fitted_package_items]
    print("-" * 50)
    print(f"not_fitted_package_items={not_fitted_json}")
    print("-" * 50)

  return res
