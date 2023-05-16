
from typing import List, Tuple
from pydantic import BaseModel
import random as rnd
rnd.seed(10101)

from Models.positioned_package import PositionedPackage
from Models.package_item import PackageItem
from Models.position3d import Position3d
from Models.point3d import Point3d

class BinSlicer(BaseModel):
  '''
    BinSlicer: slice rectangular cuboid into two pieces.
  '''

  # height: float = 0.0
  # width: float = 0.0
  # length: float = 0.0
  # num_pieces: int = 2


def slice_intersect_x(bin: PositionedPackage, intersect_x_at: float) -> Tuple[PositionedPackage]:
  '''
    Slices a bin into 2 bins.
    Returns list[PositionedPackage] that contains 2 elements.
  '''

  pos = bin.position
  front_top_at_x = Point3d(x=intersect_x_at, y=pos.front_top_left_corner.y, z=pos.front_top_left_corner.z)
  front_bottom_at_x = Point3d(x=intersect_x_at, y=pos.front_bottom_left_corner.y, z=pos.front_bottom_left_corner.z)
  back_top_at_x = Point3d(x=intersect_x_at, y=pos.back_top_left_corner.y, z=pos.back_top_left_corner.z)
  back_bottom_at_x = Point3d(x=intersect_x_at, y=pos.back_bottom_left_corner.y, z=pos.back_bottom_left_corner.z)
  
  left_position = Position3d.create_from_corners(
    front_top_left_corner = pos.front_top_left_corner,
    front_bottom_left_corner = pos.front_bottom_left_corner,
    back_top_left_corner = pos.back_top_left_corner,
    back_bottom_left_corner = pos.back_bottom_left_corner,

    front_top_right_corner = front_top_at_x,
    front_bottom_right_corner = front_bottom_at_x,
    back_top_right_corner = back_top_at_x,
    back_bottom_right_corner = back_bottom_at_x,
    )

  right_position = Position3d.create_from_corners(
    front_top_left_corner = front_top_at_x,
    front_bottom_left_corner = front_bottom_at_x,
    back_top_left_corner = back_top_at_x,
    back_bottom_left_corner = back_bottom_at_x,

    front_top_right_corner = pos.front_top_right_corner,
    front_bottom_right_corner = pos.front_bottom_right_corner,
    back_top_right_corner = pos.back_top_right_corner,
    back_bottom_right_corner = pos.back_bottom_right_corner,
    )

  left = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_left").create_from_position3d(pos3d=left_position),
              position = left_position
            )

  right = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_right").create_from_position3d(pos3d=right_position),
              position = right_position
            )

  return (left, right)

def slice_intersect_y(bin: PositionedPackage, intersect_y_at: float) -> Tuple[PositionedPackage]:
  '''
    Slices a bin into 2 bins.
    Returns list[PositionedPackage] that contains 2 elements.
  '''

  pos = bin.position
  front_left_at_y = Point3d(x=pos.front_top_left_corner.x, y=intersect_y_at, z=pos.front_top_left_corner.z)
  front_right_at_y = Point3d(x=pos.front_top_right_corner.x, y=intersect_y_at, z=pos.front_top_right_corner.z)
  back_left_at_y = Point3d(x=pos.back_top_left_corner.x, y=intersect_y_at, z=pos.back_top_left_corner.z)
  back_right_at_y = Point3d(x=pos.back_top_right_corner.x, y=intersect_y_at, z=pos.back_top_right_corner.z)

  bottom_position = Position3d.create_from_corners(
    front_bottom_left_corner = pos.front_bottom_left_corner,
    back_bottom_left_corner = pos.back_bottom_left_corner,
    front_bottom_right_corner = pos.front_bottom_right_corner,
    back_bottom_right_corner = pos.back_bottom_right_corner,

    front_top_left_corner = front_left_at_y,
    back_top_left_corner = back_left_at_y,
    front_top_right_corner = front_right_at_y,
    back_top_right_corner = back_right_at_y,
    )

  top_position = Position3d.create_from_corners(
    front_bottom_left_corner = front_left_at_y,
    back_bottom_left_corner = back_left_at_y,
    front_bottom_right_corner = front_right_at_y,
    back_bottom_right_corner = back_right_at_y,

    front_top_left_corner = pos.front_top_left_corner,
    back_top_left_corner = pos.back_top_left_corner,
    front_top_right_corner = pos.front_top_right_corner,
    back_top_right_corner = pos.back_top_right_corner,
    )

  bottom = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_bottom").create_from_position3d(pos3d=bottom_position),
              position = bottom_position
            )

  top = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_top").create_from_position3d(pos3d=top_position),
              position = top_position
            )

  return (bottom, top)

def slice_intersect_z(bin: PositionedPackage, intersect_z_at: float) -> Tuple[PositionedPackage]:
  '''
    Slices a bin into 2 bins.
    Returns list[PositionedPackage] that contains 2 elements.
  '''

  pos = bin.position
  top_left_at_z = Point3d(x=pos.front_top_left_corner.x, y=pos.front_top_left_corner.y, z=intersect_z_at)
  top_right_at_z = Point3d(x=pos.front_top_right_corner.x, y=pos.front_top_right_corner.y, z=intersect_z_at)
  bottom_left_at_z = Point3d(x=pos.front_bottom_left_corner.x, y=pos.front_bottom_left_corner.y, z=intersect_z_at)
  bottom_right_at_z = Point3d(x=pos.front_bottom_right_corner.x, y=pos.front_bottom_right_corner.y, z=intersect_z_at)

  back_position = Position3d.create_from_corners(
    back_bottom_left_corner = pos.back_bottom_left_corner,
    back_bottom_right_corner = pos.back_bottom_right_corner,
    back_top_left_corner = pos.back_top_left_corner,
    back_top_right_corner = pos.back_top_right_corner,

    front_bottom_left_corner = bottom_left_at_z,
    front_bottom_right_corner = bottom_right_at_z,
    front_top_left_corner = top_left_at_z,
    front_top_right_corner = top_right_at_z,
    )

  front_position = Position3d.create_from_corners(
    back_bottom_left_corner = bottom_left_at_z,
    back_bottom_right_corner = bottom_right_at_z,
    back_top_left_corner = top_left_at_z,
    back_top_right_corner = top_right_at_z,

    front_bottom_left_corner = pos.front_bottom_left_corner,
    front_bottom_right_corner = pos.front_bottom_right_corner,
    front_top_left_corner = pos.front_top_left_corner,
    front_top_right_corner = pos.front_top_right_corner,
    )

  back = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_back").create_from_position3d(pos3d=back_position),
              position = back_position
            )

  front = PositionedPackage(
              package_item = PackageItem(name=f"{bin.package_item.name}_front").create_from_position3d(pos3d=front_position),
              position = front_position
            )

  return (back, front)

def slice_random_axis(bin: PositionedPackage) -> Tuple[PositionedPackage]:
  '''
    Slices a bin into 2 bins by randomly choosing axis and intersectionpoint.
    Returns list[PositionedPackage] that contains 2 elements.
  '''

  axis_nr = rnd.randint(0, 2)
  res: Tuple[PositionedPackage] = []
  intersection_value: float = 0
  pos = bin.position

  random_ratio = rnd.random()
  # keep ration between some bounds eg 20%..80%
  if random_ratio < 0.4:
    random_ratio = 0.4
  elif random_ratio > 0.6:
    random_ratio = 0.6

  if axis_nr == 0:
    intersection_value = int(random_ratio * bin.package_item.width + pos.back_top_left_corner.x)
    #intersection_value = (pos.back_top_right_corner.x + pos.back_top_left_corner.x) / 2
    res = slice_intersect_x(bin=bin, intersect_x_at=intersection_value)
  elif axis_nr == 1:
    intersection_value = int(random_ratio * bin.package_item.height + pos.back_bottom_left_corner.y)
    #intersection_value = (pos.back_top_left_corner.y + pos.back_bottom_left_corner.y) / 2
    res = slice_intersect_y(bin=bin, intersect_y_at=intersection_value)
  else:
    intersection_value = int(random_ratio * bin.package_item.length + pos.back_bottom_left_corner.z)
    #intersection_value = (pos.front_bottom_left_corner.z + pos.back_bottom_left_corner.z) / 2
    res = slice_intersect_z(bin=bin, intersect_z_at=intersection_value)

  return res

def slice_random_n_times(bin: PositionedPackage, num_loops: int=1) -> List[PositionedPackage]:
  '''
    Slices a bin n-times randomly.
    Returns list[PositionedPackage] that contains 2 elements.
  '''

  ls1: List[PositionedPackage] = [bin]
  res: List[PositionedPackage] = []

  for _ in range(num_loops):
    res = []
    for pack in ls1:
      if rnd.random() < 0.8:
        res.extend(slice_random_axis(bin=pack))
      else:
        res.append(pack)
    ls1 = res.copy()

  return res












