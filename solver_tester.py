import time
from typing import List
import Examples.examples_generator as eg
from solver import find_solution


def test_solving_accuracy(min_items: int=5, max_items: int=30, num_tests: int=100):
  res = []
  fill_ratios: List[float] = []
  times_sec: List[float] = []

  if num_tests > 100:
    num_tests = 100

  counter = 0
  while len(res) < num_tests and counter <= 1000:
    counter += 1
    input = eg.random_example().solver_input

    if len(input.package_items) >= min_items and len(input.package_items) <= max_items:
      start_time = time.time()
      sol = find_solution(input=input)
      sec = time.time() - start_time
      times_sec.append(sec)
      fill_ratios.append(sol.total_fill_ratio)
      txt = f"{len(fill_ratios)}: num_items={sol.num_items_total}, fill_ratio={sol.total_fill_ratio}, fitted={sol.num_items_fitted}/{sol.num_items_total}, unfitted={sol.num_items_unfitted}, time={round(sec, 2)} sec"
      print(txt)
      res.append(txt)

  num_tests = len(fill_ratios)
  total_time = sum(times_sec)
  txt = f"num_tests={num_tests}, avg_fill_ratio={round(sum(fill_ratios) / num_tests, 4)}, avg_time={round(total_time / num_tests, 2)} sec, total_time={round(total_time, 2)}"
  print(txt)
  res.append(txt)

  return res


