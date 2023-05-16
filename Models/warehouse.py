from typing import Any, Dict, List
from Models.package_item import PackageItem
from Models.position3d import Position3d
from Models.positioned_package import PositionedPackage
from Models.container_item import ContainerItem
from Models.positioned_container import PositionedContainer
from Models.solved_container import SolvedContainer
from Models.solver_output import SolverOutput

class Warehouse(ContainerItem):
  '''
    Warehouse.
    Dimensions are specified as:
      height = y-axis
      width = x-axis
      length = z-axis
    
    NB:
      Dimensions do not reflect their relative size.
      Dimensions can be chosen arbitrarily, ie length could be smallest value of the three.
  '''

  fillable_space: Dict[str, PositionedContainer] = {}
  #non_fillable_space: List[PositionedPackage] = []

  def __init__(__pydantic_self__, name: str = "", height: float = 0, width: float = 0, length: float = 0, **data: Any) -> None:
      super().__init__(name=name, height=height, width=width, length=length, **data)


  def to_solved_container(self) -> SolvedContainer:
    '''
      Convert warhouse into solved container for visualisation purposes.
    '''
    res = SolvedContainer(container_item=ContainerItem(
                                        name=self.name,
                                        width=self.width,
                                        height=self.height,
                                        length=self.length
                                        )
                          )
    solution: List[PositionedPackage] = []

    for k,v in self.fillable_space.items():
      pack = PackageItem(
        name=k,
        width=v.container_item.width,
        height=v.container_item.height,
        length=v.container_item.length
        )

      pos_pack = PositionedPackage(
          package_item=pack,
          position=Position3d.create_from_centre_point(
            centre_point=v.centre_point,
            width=pack.width,
            height=pack.height,
            length=pack.length
          )
        )

      pos_pack.centre_point = v.centre_point
      solution.append(pos_pack)

    res.solution = solution
    res.set_calculated_props()
    return res
  
  def to_solver_output(self) -> SolverOutput:
    '''
      Convert warhouse into SolverOutput for visualisation purposes.
    '''
    res = SolverOutput()
    solved_cont = self.to_solved_container()
    res.solved_containers = [solved_cont]
    return res
