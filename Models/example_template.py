from os import name
from typing import Any
from pydantic import BaseModel

from Models.solver_input import SolverInput
from Models.solver_output import SolverOutput

class ExampleTemplate(BaseModel):
  '''
    Example template model.
  '''

  name: str = ""
  solver_input: SolverInput = SolverInput()
  solver_output: SolverOutput = SolverOutput()

  def __init__(
          __pydantic_self__,
          name: str="",
          solver_input: SolverInput=SolverInput(),
          solver_output: SolverOutput=SolverOutput(),
          **data: Any) -> None:

      super().__init__(**data)
      __pydantic_self__.name = name
      __pydantic_self__.solver_input = solver_input
      __pydantic_self__.solver_output = solver_output
