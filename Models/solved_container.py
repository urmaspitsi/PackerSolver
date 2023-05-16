from typing import Any, List
from pydantic import BaseModel
from Models.container_item import ContainerItem
from Models.positioned_package import PositionedPackage

class SolvedContainer(BaseModel):
  '''
    SolvedContainer contains data about container item together with the solution of a packing.
    container_item: a container inside what packages are positioned.
    solution: list of packages with corresponding position coordinates.
    fill_ratio: ratio of how much of the volume inside the container is filled
      fill_ratio = sum of volumes of all packages / volume of the container.

  '''

  container_item = ContainerItem()
  fill_ratio: float = 0.0
  number_of_items_inside: int = 0
  #is_success: bool = False
  solution: List[PositionedPackage] = []

  def __init__(
          __pydantic_self__,
          container_item: ContainerItem = ContainerItem(),
          solution: List[PositionedPackage] = [],
          **data: Any
        ) -> None:
      super().__init__(**data)
      __pydantic_self__.container_item = container_item
      __pydantic_self__.solution = solution
      #__pydantic_self__.fill_ratio = __pydantic_self__.get_fill_ratio()
      #if __pydantic_self__.fill_ratio > 0.00001:
      #  __pydantic_self__.is_success = True

  def get_fill_ratio(self) -> float:
    container_volume = self.container_item.volume()
    packages_volume = sum([x.package_item.volume() for x in self.solution])
    return 0 if container_volume < 0.000001 else packages_volume / container_volume

  def set_calculated_props(self):
    self.fill_ratio = round(self.get_fill_ratio(), 4)
    self.number_of_items_inside = len(self.solution)
