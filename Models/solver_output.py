from typing import List, Any
from pydantic import BaseModel
from Models.package_item import PackageItem
from Models.solved_container import SolvedContainer

class SolverOutput(BaseModel):
  '''
    Contains results of the solver.
    solved_containers: list of SolvedContainers. Solved container includes information
      about packages inside it together with there corresponding position coordinates.
    not_fitted_package_items: items that were not fitted into any container.
  '''

  is_success: bool = False
  num_items_total: int = 0
  num_items_fitted: int = 0
  num_items_unfitted: int = 0
  num_items_fitted_ratio: float = 0
  total_fill_ratio: float = 0
  solved_containers: List[SolvedContainer] = []
  not_fitted_package_items: List[PackageItem] = []

