from typing import Any
from pydantic import BaseModel

from Models.container_item import ContainerItem
from Models.point3d import Point3d

class PositionedContainer(BaseModel):
  '''
    Positioned container: container item together with its 3-dim position.
    
  '''

  container_item: ContainerItem = ContainerItem()
  centre_point: Point3d = Point3d()

  def __init__(__pydantic_self__,
        container_item: ContainerItem=ContainerItem(),
        centre_point: Point3d=Point3d(),
        **data: Any) -> None:

      super().__init__(**data)
      __pydantic_self__.container_item = container_item
      __pydantic_self__.centre_point = centre_point

  @staticmethod
  def create_from_back_bottom_left_corner(
        container_item: ContainerItem,
        back_bottom_left_corner: Point3d
        ):

    return PositionedContainer(
      container_item=container_item.copy(),
      centre_point=container_item.get_centre_point_from_back_bottom_left_corner(
            back_bottom_left_corner=back_bottom_left_corner)

    )
