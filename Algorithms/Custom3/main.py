import random as rnd
from copy import deepcopy
from typing import List, Tuple

#from .auxiliary_methods import intersect
from ..utils import permute_slice, reverse_slice, swap_idx
from ..utils import intersect_cuboids as intersect

rnd.seed(10101)

START_POSITION = (0, 0, 0)

class Item:
    def __init__(self, name, width, height, depth, weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
        self.position = START_POSITION

        self.volume = width * height * depth
        self.bottom_area = width * depth
        self.side_area = height * depth
        self.front_area = width * height
        self.total_area =  2 * (width * depth + width * height + height * depth)

    def get_dimension(self):
        return (self.width, self.height, self.depth)

class Bin:
    def __init__(self, name, width, height, depth, max_weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight
        self.items: List[Item] = []

        self.volume = width * height * depth
        self.available_volume = width * height * depth
        self.available_weight = max_weight

    def fits_inside(self, item: Item, corner: Tuple[int]) -> bool:
        # 1. Check available volume
        if item.volume > self.available_volume:
            return False

        x0,y0,z0 = corner
        dims: Tuple[int] = item.get_dimension()
        width0, height0, depth0 = dims
        new_front_bottom_right = (x0 + width0, y0, z0 + depth0)

        if self.width < x0 + width0 or self.height < y0 + height0 or self.depth < z0 + depth0:
            return False
        else:
            has_support_below = y0 == 0

            for current_item_in_bin in self.items:
                dim1=current_item_in_bin.get_dimension()
                width1, height1, depth1 = dim1
                pos1=current_item_in_bin.position
                x1,y1,z1 = pos1

                if intersect(dim1=dim1, pos1=pos1, dim2=dims, pos2=corner):
                    return False
                else:
                    if not has_support_below:
                        # test against back_top_left corner and front_top_right of an existing item
                        # new position above must be within these points.
                        back_top_left = (x1, y1 + height1, z1)
                        front_top_right = (x1 + width1, y1 + height1, z1 + depth1)

                        # check support along length (z-axis) and width (x-axis)
                        has_support_below = round(y0, 2) == round(back_top_left[1], 2) \
                            and not x0 >= back_top_left[0] + width1 \
                            and not x0 + width0 <= back_top_left[0] \
                            and not new_front_bottom_right[2] <= front_top_right[2] - depth1 \
                            and not new_front_bottom_right[2] - depth0 >= front_top_right[2]

                        if has_support_below: # check if enough support area
                            min_support = 0.8
                            has_support_below = abs(z0 - front_top_right[2]) / depth0 >= min_support
                                                #and abs(new_back_bottom_left[0] - front_top_right[0]) / item.width >= min_support

            return True if has_support_below else False


    def put_item(self, item: Item, corner: Tuple[int]) -> bool:
        # 1. Check available weight
        if self.available_weight + item.weight > self.max_weight:
            return False

        # 2. Check if fits inside
        fit = self.fits_inside(item=item, corner=corner)
        if fit:
            item.position = (corner[0], corner[1], corner[2])
            self.available_volume -= item.volume
            self.available_weight -= item.weight
            self.items.append(item)

        return fit

    def reset(self) -> None:
        self.items = []
        self.available_volume = self.volume
        self.available_weight = self.max_weight

    def sort_items_by_depth_height_width(self):
        sorted_items = list(sorted(self.items, key= lambda x: (x.position[2], x.position[1], x.position[0])))
        self.items = sorted_items

    def get_fill_ratio(self) -> float:
        return 0 if self.volume < 0.00001 else (self.volume - self.available_volume) / self.volume


class Packer:
    def __init__(self, bin: Bin, items: List[Item]):
        self.bin: Bin = bin
        self.items: List[Item] = items
        self.unfitted_items: List[Item] = []

    def get_bin(self) -> Bin:
        return self.bin

    def pack_to_bin(self, item: Item) -> bool:
        '''
            Find possible possible corner positions.
        '''

        bin = self.bin

        if len(bin.items) < 1: # First item goes to corner (0,0,0).
            return bin.put_item(item, corner=START_POSITION)
        else:
            # Find possible corner points: by item, then by axis
            for ib in bin.items:
                for axis in range(3):
                    x0, y0, z0 = ib.position
                    if axis == 0:
                        x0 += ib.width
                    elif axis == 1:
                        y0 += ib.height
                    elif axis == 2:
                        z0 += ib.depth

                    if bin.put_item(item, corner=(x0, y0, z0)):
                        return True

        return False

    def reset(self, items: List[Item]) -> None:
        self.bin.reset()
        self.items = items
        self.unfitted_items = []


    def pack(
            self,
            sort: bool = True,
            bigger_first: bool = True,
            pack_unfitted_again: bool = False
        ):

        if sort:
            self.items.sort(key=lambda item: item.volume, reverse=bigger_first)
            #self.items.sort(key=lambda item: item.bottom_area, reverse=bigger_first)
            #self.items.sort(key=lambda item: item.side_area, reverse=bigger_first)
            #self.items.sort(key=lambda item: item.front_area, reverse=bigger_first)
            #self.items.sort(key=lambda item: item.total_area, reverse=bigger_first)
            #rnd.shuffle(self.items)

        # reverse because we will start taking items with list.pop()
        # list.pop() takes last element first. This way it is fast access.
        self.items.reverse()

        num_items = len(self.items)
        for _ in range(num_items):
            item = self.items.pop()
            if not self.pack_to_bin(item):
                self.unfitted_items.append(item)


        if pack_unfitted_again:
            self.pack_unfitted(sort=False, bigger_first=True)

    def pack_unfitted(
            self,
            sort = False,
            bigger_first = True,
        ):

        if len(self.unfitted_items) > 0:
            if sort:
                self.unfitted_items.sort(key=lambda item: item.volume, reverse=bigger_first)

            # reverse because we will start taking items with list.pop()
            # list.pop() takes last element first. This way it is fast access.
            self.unfitted_items.reverse()

            num_items = len(self.unfitted_items)
            new_unfitted_items: List[Item] = []
            for _ in range(num_items):
                item = self.unfitted_items.pop()
                if not self.pack_to_bin(item):
                    new_unfitted_items.append(item)
                else:
                    print(f"successfully refitted from unfitted list of lenght={len(self.unfitted_items)+1}")
            
            self.unfitted_items = new_unfitted_items


    def get_fill_ratio(self) -> float:
        return self.bin.get_fill_ratio()

    def get_num_items_fitted(self) -> int:
        return len(self.bin.items)

    def get_num_items_not_fitted(self) -> int:
        return len(self.unfitted_items)

class IterativePacker:

    def __init__(self,
            num_iterations: int=10,
            num_restarts: int=0,
            pack_unfitted_again: bool=False
        ):

        self.num_iterations: int = num_iterations
        self.num_restarts = num_restarts
        self.pack_unfitted_again = pack_unfitted_again

    def pack(self, packer: Packer) -> Packer:

        best_packer: Packer = self.pack_once(packer=deepcopy(packer))
        for i in range(self.num_restarts):
            best_fill_ratio = best_packer.get_fill_ratio()
            if best_fill_ratio > 0.99:
                break

            new_packer = self.pack_once(packer=deepcopy(packer))

            new_fill_ratio = new_packer.get_fill_ratio()
            if new_fill_ratio > best_fill_ratio:
                num_items_text = f"items_fitted={best_packer.get_num_items_fitted()}->{new_packer.get_num_items_fitted()}"
                print(f"found better packer: {i+1}, fill_ratio={round(best_fill_ratio, 4)}->{round(new_fill_ratio, 4)}, {num_items_text}")
                best_packer = deepcopy(new_packer)

        return best_packer

    def pack_once(self, packer: Packer) -> Packer:
        
        num_items = len(packer.items)

        # Initial packing
        packer.pack(
                sort=True,
                bigger_first=True,
                pack_unfitted_again=self.pack_unfitted_again
            )

        packer_before: Packer = deepcopy(packer)
        packer_new: Packer = deepcopy(packer)

        fill_ratio_before = packer_before.get_fill_ratio()
        fill_ratio_new = packer_new.get_fill_ratio()

        for i in range(self.num_iterations):
            if fill_ratio_new > 0.99:
                return packer_new
            else:
                new_is_better = False
                if fill_ratio_new > fill_ratio_before:
                    new_is_better = True
                    packer_before = deepcopy(packer_new)
                    fill_ratio_before = packer_before.get_fill_ratio()
                else:
                    packer_new = deepcopy(packer_before)
                    fill_ratio_new = packer_new.get_fill_ratio()

                # reset packer, reorder items and pack again
                new_items = deepcopy(packer_new.bin.items + packer_new.unfitted_items)

                rnd1 = rnd.randint(0, num_items - 1)
                rnd2 = rnd.randint(0, num_items - 1)
                start_idx = min(rnd1, rnd2)
                end_idx = max(rnd1, rnd2)
                if end_idx - start_idx < 2:
                    end_idx = start_idx + 2

                action = ""
                random_value = rnd.random()
                if random_value < -0.15: # disabled: some weird mutability issue or smth
                    action = "permute"
                    new_items = permute_slice(new_items, start_idx=start_idx, end_idx=start_idx+3)
                    #packer_new.items = permute_slice(all_items, start_idx=start_idx, end_idx=start_idx)
                elif random_value < -0.2: # disabled: some weird mutability issue or smth
                    action = "reverse"
                    #packer_new.items = reverse_slice(all_items, start_idx=start_idx, end_idx=end_idx)
                    new_items = reverse_slice(new_items, start_idx=start_idx, end_idx=start_idx+4)
                else:
                    action = "swap"
                    new_items = swap_idx(new_items, idx1=start_idx, idx2=end_idx)

                    # swap 2 times sometimes
                    if random_value > 0.75:
                        action = "swap2"
                        new_items = swap_idx(new_items, idx1=rnd.randint(0, num_items - 1), idx2=rnd.randint(0, num_items - 1))

                    # swap 3 times sometimes
                    if random_value > 10.9:
                        action = "swap3"
                        new_items = swap_idx(new_items, idx1=rnd.randint(0, num_items - 1), idx2=rnd.randint(0, num_items - 1))

                packer_new.reset(items=new_items)

                packer_new.pack(
                        sort=False,
                        #pack_unfitted_again=self.pack_unfitted_again
                    )
                
                fill_ratio_new = packer_new.get_fill_ratio()

                #if new_is_better or i % 100 == 0 or i == self.num_iterations - 1:
                #if new_is_better:
                #    print(f"{i}: new_is_better={new_is_better}, action={action},  fill_ratio_before={int(fill_ratio_before*100)}%, fill_ratio_new={int(fill_ratio_new*100)}%, start_idx={start_idx}, end_idx={end_idx}")

        if fill_ratio_new > fill_ratio_before:
            return packer_new
        else:
            return packer_before




