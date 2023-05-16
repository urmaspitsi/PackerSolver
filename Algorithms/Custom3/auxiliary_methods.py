
from typing import Tuple

def rect_intersect(dim1: Tuple[int], pos1: Tuple[int], dim2: Tuple[int], pos2: Tuple[int], axis1: int, axis2: int):
    d1 = dim1
    d2 = dim2

    d1_ax1 = d1[axis1]
    d1_ax2 = d1[axis2]

    d2_ax1 = d2[axis1]
    d2_ax2 = d2[axis2]

    cx1 = pos1[axis1] + d1_ax1 / 2
    cy1 = pos1[axis2] + d1_ax2 / 2
    cx2 = pos2[axis1] + d2_ax1 / 2
    cy2 = pos2[axis2] + d2_ax2 / 2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (d1_ax1 + d2_ax1) / 2 and iy < (d1_ax2 + d2_ax2) / 2


def intersect(dim1: Tuple[int], pos1: Tuple[int], dim2: Tuple[int], pos2: Tuple[int]):
    return rect_intersect(dim1=dim1, pos1=pos1, dim2=dim2, pos2=pos2, axis1=0, axis2=1) \
        and rect_intersect(dim1=dim1, pos1=pos1, dim2=dim2, pos2=pos2, axis1=1, axis2=2) \
        and rect_intersect(dim1=dim1, pos1=pos1, dim2=dim2, pos2=pos2, axis1=0, axis2=2)
