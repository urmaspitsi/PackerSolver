from typing import List, Tuple
from pydantic import BaseModel

from Models.point3d import Point3d

class Position3d(BaseModel):
  '''
    Position of a package is defined as a set of its 8 corners with there respective coordinates.
    Package position contains 8 corners of a rectangular cuboid.
    Each corner is represented as PointCoordinate.
    8 PointCoordinates or 8 3-typles of (x,y,z) coordinate values.
  '''

  front_top_left_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  front_bottom_left_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  front_top_right_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  front_bottom_right_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)

  back_top_left_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  back_bottom_left_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  back_top_right_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)
  back_bottom_right_corner: Point3d = Point3d(x=0.0, y=0.0, z=0.0)

  def adjust_with_centre_point(self, centre_point: Point3d):

    self.back_bottom_left_corner = self.back_bottom_left_corner.add(centre_point)
    self.back_bottom_right_corner = self.back_bottom_right_corner.add(centre_point)
    self.back_top_left_corner = self.back_top_left_corner.add(centre_point)
    self.back_top_right_corner = self.back_top_right_corner.add(centre_point)
    
    self.front_bottom_left_corner = self.front_bottom_left_corner.add(centre_point)
    self.front_bottom_right_corner = self.front_bottom_right_corner.add(centre_point)
    self.front_top_left_corner = self.front_top_left_corner.add(centre_point)
    self.front_top_right_corner = self.front_top_right_corner.add(centre_point)

    return self

  @staticmethod
  def create_from_corners(
      front_top_left_corner: Point3d,
      front_bottom_left_corner: Point3d,
      front_top_right_corner: Point3d,
      front_bottom_right_corner: Point3d,
      back_top_left_corner: Point3d,
      back_bottom_left_corner: Point3d,
      back_top_right_corner: Point3d,
      back_bottom_right_corner: Point3d
      ):

    res = Position3d()

    res.back_bottom_left_corner = back_bottom_left_corner.copy()
    res.back_bottom_right_corner = back_bottom_right_corner.copy()
    res.back_top_left_corner = back_top_left_corner.copy()
    res.back_top_right_corner = back_top_right_corner.copy()
    
    res.front_bottom_left_corner = front_bottom_left_corner.copy()
    res.front_bottom_right_corner = front_bottom_right_corner.copy()
    res.front_top_left_corner = front_top_left_corner.copy()
    res.front_top_right_corner = front_top_right_corner.copy()

    return res

  @staticmethod
  def create_from_centre_point(centre_point: Point3d, height: float, width: float, length: float):
    adjust_point = Point3d(
      x=centre_point.x - width / 2,
      y=centre_point.y - height / 2,
      z=centre_point.z - length / 2
    )

    return Position3d.create_from_dimensions(
      height=height,
      width=width,
      length=length).adjust_with_centre_point(centre_point=adjust_point)

  @staticmethod
  def create_from_dimensions(height: float, width: float, length: float):

    res = Position3d()

    res.back_bottom_left_corner = Point3d(x=0.0, y=0.0, z=0.0)
    res.back_bottom_right_corner = Point3d(x=width, y=0.0, z=0.0)
    res.back_top_left_corner = Point3d(x=0.0, y=height, z=0.0)
    res.back_top_right_corner = Point3d(x=width, y=height, z=0.0)

    res.front_bottom_left_corner = Point3d(x=0.0, y=0.0, z=length)
    res.front_bottom_right_corner = Point3d(x=width, y=0.0, z=length)
    res.front_top_left_corner = Point3d(x=0.0, y=height, z=length)
    res.front_top_right_corner = Point3d(x=width, y=height, z=length)

    return res

  def width(self) -> float:
    return self.back_bottom_right_corner.x - self.back_bottom_left_corner.x

  def height(self) -> float:
    return self.back_top_left_corner.y - self.back_bottom_left_corner.y

  def length(self) -> float:
    return self.front_bottom_left_corner.z - self.back_bottom_left_corner.z

  def is_valid(self) -> bool:
    return self.width() > 0 and self.height() > 0 and self.length() > 0 \
        and self.front_top_left_corner.is_valid() \
        and self.front_bottom_left_corner.is_valid() \
        and self.front_top_right_corner.is_valid() \
        and self.front_bottom_right_corner.is_valid() \
        and self.back_top_left_corner.is_valid() \
        and self.back_bottom_left_corner.is_valid() \
        and self.back_top_right_corner.is_valid() \
        and self.back_bottom_right_corner.is_valid()
