
import json
import random as rnd
rnd.seed(10101)

from os import name
import Algorithms.bin_slicer as bs
from Models.container_item import ContainerItem
from Models.positioned_package import PositionedPackage
from Models.package_item import PackageItem
from Models.point3d import Point3d
from Models.solved_container import SolvedContainer
from Models.solver_input import SolverInput
from Models.solver_output import SolverOutput
from Models.example_template import ExampleTemplate

def example_by_id(id: int):
  if id == 1:
    return example1()
  elif id == 2:
    return example2()
  elif id == 3:
    return example3()
  elif id == 4:
    return example4()
  elif id == 5:
    return example5()
  else:
    return example1()

def random_example():
    return next_random_example()

def example1() -> ExampleTemplate:

  solved_container = SolvedContainer(
      container_item = ContainerItem(name="container1", width=200, height=300, length=600)
    )

  pack1 = PackageItem(name="pack1", width=100, height=300, length=500)
  pos1 = pack1.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=0, z=0))

  pack2 = PackageItem(name="pack2", width=100, height=200, length=500)
  pos2 = pack2.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=100, y=0, z=0))

  pack3 = PackageItem(name="pack3", width=100, height=100, length=400)
  pos3 = pack3.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=0))

  pack4 = PackageItem(name="pack4", width=200, height=100, length=100)
  pos4 = pack4.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=200))

  pack5 = PackageItem(name="pack5", width=200, height=100, length=100)
  pos5 = pack5.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=400))

  pack6 = PackageItem(name="pack6", width=100, height=100, length=150)
  pos6 = pack6.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=0))

  pack7 = PackageItem(name="pack7", width=100, height=100, length=100)
  pos7 = pack7.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=300))

  pack8 = PackageItem(name="pack8", width=100, height=100, length=50)
  pos8 = pack8.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=100, z=0))

  solved_container.solution = [
        PositionedPackage(package_item=pack1, position=pos1),
        PositionedPackage(package_item=pack2, position=pos2),
        PositionedPackage(package_item=pack3, position=pos3),
        PositionedPackage(package_item=pack4, position=pos4),
        PositionedPackage(package_item=pack5, position=pos5),
        PositionedPackage(package_item=pack6, position=pos6),
        PositionedPackage(package_item=pack7, position=pos7),
        PositionedPackage(package_item=pack8, position=pos8),
      ]

  solved_container.set_calculated_props()

  solver_output = SolverOutput()
  solver_output.solved_containers = [solved_container]

  solver_input = SolverInput()
  solver_input.container_items = [solved_container.container_item]
  solver_input.package_items = [i.package_item for i in solved_container.solution]

  res = ExampleTemplate(name="example1", solver_input=solver_input, solver_output=solver_output)
  return res

def example1x() -> ExampleTemplate:

  solved_container = SolvedContainer(
      container_item = ContainerItem(name="container1", height=200, width=300, length=600)
    )

  pack1 = PackageItem(name="pack1", height=50, width=100, length=600)
  pos1 = pack1.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=0, z=0))

  pack2 = PackageItem(name="pack2", height=50, width=100, length=600)
  pos2 = pack2.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=100, y=0, z=0))

  pack3 = PackageItem(name="pack3", height=100, width=100, length=200)
  pos3 = pack3.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=0))

  pack4 = PackageItem(name="pack4", height=100, width=100, length=200)
  pos4 = pack4.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=200))

  pack5 = PackageItem(name="pack5", height=100, width=100, length=200)
  pos5 = pack5.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=400))

  pack6 = PackageItem(name="pack6", height=150, width=150, length=300)
  pos6 = pack6.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=0))

  pack7 = PackageItem(name="pack7", height=150, width=150, length=300)
  pos7 = pack7.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=300))

  pack7a = PackageItem(name="pack7a", height=150, width=50, length=600)
  pos7a = pack7a.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=150, y=50, z=0))

  pack8 = PackageItem(name="pack8", height=50, width=50, length=400)
  pos8 = pack8.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=100, z=0))

  pack9 = PackageItem(name="pack9", height=50, width=50, length=400)
  pos9 = pack9.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=250, y=100, z=0))

  pack10 = PackageItem(name="pack10", height=50, width=100, length=300)
  pos10 = pack10.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=150, z=0))

  pack11 = PackageItem(name="pack11", height=50, width=100, length=100)
  pos11 = pack11.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=150, z=300))

  pack12 = PackageItem(name="pack12", height=100, width=100, length=200)
  pos12 = pack12.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=200, z=400))

  solved_container.solution = [
        PositionedPackage(package_item=pack1, position=pos1),
        PositionedPackage(package_item=pack2, position=pos2),
        PositionedPackage(package_item=pack3, position=pos3),
        PositionedPackage(package_item=pack4, position=pos4),
        PositionedPackage(package_item=pack5, position=pos5),
        PositionedPackage(package_item=pack6, position=pos6),
        PositionedPackage(package_item=pack7, position=pos7),
        PositionedPackage(package_item=pack7a, position=pos7a),
        PositionedPackage(package_item=pack8, position=pos8),
        PositionedPackage(package_item=pack9, position=pos9),
        PositionedPackage(package_item=pack10, position=pos10),
        PositionedPackage(package_item=pack11, position=pos11),
        PositionedPackage(package_item=pack12, position=pos12),
      ]

  solved_container.set_calculated_props()

  solver_output = SolverOutput()
  solver_output.solved_containers = [solved_container]

  solver_input = SolverInput()
  solver_input.container_items = [solved_container.container_item]
  solver_input.package_items = [i.package_item for i in solved_container.solution]

  res = ExampleTemplate(name="example1", solver_input=solver_input, solver_output=solver_output)
  return res

def example2() -> ExampleTemplate:

  solved_container = SolvedContainer(
      container_item = ContainerItem(name="container1", width=300, height=200, length=600)
    )

  pack1 = PackageItem(name="pack1", width=300, height=100, length=500)
  pos1 = pack1.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=0, z=0))

  pack2 = PackageItem(name="pack2", width=200, height=100, length=500)
  pos2 = pack2.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=100, y=0, z=0))

  pack3 = PackageItem(name="pack3", width=100, height=100, length=400)
  pos3 = pack3.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=0))

  pack4 = PackageItem(name="pack4", width=100, height=200, length=100)
  pos4 = pack4.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=200))

  pack5 = PackageItem(name="pack5", width=100, height=200, length=100)
  pos5 = pack5.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=0, z=400))

  pack6 = PackageItem(name="pack6", width=100, height=100, length=150)
  pos6 = pack6.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=0))

  pack7 = PackageItem(name="pack7", width=100, height=100, length=100)
  pos7 = pack7.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0, y=50, z=300))

  pack8 = PackageItem(name="pack8", width=100, height=100, length=50)
  pos8 = pack8.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=200, y=100, z=0))

  solved_container.solution = [
        PositionedPackage(package_item=pack1, position=pos1),
        PositionedPackage(package_item=pack2, position=pos2),
        PositionedPackage(package_item=pack3, position=pos3),
        PositionedPackage(package_item=pack4, position=pos4),
        PositionedPackage(package_item=pack5, position=pos5),
        PositionedPackage(package_item=pack6, position=pos6),
        PositionedPackage(package_item=pack7, position=pos7),
        PositionedPackage(package_item=pack8, position=pos8),
      ]

  solved_container.set_calculated_props()

  solver_output = SolverOutput()
  solver_output.solved_containers = [solved_container]

  solver_input = SolverInput()
  solver_input.container_items = [solved_container.container_item]
  solver_input.package_items = [i.package_item for i in solved_container.solution]

  res = ExampleTemplate(name="example2", solver_input=solver_input, solver_output=solver_output)
  return res

def example2x() -> ExampleTemplate:
  height = 200
  width = 300
  length = 600

  solved_container = SolvedContainer()

  # Create container with given dimensions.
  solved_container.container_item  = ContainerItem(name="container1", height=height, width=width, length=length)

  # Create initial package with the same dimensions as container.
  package_item = PackageItem(name="pack1", height=height, width=width, length=length)
  pos = package_item.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0,y=0,z=0))
  positioned_package = PositionedPackage(package_item=package_item, position=pos)

  intersection_value = 100

  slice_result = bs.slice_intersect_z(bin=positioned_package, intersect_z_at=intersection_value)

  solved_container.solution = slice_result
  solved_container.set_calculated_props()

  solver_output = SolverOutput()
  solver_output.solved_containers = [solved_container]

  solver_input = SolverInput()
  solver_input.container_items = [solved_container.container_item]
  solver_input.package_items = [i.package_item for i in solved_container.solution]

  res = ExampleTemplate(name="example2", solver_input=solver_input, solver_output=solver_output)
  return res

def example3() -> ExampleTemplate:
  # solver_perfect_example_custom1_15_items.txt
  json_string = u'{"name":"example3","solver_input":{"container_items":[{"name":"container1","height":200,"width":300,"length":600}],"package_items":[{"name":"slice_front_bottom_right_left_top_left","height":50.0,"width":37.5,"length":300.0},{"name":"slice_front_bottom_left","height":100.0,"width":150.0,"length":300.0},{"name":"slice_front_top_left_bottom_top","height":25.0,"width":150.0,"length":300.0},{"name":"slice_front_bottom_right_right_front_top","height":50.0,"width":75.0,"length":150.0},{"name":"slice_front_bottom_right_left_bottom_back","height":50.0,"width":75.0,"length":150.0},{"name":"slice_front_bottom_right_right_back","height":100.0,"width":75.0,"length":150.0},{"name":"slice_front_bottom_right_right_front_bottom","height":50.0,"width":75.0,"length":150.0},{"name":"slice_back_right","height":200,"width":150.0,"length":300.0},{"name":"slice_front_top_right","height":100.0,"width":150.0,"length":300.0},{"name":"slice_front_top_left_bottom_bottom","height":25.0,"width":150.0,"length":300.0},{"name":"slice_front_bottom_right_left_bottom_front","height":50.0,"width":75.0,"length":150.0},{"name":"slice_front_top_left_top","height":50.0,"width":150.0,"length":300.0},{"name":"slice_front_bottom_right_left_top_right","height":50.0,"width":37.5,"length":300.0},{"name":"slice_back_left_top","height":100.0,"width":150.0,"length":300.0},{"name":"slice_back_left_bottom","height":100.0,"width":150.0,"length":300.0}]},"solver_output":{"is_success":true,"num_items_total":0,"num_items_fitted":0,"num_items_unfitted":0,"num_items_fitted_ratio":0,"total_fill_ratio":0,"solved_containers":[{"fill_ratio":1.0,"number_of_items_inside":15,"solution":[{"package_item":{"name":"slice_back_left_bottom","height":100.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":100.0,"z":300.0},"front_bottom_left_corner":{"x":0,"y":0,"z":300.0},"front_top_right_corner":{"x":150.0,"y":100.0,"z":300.0},"front_bottom_right_corner":{"x":150.0,"y":0,"z":300.0},"back_top_left_corner":{"x":0,"y":100.0,"z":0},"back_bottom_left_corner":{"x":0,"y":0,"z":0},"back_top_right_corner":{"x":150.0,"y":100.0,"z":0},"back_bottom_right_corner":{"x":150.0,"y":0,"z":0}}},{"package_item":{"name":"slice_back_left_top","height":100.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":300.0},"front_bottom_left_corner":{"x":0,"y":100.0,"z":300.0},"front_top_right_corner":{"x":150.0,"y":200,"z":300.0},"front_bottom_right_corner":{"x":150.0,"y":100.0,"z":300.0},"back_top_left_corner":{"x":0,"y":200,"z":0},"back_bottom_left_corner":{"x":0,"y":100.0,"z":0},"back_top_right_corner":{"x":150.0,"y":200,"z":0},"back_bottom_right_corner":{"x":150.0,"y":100.0,"z":0}}},{"package_item":{"name":"slice_back_right","height":200,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":150.0,"y":200,"z":300.0},"front_bottom_left_corner":{"x":150.0,"y":0,"z":300.0},"front_top_right_corner":{"x":300,"y":200,"z":300.0},"front_bottom_right_corner":{"x":300,"y":0,"z":300.0},"back_top_left_corner":{"x":150.0,"y":200,"z":0},"back_bottom_left_corner":{"x":150.0,"y":0,"z":0},"back_top_right_corner":{"x":300,"y":200,"z":0},"back_bottom_right_corner":{"x":300,"y":0,"z":0}}},{"package_item":{"name":"slice_front_bottom_left","height":100.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":100.0,"z":600},"front_bottom_left_corner":{"x":0,"y":0,"z":600},"front_top_right_corner":{"x":150.0,"y":100.0,"z":600},"front_bottom_right_corner":{"x":150.0,"y":0,"z":600},"back_top_left_corner":{"x":0,"y":100.0,"z":300.0},"back_bottom_left_corner":{"x":0,"y":0,"z":300.0},"back_top_right_corner":{"x":150.0,"y":100.0,"z":300.0},"back_bottom_right_corner":{"x":150.0,"y":0,"z":300.0}}},{"package_item":{"name":"slice_front_bottom_right_left_bottom_back","height":50.0,"width":75.0,"length":150.0},"position":{"front_top_left_corner":{"x":150.0,"y":50.0,"z":450.0},"front_bottom_left_corner":{"x":150.0,"y":0,"z":450.0},"front_top_right_corner":{"x":225.0,"y":50.0,"z":450.0},"front_bottom_right_corner":{"x":225.0,"y":0,"z":450.0},"back_top_left_corner":{"x":150.0,"y":50.0,"z":300.0},"back_bottom_left_corner":{"x":150.0,"y":0,"z":300.0},"back_top_right_corner":{"x":225.0,"y":50.0,"z":300.0},"back_bottom_right_corner":{"x":225.0,"y":0,"z":300.0}}},{"package_item":{"name":"slice_front_bottom_right_left_bottom_front","height":50.0,"width":75.0,"length":150.0},"position":{"front_top_left_corner":{"x":150.0,"y":50.0,"z":600},"front_bottom_left_corner":{"x":150.0,"y":0,"z":600},"front_top_right_corner":{"x":225.0,"y":50.0,"z":600},"front_bottom_right_corner":{"x":225.0,"y":0,"z":600},"back_top_left_corner":{"x":150.0,"y":50.0,"z":450.0},"back_bottom_left_corner":{"x":150.0,"y":0,"z":450.0},"back_top_right_corner":{"x":225.0,"y":50.0,"z":450.0},"back_bottom_right_corner":{"x":225.0,"y":0,"z":450.0}}},{"package_item":{"name":"slice_front_bottom_right_left_top_left","height":50.0,"width":37.5,"length":300.0},"position":{"front_top_left_corner":{"x":150.0,"y":100.0,"z":600},"front_bottom_left_corner":{"x":150.0,"y":50.0,"z":600},"front_top_right_corner":{"x":187.5,"y":100.0,"z":600},"front_bottom_right_corner":{"x":187.5,"y":50.0,"z":600},"back_top_left_corner":{"x":150.0,"y":100.0,"z":300.0},"back_bottom_left_corner":{"x":150.0,"y":50.0,"z":300.0},"back_top_right_corner":{"x":187.5,"y":100.0,"z":300.0},"back_bottom_right_corner":{"x":187.5,"y":50.0,"z":300.0}}},{"package_item":{"name":"slice_front_bottom_right_left_top_right","height":50.0,"width":37.5,"length":300.0},"position":{"front_top_left_corner":{"x":187.5,"y":100.0,"z":600},"front_bottom_left_corner":{"x":187.5,"y":50.0,"z":600},"front_top_right_corner":{"x":225.0,"y":100.0,"z":600},"front_bottom_right_corner":{"x":225.0,"y":50.0,"z":600},"back_top_left_corner":{"x":187.5,"y":100.0,"z":300.0},"back_bottom_left_corner":{"x":187.5,"y":50.0,"z":300.0},"back_top_right_corner":{"x":225.0,"y":100.0,"z":300.0},"back_bottom_right_corner":{"x":225.0,"y":50.0,"z":300.0}}},{"package_item":{"name":"slice_front_bottom_right_right_back","height":100.0,"width":75.0,"length":150.0},"position":{"front_top_left_corner":{"x":225.0,"y":100.0,"z":450.0},"front_bottom_left_corner":{"x":225.0,"y":0,"z":450.0},"front_top_right_corner":{"x":300,"y":100.0,"z":450.0},"front_bottom_right_corner":{"x":300,"y":0,"z":450.0},"back_top_left_corner":{"x":225.0,"y":100.0,"z":300.0},"back_bottom_left_corner":{"x":225.0,"y":0,"z":300.0},"back_top_right_corner":{"x":300,"y":100.0,"z":300.0},"back_bottom_right_corner":{"x":300,"y":0,"z":300.0}}},{"package_item":{"name":"slice_front_bottom_right_right_front_bottom","height":50.0,"width":75.0,"length":150.0},"position":{"front_top_left_corner":{"x":225.0,"y":50.0,"z":600},"front_bottom_left_corner":{"x":225.0,"y":0,"z":600},"front_top_right_corner":{"x":300,"y":50.0,"z":600},"front_bottom_right_corner":{"x":300,"y":0,"z":600},"back_top_left_corner":{"x":225.0,"y":50.0,"z":450.0},"back_bottom_left_corner":{"x":225.0,"y":0,"z":450.0},"back_top_right_corner":{"x":300,"y":50.0,"z":450.0},"back_bottom_right_corner":{"x":300,"y":0,"z":450.0}}},{"package_item":{"name":"slice_front_bottom_right_right_front_top","height":50.0,"width":75.0,"length":150.0},"position":{"front_top_left_corner":{"x":225.0,"y":100.0,"z":600},"front_bottom_left_corner":{"x":225.0,"y":50.0,"z":600},"front_top_right_corner":{"x":300,"y":100.0,"z":600},"front_bottom_right_corner":{"x":300,"y":50.0,"z":600},"back_top_left_corner":{"x":225.0,"y":100.0,"z":450.0},"back_bottom_left_corner":{"x":225.0,"y":50.0,"z":450.0},"back_top_right_corner":{"x":300,"y":100.0,"z":450.0},"back_bottom_right_corner":{"x":300,"y":50.0,"z":450.0}}},{"package_item":{"name":"slice_front_top_left_bottom_bottom","height":25.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":125.0,"z":600},"front_bottom_left_corner":{"x":0,"y":100.0,"z":600},"front_top_right_corner":{"x":150.0,"y":125.0,"z":600},"front_bottom_right_corner":{"x":150.0,"y":100.0,"z":600},"back_top_left_corner":{"x":0,"y":125.0,"z":300.0},"back_bottom_left_corner":{"x":0,"y":100.0,"z":300.0},"back_top_right_corner":{"x":150.0,"y":125.0,"z":300.0},"back_bottom_right_corner":{"x":150.0,"y":100.0,"z":300.0}}},{"package_item":{"name":"slice_front_top_left_bottom_top","height":25.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":150.0,"z":600},"front_bottom_left_corner":{"x":0,"y":125.0,"z":600},"front_top_right_corner":{"x":150.0,"y":150.0,"z":600},"front_bottom_right_corner":{"x":150.0,"y":125.0,"z":600},"back_top_left_corner":{"x":0,"y":150.0,"z":300.0},"back_bottom_left_corner":{"x":0,"y":125.0,"z":300.0},"back_top_right_corner":{"x":150.0,"y":150.0,"z":300.0},"back_bottom_right_corner":{"x":150.0,"y":125.0,"z":300.0}}},{"package_item":{"name":"slice_front_top_left_top","height":50.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":600},"front_bottom_left_corner":{"x":0,"y":150.0,"z":600},"front_top_right_corner":{"x":150.0,"y":200,"z":600},"front_bottom_right_corner":{"x":150.0,"y":150.0,"z":600},"back_top_left_corner":{"x":0,"y":200,"z":300.0},"back_bottom_left_corner":{"x":0,"y":150.0,"z":300.0},"back_top_right_corner":{"x":150.0,"y":200,"z":300.0},"back_bottom_right_corner":{"x":150.0,"y":150.0,"z":300.0}}},{"package_item":{"name":"slice_front_top_right","height":100.0,"width":150.0,"length":300.0},"position":{"front_top_left_corner":{"x":150.0,"y":200,"z":600},"front_bottom_left_corner":{"x":150.0,"y":100.0,"z":600},"front_top_right_corner":{"x":300,"y":200,"z":600},"front_bottom_right_corner":{"x":300,"y":100.0,"z":600},"back_top_left_corner":{"x":150.0,"y":200,"z":300.0},"back_bottom_left_corner":{"x":150.0,"y":100.0,"z":300.0},"back_top_right_corner":{"x":300,"y":200,"z":300.0},"back_bottom_right_corner":{"x":300,"y":100.0,"z":300.0}}}],"container_item":{"name":"container1","height":200,"width":300,"length":600}}],"not_fitted_package_items":[]}}'
  res = json.loads(json_string)
  return res

def example4() -> ExampleTemplate:
  json_string = u'{"name":"example4","solver_input":{"container_items":[{"name":"container1","height":200,"width":300,"length":600}],"package_items":[{"name":"slice_front_left_front_right","height":200,"width":92,"length":216},{"name":"slice_front_left_back_top","height":120,"width":153,"length":144},{"name":"slice_back_front_back","height":200,"width":300,"length":86},{"name":"slice_front_left_back_bottom","height":80,"width":153,"length":144},{"name":"slice_front_left_front_left","height":200,"width":61,"length":216},{"name":"slice_back_front_front","height":200,"width":300,"length":58},{"name":"slice_back_back","height":200,"width":300,"length":96},{"name":"slice_front_right_right_front","height":200,"width":59,"length":144},{"name":"slice_front_right_left","height":200,"width":88,"length":360},{"name":"slice_front_right_right_back","height":200,"width":59,"length":216}]},"solver_output":{"is_success":true,"num_items_total":0,"num_items_fitted":0,"num_items_unfitted":0,"num_items_fitted_ratio":0,"total_fill_ratio":0,"solved_containers":[{"fill_ratio":1.0,"number_of_items_inside":10,"solution":[{"package_item":{"name":"slice_back_back","height":200,"width":300,"length":96},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":96},"front_bottom_left_corner":{"x":0,"y":0,"z":96},"front_top_right_corner":{"x":300,"y":200,"z":96},"front_bottom_right_corner":{"x":300,"y":0,"z":96},"back_top_left_corner":{"x":0,"y":200,"z":0},"back_bottom_left_corner":{"x":0,"y":0,"z":0},"back_top_right_corner":{"x":300,"y":200,"z":0},"back_bottom_right_corner":{"x":300,"y":0,"z":0}}},{"package_item":{"name":"slice_back_front_back","height":200,"width":300,"length":86},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":182},"front_bottom_left_corner":{"x":0,"y":0,"z":182},"front_top_right_corner":{"x":300,"y":200,"z":182},"front_bottom_right_corner":{"x":300,"y":0,"z":182},"back_top_left_corner":{"x":0,"y":200,"z":96},"back_bottom_left_corner":{"x":0,"y":0,"z":96},"back_top_right_corner":{"x":300,"y":200,"z":96},"back_bottom_right_corner":{"x":300,"y":0,"z":96}}},{"package_item":{"name":"slice_back_front_front","height":200,"width":300,"length":58},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":240},"front_bottom_left_corner":{"x":0,"y":0,"z":240},"front_top_right_corner":{"x":300,"y":200,"z":240},"front_bottom_right_corner":{"x":300,"y":0,"z":240},"back_top_left_corner":{"x":0,"y":200,"z":182},"back_bottom_left_corner":{"x":0,"y":0,"z":182},"back_top_right_corner":{"x":300,"y":200,"z":182},"back_bottom_right_corner":{"x":300,"y":0,"z":182}}},{"package_item":{"name":"slice_front_left_back_bottom","height":80,"width":153,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":80,"z":384},"front_bottom_left_corner":{"x":0,"y":0,"z":384},"front_top_right_corner":{"x":153,"y":80,"z":384},"front_bottom_right_corner":{"x":153,"y":0,"z":384},"back_top_left_corner":{"x":0,"y":80,"z":240},"back_bottom_left_corner":{"x":0,"y":0,"z":240},"back_top_right_corner":{"x":153,"y":80,"z":240},"back_bottom_right_corner":{"x":153,"y":0,"z":240}}},{"package_item":{"name":"slice_front_left_back_top","height":120,"width":153,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":384},"front_bottom_left_corner":{"x":0,"y":80,"z":384},"front_top_right_corner":{"x":153,"y":200,"z":384},"front_bottom_right_corner":{"x":153,"y":80,"z":384},"back_top_left_corner":{"x":0,"y":200,"z":240},"back_bottom_left_corner":{"x":0,"y":80,"z":240},"back_top_right_corner":{"x":153,"y":200,"z":240},"back_bottom_right_corner":{"x":153,"y":80,"z":240}}},{"package_item":{"name":"slice_front_left_front_left","height":200,"width":61,"length":216},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":600},"front_bottom_left_corner":{"x":0,"y":0,"z":600},"front_top_right_corner":{"x":61,"y":200,"z":600},"front_bottom_right_corner":{"x":61,"y":0,"z":600},"back_top_left_corner":{"x":0,"y":200,"z":384},"back_bottom_left_corner":{"x":0,"y":0,"z":384},"back_top_right_corner":{"x":61,"y":200,"z":384},"back_bottom_right_corner":{"x":61,"y":0,"z":384}}},{"package_item":{"name":"slice_front_left_front_right","height":200,"width":92,"length":216},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":61,"y":200,"z":600},"front_bottom_left_corner":{"x":61,"y":0,"z":600},"front_top_right_corner":{"x":153,"y":200,"z":600},"front_bottom_right_corner":{"x":153,"y":0,"z":600},"back_top_left_corner":{"x":61,"y":200,"z":384},"back_bottom_left_corner":{"x":61,"y":0,"z":384},"back_top_right_corner":{"x":153,"y":200,"z":384},"back_bottom_right_corner":{"x":153,"y":0,"z":384}}},{"package_item":{"name":"slice_front_right_left","height":200,"width":88,"length":360},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":153,"y":200,"z":600},"front_bottom_left_corner":{"x":153,"y":0,"z":600},"front_top_right_corner":{"x":241,"y":200,"z":600},"front_bottom_right_corner":{"x":241,"y":0,"z":600},"back_top_left_corner":{"x":153,"y":200,"z":240},"back_bottom_left_corner":{"x":153,"y":0,"z":240},"back_top_right_corner":{"x":241,"y":200,"z":240},"back_bottom_right_corner":{"x":241,"y":0,"z":240}}},{"package_item":{"name":"slice_front_right_right_back","height":200,"width":59,"length":216},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":241,"y":200,"z":456},"front_bottom_left_corner":{"x":241,"y":0,"z":456},"front_top_right_corner":{"x":300,"y":200,"z":456},"front_bottom_right_corner":{"x":300,"y":0,"z":456},"back_top_left_corner":{"x":241,"y":200,"z":240},"back_bottom_left_corner":{"x":241,"y":0,"z":240},"back_top_right_corner":{"x":300,"y":200,"z":240},"back_bottom_right_corner":{"x":300,"y":0,"z":240}}},{"package_item":{"name":"slice_front_right_right_front","height":200,"width":59,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":241,"y":200,"z":600},"front_bottom_left_corner":{"x":241,"y":0,"z":600},"front_top_right_corner":{"x":300,"y":200,"z":600},"front_bottom_right_corner":{"x":300,"y":0,"z":600},"back_top_left_corner":{"x":241,"y":200,"z":456},"back_bottom_left_corner":{"x":241,"y":0,"z":456},"back_top_right_corner":{"x":300,"y":200,"z":456},"back_bottom_right_corner":{"x":300,"y":0,"z":456}}}],"container_item":{"name":"container1","height":200,"width":300,"length":600}}],"not_fitted_package_items":[]}}'
  res = json.loads(json_string)
  return res

def example5() -> ExampleTemplate:
  json_string = u'{"name":"example5","solver_input":{"container_items":[{"name":"container1","height":200,"width":300,"length":600}],"package_items":[{"name":"slice_right_right_front","height":200,"width":80,"length":360},{"name":"slice_left_front_bottom","height":120,"width":120,"length":360},{"name":"slice_left_back_back_right","height":200,"width":72,"length":144},{"name":"slice_right_left_top","height":80,"width":100,"length":600},{"name":"slice_left_front_top_back","height":80,"width":120,"length":144},{"name":"slice_right_right_back","height":200,"width":80,"length":240},{"name":"slice_left_back_front_top","height":80,"width":120,"length":96},{"name":"slice_left_back_back_left","height":200,"width":48,"length":144},{"name":"slice_right_left_bottom","height":120,"width":100,"length":600},{"name":"slice_left_front_top_front","height":80,"width":120,"length":216},{"name":"slice_left_back_front_bottom","height":120,"width":120,"length":96}]},"solver_output":{"is_success":true,"num_items_total":0,"num_items_fitted":0,"num_items_unfitted":0,"num_items_fitted_ratio":0,"total_fill_ratio":0,"solved_containers":[{"fill_ratio":1.0,"number_of_items_inside":11,"solution":[{"package_item":{"name":"slice_left_back_back_left","height":200,"width":48,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":144},"front_bottom_left_corner":{"x":0,"y":0,"z":144},"front_top_right_corner":{"x":48,"y":200,"z":144},"front_bottom_right_corner":{"x":48,"y":0,"z":144},"back_top_left_corner":{"x":0,"y":200,"z":0},"back_bottom_left_corner":{"x":0,"y":0,"z":0},"back_top_right_corner":{"x":48,"y":200,"z":0},"back_bottom_right_corner":{"x":48,"y":0,"z":0}}},{"package_item":{"name":"slice_left_back_back_right","height":200,"width":72,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":48,"y":200,"z":144},"front_bottom_left_corner":{"x":48,"y":0,"z":144},"front_top_right_corner":{"x":120,"y":200,"z":144},"front_bottom_right_corner":{"x":120,"y":0,"z":144},"back_top_left_corner":{"x":48,"y":200,"z":0},"back_bottom_left_corner":{"x":48,"y":0,"z":0},"back_top_right_corner":{"x":120,"y":200,"z":0},"back_bottom_right_corner":{"x":120,"y":0,"z":0}}},{"package_item":{"name":"slice_left_back_front_bottom","height":120,"width":120,"length":96},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":120,"z":240},"front_bottom_left_corner":{"x":0,"y":0,"z":240},"front_top_right_corner":{"x":120,"y":120,"z":240},"front_bottom_right_corner":{"x":120,"y":0,"z":240},"back_top_left_corner":{"x":0,"y":120,"z":144},"back_bottom_left_corner":{"x":0,"y":0,"z":144},"back_top_right_corner":{"x":120,"y":120,"z":144},"back_bottom_right_corner":{"x":120,"y":0,"z":144}}},{"package_item":{"name":"slice_left_back_front_top","height":80,"width":120,"length":96},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":240},"front_bottom_left_corner":{"x":0,"y":120,"z":240},"front_top_right_corner":{"x":120,"y":200,"z":240},"front_bottom_right_corner":{"x":120,"y":120,"z":240},"back_top_left_corner":{"x":0,"y":200,"z":144},"back_bottom_left_corner":{"x":0,"y":120,"z":144},"back_top_right_corner":{"x":120,"y":200,"z":144},"back_bottom_right_corner":{"x":120,"y":120,"z":144}}},{"package_item":{"name":"slice_left_front_bottom","height":120,"width":120,"length":360},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":120,"z":600},"front_bottom_left_corner":{"x":0,"y":0,"z":600},"front_top_right_corner":{"x":120,"y":120,"z":600},"front_bottom_right_corner":{"x":120,"y":0,"z":600},"back_top_left_corner":{"x":0,"y":120,"z":240},"back_bottom_left_corner":{"x":0,"y":0,"z":240},"back_top_right_corner":{"x":120,"y":120,"z":240},"back_bottom_right_corner":{"x":120,"y":0,"z":240}}},{"package_item":{"name":"slice_left_front_top_back","height":80,"width":120,"length":144},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":384},"front_bottom_left_corner":{"x":0,"y":120,"z":384},"front_top_right_corner":{"x":120,"y":200,"z":384},"front_bottom_right_corner":{"x":120,"y":120,"z":384},"back_top_left_corner":{"x":0,"y":200,"z":240},"back_bottom_left_corner":{"x":0,"y":120,"z":240},"back_top_right_corner":{"x":120,"y":200,"z":240},"back_bottom_right_corner":{"x":120,"y":120,"z":240}}},{"package_item":{"name":"slice_left_front_top_front","height":80,"width":120,"length":216},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":0,"y":200,"z":600},"front_bottom_left_corner":{"x":0,"y":120,"z":600},"front_top_right_corner":{"x":120,"y":200,"z":600},"front_bottom_right_corner":{"x":120,"y":120,"z":600},"back_top_left_corner":{"x":0,"y":200,"z":384},"back_bottom_left_corner":{"x":0,"y":120,"z":384},"back_top_right_corner":{"x":120,"y":200,"z":384},"back_bottom_right_corner":{"x":120,"y":120,"z":384}}},{"package_item":{"name":"slice_right_left_bottom","height":120,"width":100,"length":600},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":120,"y":120,"z":600},"front_bottom_left_corner":{"x":120,"y":0,"z":600},"front_top_right_corner":{"x":220,"y":120,"z":600},"front_bottom_right_corner":{"x":220,"y":0,"z":600},"back_top_left_corner":{"x":120,"y":120,"z":0},"back_bottom_left_corner":{"x":120,"y":0,"z":0},"back_top_right_corner":{"x":220,"y":120,"z":0},"back_bottom_right_corner":{"x":220,"y":0,"z":0}}},{"package_item":{"name":"slice_right_left_top","height":80,"width":100,"length":600},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":120,"y":200,"z":600},"front_bottom_left_corner":{"x":120,"y":120,"z":600},"front_top_right_corner":{"x":220,"y":200,"z":600},"front_bottom_right_corner":{"x":220,"y":120,"z":600},"back_top_left_corner":{"x":120,"y":200,"z":0},"back_bottom_left_corner":{"x":120,"y":120,"z":0},"back_top_right_corner":{"x":220,"y":200,"z":0},"back_bottom_right_corner":{"x":220,"y":120,"z":0}}},{"package_item":{"name":"slice_right_right_back","height":200,"width":80,"length":240},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":220,"y":200,"z":240},"front_bottom_left_corner":{"x":220,"y":0,"z":240},"front_top_right_corner":{"x":300,"y":200,"z":240},"front_bottom_right_corner":{"x":300,"y":0,"z":240},"back_top_left_corner":{"x":220,"y":200,"z":0},"back_bottom_left_corner":{"x":220,"y":0,"z":0},"back_top_right_corner":{"x":300,"y":200,"z":0},"back_bottom_right_corner":{"x":300,"y":0,"z":0}}},{"package_item":{"name":"slice_right_right_front","height":200,"width":80,"length":360},"centre_point":{"x":0.0,"y":0.0,"z":0.0},"position":{"front_top_left_corner":{"x":220,"y":200,"z":600},"front_bottom_left_corner":{"x":220,"y":0,"z":600},"front_top_right_corner":{"x":300,"y":200,"z":600},"front_bottom_right_corner":{"x":300,"y":0,"z":600},"back_top_left_corner":{"x":220,"y":200,"z":240},"back_bottom_left_corner":{"x":220,"y":0,"z":240},"back_top_right_corner":{"x":300,"y":200,"z":240},"back_bottom_right_corner":{"x":300,"y":0,"z":240}}}],"container_item":{"name":"container1","height":200,"width":300,"length":600}}],"not_fitted_package_items":[]}}'
  res = json.loads(json_string)
  return res

def next_random_example() -> ExampleTemplate:
  height = 200
  width = 300
  length = 600

  solved_container = SolvedContainer()

  # Create container with given dimensions.
  solved_container.container_item  = ContainerItem(name="container1", height=height, width=width, length=length)

  # Create initial package with the same dimensions as container.
  package_item = PackageItem(name="slice", height=height, width=width, length=length)
  pos = package_item.to_position3d_from_back_bottom_left_corner(back_bottom_left_corner=Point3d(x=0,y=0,z=0))
  positioned_package = PositionedPackage(package_item=package_item, position=pos)

  slice_result = bs.slice_random_n_times(bin=positioned_package, num_loops=rnd.randint(4, 7))
  
  solved_container.solution = slice_result
  solved_container.set_calculated_props()

  output = SolverOutput()
  output.solved_containers = [solved_container]
  output.is_success = True

  input = SolverInput()
  input.container_items = [solved_container.container_item]
  input.package_items = [i.package_item for i in solved_container.solution]
  rnd.shuffle(input.package_items)

  res = ExampleTemplate(name="random1", solver_input=input, solver_output=output)
  return res
