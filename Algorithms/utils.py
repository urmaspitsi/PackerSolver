import numpy as np
from copy import deepcopy
from random import shuffle
from typing import List, Tuple

def permute_slice(input: List, start_idx: int, end_idx: int) -> List:
  '''
    Permutes slice of the input list between start_idx and end_idx.
    start_idx, end_idx both included.
  '''
  inp = deepcopy(input)
  middle = list(inp[start_idx:(end_idx + 1)])
  shuffle(middle)

  if start_idx == 0 and end_idx >= len(inp):
    return middle

  elif start_idx == 0:
    end = inp[end_idx:]
    return middle + end

  elif end_idx >= len(inp):
    start = inp[:start_idx]
    return start + middle

  else:
    start = inp[:start_idx]
    end = inp[end_idx:]
    return start + middle + end

def reverse_slice(input: List, start_idx: int, end_idx: int) -> List:
  '''
    Reverses slice of the input list between start_idx and end_idx.
    start_idx, end_idx both included.
  '''

  #middle = deepcopy(input[start_idx:(end_idx + 1)])
  #middle = list(reversed(middle))
  middle = list(reversed(input[start_idx:(end_idx + 1)]))

  res = []
  if start_idx == 0 and end_idx >= len(input):
    res = middle

  elif start_idx == 0:
    end = input[end_idx:]
    res = middle + end

  elif end_idx >= len(input):
    start = input[:start_idx]
    res = start + middle

  else:
    start = input[:start_idx]
    end = input[end_idx:]
    res = start + middle + end

  return deepcopy(res)

def swap_idx(input: List, idx1: int, idx2: int) -> List:
  '''
    Swaps items on positions idx1 and idx2.
  '''

  if idx2 >= len(input) or idx1 == idx2:
    return input
  else:
    res = deepcopy(input)
    res[idx1] = deepcopy(input[idx2])
    res[idx2] = deepcopy(input[idx1])
    return res

def point_clouds_intersect(points: np.ndarray, x0: int, y0: int, z0: int, size_x: int, size_y: int, size_z: int) -> bool:
  return np.sum(points[x0:(x0+size_x), y0:(y0+size_y), z0:(z0+size_z)]) > 0

def point_clouds_add(original_points: np.ndarray, x0: int, y0: int, z0: int, size_x: int, size_y: int, size_z: int) -> np.ndarray:
  x, y, z = original_points.shape
  x1, y1, z1 = x0 + size_x, y0 + size_y, z0 + size_z

  if x < x1 or y < y1 or z < z1:
    return original_points
  else:
    true_values = np.full(shape=(size_x,size_y,size_z), fill_value=True, dtype=bool)
    original_points[x0:x1, y0:y1, z0:z1] = true_values
    return original_points

def intersect_cuboids(dim1: Tuple[int], pos1: Tuple[int], dim2: Tuple[int], pos2: Tuple[int]) -> bool:
  width1, height1, depth1 = dim1
  x1,y1,z1 = pos1

  width2, height2, depth2 = dim2
  x2,y2,z2 = pos2

  if x1 >= x2 + width2:   # first is far right
    return False

  if x1 + width1 <= x2: # first is far left
    return False

  if y1 >= y2 + height2:   # first is far up
    return False

  if y1 + height1 <= y2: # first is far down
    return False

  if z1 >= z2 + depth2:   # first is far front
    return False

  if z1 + depth1 <= z2: # first is far back
    return False

  return True
