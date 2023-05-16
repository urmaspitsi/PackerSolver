from typing import List, Any
from pydantic import BaseModel

from Models.package_item import PackageItem
from Models.position3d import Position3d
from Models.point3d import Point3d

class PositionedPackage(BaseModel):
  '''
    Positioned package: package item together with its 3-dim position.
    
  '''

  package_item: PackageItem = PackageItem()
  centre_point: Point3d = Point3d()
  position: Position3d = Position3d()

  def __init__(__pydantic_self__, package_item: PackageItem=PackageItem(), position: Position3d=Position3d(), **data: Any) -> None:
      super().__init__(**data)
      __pydantic_self__.package_item = package_item
      __pydantic_self__.position = position

  @staticmethod
  def create_from_back_bottom_left_corner(
        package_item: PackageItem,
        back_bottom_left_corner: Point3d
        ):
    res = PositionedPackage()
    res.package_item = package_item.copy()

    res.position = res.package_item.to_position3d_from_back_bottom_left_corner(
                    back_bottom_left_corner=back_bottom_left_corner
                    )

    res.centre_point=package_item.get_centre_point_from_back_bottom_left_corner(
            back_bottom_left_corner=back_bottom_left_corner)

    return res
