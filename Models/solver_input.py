from typing import List, Any
from pydantic import BaseModel

from Models.container_item import ContainerItem
from Models.package_item import PackageItem

class SolverInput(BaseModel):
  '''
    Contains inputs to the solver.
    container_items : List of containers where to put package items.
    package_items : List of all package items to be packed into container(s).
  '''
  container_items: List[ContainerItem] = []
  package_items: List[PackageItem] = []
