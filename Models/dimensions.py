from typing import List, Any
from pydantic import BaseModel

class Dimensions(BaseModel):
  width: float = 0.0
  height: float = 0.0
  length: float = 0.0

  def __init__(__pydantic_self__, width: float=0.0, height: float=0.0, length: float=0.0, **data: Any) -> None:
    super().__init__(**data)
    __pydantic_self__.width = width
    __pydantic_self__.height = height
    __pydantic_self__.length = length
