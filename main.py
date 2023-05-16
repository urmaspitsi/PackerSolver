from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import Examples.examples_generator as eg
from Models.example_template import ExampleTemplate
from Models.solver_input import SolverInput
from Models.solver_output import SolverOutput
from solver import find_solution
from solver_tester import test_solving_accuracy

app = FastAPI(
  title="PackerSolver",
  description="Packer solver web api.",
  version="0.0.1",
  
  )

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://packer.ga",
    "https://packer.ga",
  ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
  )


@app.get("/")
def index():
  return {
            "Hello": "Welcome to the packer world!",
            "version" : app.version,
            "title" : app.title,
            "description" : app.description,
            "docs_url" : app.docs_url,
            "redoc_url" : app.redoc_url,
            "openapi_url" : app.openapi_url,
          }

@app.post("/solve/", response_model=SolverOutput)
async def solve(input: SolverInput, algorithm: str="") -> SolverOutput:
  res = find_solution(input=input, algorithm=algorithm)
  return res

@app.get("/examples/{id}", response_model=ExampleTemplate)
def show_example(id: int) -> ExampleTemplate:
  return eg.example_by_id(id=id)

@app.get("/random_examples", response_model=ExampleTemplate)
def show_random_example() -> ExampleTemplate:
  return eg.random_example()

@app.get("/solve/tester", response_model=List[str])
def solver_tester(min_items: int=10, max_items: int=20, num_tests: int=20, code: str="") -> List[str]:
  if code != "kavaltest":
    return ["Unauthorized: you need correct code to run the tests."]
  else:
    return test_solving_accuracy(min_items=min_items, max_items=max_items, num_tests=num_tests)
