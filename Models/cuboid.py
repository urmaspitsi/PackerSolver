from typing import Any, Optional
from pydantic import BaseModel

from Models.position3d import Position3d
from Models.point3d import Point3d

class Cuboid(BaseModel):
  '''
    Generic bin or rectangular cuboid.
  '''

  name: str = ""
  height: float = 0.0
  width: float = 0.0
  length: float = 0.0
  #applied_rotation: str = ""

  def __init__(
      __pydantic_self__,
      name: str="",
      height: float = 0.0,
      width: float = 0.0,
      length: float = 0.0,
      **data: Any
    ) -> None:

    super().__init__(**data)
    __pydantic_self__.name = name
    __pydantic_self__.height = height
    __pydantic_self__.width = width
    __pydantic_self__.length = length

  def volume(self) -> float:
    return self.height * self.width * self.length

  def surface_area(self) -> float:
    return (self.height * self.width) * 2 + (self.width * self.length) * 2 + (self.height * self.length) * 2

  def get_x(self) -> float:
    return self.width

  def get_y(self) -> float:
    return self.height

  def get_z(self) -> float:
    return self.length

  def rotate_x(self):
    '''
      Rotate 90 degrees along x-axis.
      Imagine you sit on an axis and look towards the origin. Rotate (clockwise) 90 degrees.
    '''
    res = self.copy()
    res.height = self.length
    res.length = self.height
    res.applied_rotation = f"{res.applied_rotation}X"
    return res

  def rotate_y(self):
    '''
      Rotate 90 degrees along y-axis.
      Imagine you sit on an axis and look towards the origin. Rotate (clockwise) 90 degrees.
    '''
    res = self.copy()
    res.width = self.length
    res.length = self.width
    res.applied_rotation = f"{res.applied_rotation}Y"
    return res

  def rotate_z(self):
    '''
      Rotate 90 degrees along z-axis.
      Imagine you sit on an axis and look towards the origin. Rotate (clockwise) 90 degrees.
    '''
    res = self.copy()
    res.width = self.height
    res.height = self.width
    res.applied_rotation = f"{res.applied_rotation}Y"
    return res

  def rotate_left_side_up(self):
    return self.rotate_z()

  def rotate_front_side_up(self):
    return self.rotate_x()

  def rotate_front_side_left(self):
    return self.rotate_y()

  def create_from_position3d(self, pos3d: Position3d):
    res = self.copy()
    res.width = pos3d.width()
    res.height = pos3d.height()
    res.length = pos3d.length()
    return res

  def to_position3d_from_back_bottom_left_corner(self, back_bottom_left_corner: Point3d) -> Position3d:

    res = Position3d()

    res.back_bottom_left_corner = back_bottom_left_corner.copy()
    res.back_bottom_right_corner = back_bottom_left_corner.add_x(self.width)
    res.back_top_left_corner = back_bottom_left_corner.add_y(self.height)
    res.back_top_right_corner = res.back_bottom_right_corner.add_y(self.height)
    
    res.front_bottom_left_corner = back_bottom_left_corner.add_z(self.length)
    res.front_bottom_right_corner = res.front_bottom_left_corner.add_x(self.width)
    res.front_top_left_corner = res.front_bottom_left_corner.add_y(self.height)
    res.front_top_right_corner = res.front_bottom_right_corner.add_y(self.height)

    return res

  def get_centre_point(self) -> Point3d:
    return Point3d(
        x = self.width / 2,
        y = self.height / 2,
        z = self.length / 2
      )

  def get_centre_point_from_back_bottom_left_corner(self, back_bottom_left_corner: Point3d) -> Point3d:
    return self.get_centre_point().add(back_bottom_left_corner)
