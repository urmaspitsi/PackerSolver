from typing import List, Any
from pydantic import BaseModel

class Point3d(BaseModel):
  x: float = 0.0
  y: float = 0.0
  z: float = 0.0

  def __init__(__pydantic_self__, x: float=0.0, y: float=0.0, z: float=0.0, **data: Any) -> None:
    super().__init__(**data)
    __pydantic_self__.x = x
    __pydantic_self__.y = y
    __pydantic_self__.z = z

  def add(self, add_point3d):
    return Point3d(
        x = self.x + add_point3d.x,
        y = self.y + add_point3d.y,
        z = self.z + add_point3d.z,
      )

  def add_x(self, add_value: float):
    res = self.copy()
    res.x += add_value
    return res

  def add_y(self, add_value: float):
    res = self.copy()
    res.y += add_value
    return res

  def add_z(self, add_value: float):
    res = self.copy()
    res.z += add_value
    return res
  
  def is_valid(self) -> bool:
    return not (self.x < 0 or self.y < 0 or self.z < 0)
