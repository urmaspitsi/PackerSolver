from typing import List, Tuple
from Models.dimensions import Dimensions
from Models.warehouse import Warehouse
from ..container_item import ContainerItem
from ..package_item import PackageItem
from ..positioned_container import PositionedContainer

# Build warehouse as a container containing containers (shelves).
# Warehouse contains fillable space: collection of Containers where to store items.


def is_warehouse(container_item: ContainerItem, package_items: List[PackageItem]) -> Tuple[bool, Warehouse]:
  if (int(container_item.width) == 401 and int(container_item.height) == 251 and int(container_item.length) == 801):
    return (True, garage48())
  elif (int(container_item.width) == 701 and int(container_item.height) == 851 and int(container_item.length) == 1501):
    return (True, bauhof_aisle())

  return (False, None)


def warehouse_with_shelves_along_sides(
    name:str,
    warehouse_dims: Dimensions,
    shelf_depth: float,
    shelf_height: float
  ) -> Warehouse:

  '''
    Shelves/storage spaces along left and right sides.
  '''

  res = Warehouse(
      name=name,
      width=warehouse_dims.width,
      height=warehouse_dims.height,
      length=warehouse_dims.length
    )
  
  conts_left = [ContainerItem(name=f"shelf_left_{i}", width=shelf_depth, height=shelf_height, length=res.length) for i in range(1, 11)]
  conts_right = [ContainerItem(name=f"shelf_right_{i}", width=shelf_depth, height=shelf_height, length=res.length) for i in range(1, 11)]
  
  left_side = [PositionedContainer(container_item=c, centre_point=c.get_centre_point().add_y(i * shelf_height)) for i,c in enumerate(conts_left)]
  right_side = [PositionedContainer(container_item=c, centre_point=c.get_centre_point().add_y(i * shelf_height).add_x(res.width - shelf_depth)) for i,c in enumerate(conts_right)]

  for cont in left_side + right_side:
     if cont.centre_point.y < (res.height - shelf_height / 2):
      res.fillable_space[cont.container_item.name] = cont

  #res.fillable_space = { cont.container_item.name: cont for cont in (left_side + right_side) if cont.centre_point.y < res.height - shelf_height / 2 }

  return res


def garage48() -> Warehouse:
  return warehouse_with_shelves_along_sides(
    name="Garage48",
    warehouse_dims=Dimensions(width=401, height=251, length=801),
    shelf_depth=100,
    shelf_height=120
  )

def bauhof_aisle() -> Warehouse:
  return warehouse_with_shelves_along_sides(
    name="Bauhof aisle",
    warehouse_dims=Dimensions(width=701, height=851, length=1501),
    shelf_depth=120,
    shelf_height=150
  )
