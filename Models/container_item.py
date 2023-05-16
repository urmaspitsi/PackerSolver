from typing import Any

from Models.cuboid import Cuboid

class ContainerItem(Cuboid):
  '''
    ContainerItem is a container inside what items (PackageItem) are packed.
    Dimensions are specified as:
      height = y-axis
      width = x-axis
      length = z-axis
    
    NB:
      Dimensions do not reflect their relative size.
      Dimensions can be chosen arbitrarily, ie length could be smallest value of the three.
  '''
  def __init__(__pydantic_self__, name: str = "", height: float = 0, width: float = 0, length: float = 0, **data: Any) -> None:
      super().__init__(name=name, height=height, width=width, length=length, **data)
