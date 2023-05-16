import numpy as np
import random as rnd
from copy import deepcopy
from typing import List, Tuple

from .constants import RotationType, Axis
from .auxiliary_methods import intersect
from ..utils import permute_slice, reverse_slice, swap_idx
from ..utils import point_clouds_add, point_clouds_intersect

rnd.seed(10101)

START_POSITION = [0, 0, 0]

class Item:
    def __init__(self, name, width, height, depth, weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
        self.rotation_type = 0
        self.position = START_POSITION

    def string(self):
        return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.weight,
            self.position, self.rotation_type, self.get_volume()
        )

    def get_volume(self) -> float:
        return self.width * self.height * self.depth

    def get_bottom_area(self) -> float:
        return self.width * self.depth

    def get_side_area(self) -> float:
        return self.height * self.depth

    def get_front_area(self) -> float:
        return self.width * self.height

    def get_total_area(self) -> float:
        return 2 * (self.get_bottom_area() + self.get_front_area() + self.get_side_area())

    def get_dimension(self):
        if self.rotation_type == RotationType.RT_WHD:
            dimension = [self.width, self.height, self.depth]
        elif self.rotation_type == RotationType.RT_HWD:
            dimension = [self.height, self.width, self.depth]
        elif self.rotation_type == RotationType.RT_HDW:
            dimension = [self.height, self.depth, self.width]
        elif self.rotation_type == RotationType.RT_DHW:
            dimension = [self.depth, self.height, self.width]
        elif self.rotation_type == RotationType.RT_DWH:
            dimension = [self.depth, self.width, self.height]
        elif self.rotation_type == RotationType.RT_WDH:
            dimension = [self.width, self.depth, self.height]
        else:
            dimension = []

        return dimension

class Bin:
    def __init__(self, name, width, height, depth, max_weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight
        self.items: List[Item] = []
        self.unfitted_items = []
        #self.point_cloud: np.ndarray = None

    def string(self):
        return "%s(%sx%sx%s, max_weight:%s) vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.max_weight,
            self.get_volume()
        )

    def get_volume(self):
        return self.width * self.height * self.depth

    def get_total_weight(self):
        return sum([item.weight for item in self.items])

    def put_item(self, item: Item, pivot: Tuple[int]) -> bool:
        fit = False
        valid_item_position = item.position
        item.position = pivot
        use_point_cloud = False # point_cloud is not None
        #new_point_cloud: np.ndarray=None

        for i in range(0, len(RotationType.ALL)):
            item.rotation_type = i
            dimension = item.get_dimension()
            # x0,y0,z0 = pivot
            # size_x,size_y,size_z = dimension
            if (
                self.width < pivot[0] + dimension[0] or
                self.height < pivot[1] + dimension[1] or
                self.depth < pivot[2] + dimension[2]
            ):
                continue

            fit = True

            # if use_point_cloud:
            #     fit = not point_clouds_intersect(
            #                     points = point_cloud,
            #                     x0 = x0,
            #                     y0 = y0,
            #                     z0 = z0,
            #                     size_x = size_x,
            #                     size_y = size_y,
            #                     size_z = size_z
            #                 )

            has_support_below = pivot[1] == 0

            for current_item_in_bin in self.items:
                if not use_point_cloud:
                    if intersect(current_item_in_bin, item):
                        fit = False
                        break
                
                if not has_support_below:
                    # test against back_top_left corner and front_top_right of an existing item
                    # new position above must be within these points.
                    back_top_left = deepcopy(current_item_in_bin.position)
                    back_top_left[1] += current_item_in_bin.height

                    front_top_right = deepcopy(current_item_in_bin.position)
                    front_top_right[0] += current_item_in_bin.width
                    front_top_right[1] += current_item_in_bin.height
                    front_top_right[2] += current_item_in_bin.depth

                    new_back_bottom_left = deepcopy(pivot)
                    new_front_bottom_right = (pivot[0] + item.width, pivot[1], pivot[2] + item.depth)

                    # check support along length (z-axis) and width (x-axis)
                    has_support_below = round(new_back_bottom_left[1], 2) == round(back_top_left[1], 2) \
                        and not new_back_bottom_left[0] >= back_top_left[0] + current_item_in_bin.width \
                        and not new_back_bottom_left[0] + item.width <= back_top_left[0] \
                        and not new_front_bottom_right[2] <= front_top_right[2] - current_item_in_bin.depth \
                        and not new_front_bottom_right[2] - item.depth >= front_top_right[2]
 
                    if has_support_below: # check if enough support area
                        min_support = 0.8
                        has_support_below = abs(new_back_bottom_left[2] - front_top_right[2]) / item.depth >= min_support
                                         #and abs(new_back_bottom_left[0] - front_top_right[0]) / item.width >= min_support
 
            #has_support_below = True
            if not has_support_below:
                fit = False

            if fit:
                if self.get_total_weight() + item.weight > self.max_weight:
                    fit = False
                    return fit

                self.items.append(item)

            if not fit:
                item.position = valid_item_position

            # if use_point_cloud and fit:
            #     new_point_cloud = point_clouds_add(
            #             original_points = point_cloud,
            #             x0 = x0,
            #             y0 = y0,
            #             z0 = z0,
            #             size_x = size_x,
            #             size_y = size_y,
            #             size_z = size_z
            #         )

            return fit

        if not fit:
            item.position = valid_item_position

        return fit

    def get_fill_ratio(self) -> float:
        bin_volume = self.get_volume()
        filled_volume = sum([i.get_volume() for i in self.items])
        return 0 if bin_volume < 0.00001 else filled_volume / bin_volume

class Packer:
    def __init__(self, bin: Bin, items: List[Item]):
        self.bins: List[Bin] = [bin]
        self.items: List[Item] = items
        self.unfitted_items: List[Item] = []

    def get_bin(self) -> Bin:
        return self.bins[0]

    def add_bin(self, bin):
        self.bins.append(bin)

    def add_item(self, item):
        self.items.append(item)

    def pack_to_bin(self, bin: Bin, item: Item) -> bool:
        fitted = False

        if not bin.items:
            response = bin.put_item(item, START_POSITION)

            if not response:
                bin.unfitted_items.append(item)

            return response

        ###############################################################
        # by axis, then by items (original)
        ###############################################################
        # for axis in range(0, 3):
        #     items_in_bin = bin.items

        #     for ib in items_in_bin:
        #         pivot = [0, 0, 0]
        #         w, h, d = ib.get_dimension()
        #         if axis == Axis.WIDTH:
        #             pivot = [
        #                 ib.position[0] + w,
        #                 ib.position[1],
        #                 ib.position[2]
        #             ]
        #         elif axis == Axis.HEIGHT:
        #             pivot = [
        #                 ib.position[0],
        #                 ib.position[1] + h,
        #                 ib.position[2]
        #             ]
        #         elif axis == Axis.DEPTH:
        #             pivot = [
        #                 ib.position[0],
        #                 ib.position[1],
        #                 ib.position[2] + d
        #             ]

        #         if bin.put_item(item, pivot):
        #             fitted = True
        #             break
        #     if fitted:
        #         break

        ###############################################################
        # by items, then by axis
        ###############################################################

        items_in_bin = bin.items
        for ib in items_in_bin:
            items_in_bin = bin.items

            for axis in range(0, 3):
                pivot = [0, 0, 0]
                w, h, d = ib.get_dimension()
                if axis == Axis.WIDTH:
                    pivot = [
                        ib.position[0] + w,
                        ib.position[1],
                        ib.position[2]
                    ]
                elif axis == Axis.HEIGHT:
                    pivot = [
                        ib.position[0],
                        ib.position[1] + h,
                        ib.position[2]
                    ]
                elif axis == Axis.DEPTH:
                    pivot = [
                        ib.position[0],
                        ib.position[1],
                        ib.position[2] + d
                    ]

                can_put_in_bin = bin.put_item(item, pivot)
                if can_put_in_bin:
                    fitted = True
                    break

            if fitted:
                break

        ###############################################################

        if not fitted:
            bin.unfitted_items.append(item)

        return fitted

    def pack(
            self,
            sort: bool = True,
            bigger_first: bool = True,
            pack_unfitted_again: bool = False
        ):

        distribute_items = False

        if sort:
            self.bins.sort(key=lambda bin: bin.get_volume(), reverse=bigger_first)

            self.items.sort(key=lambda item: item.get_volume(), reverse=bigger_first)
            #self.items.sort(key=lambda item: item.get_bottom_area(), reverse=bigger_first)
            #self.items.sort(key=lambda item: item.get_side_area(), reverse=bigger_first)
            #self.items.sort(key=lambda item: item.get_front_area(), reverse=bigger_first)
            #self.items.sort(key=lambda item: item.get_total_area(), reverse=bigger_first)
            #rnd.shuffle(self.items)

        for bin in self.bins:
            for item in self.items:
                self.pack_to_bin(bin, item)

            if distribute_items:
                for item in bin.items:
                    self.items.remove(item)

        if pack_unfitted_again:
            self.pack_unfitted(sort=False, bigger_first=True)

        self.unfitted_items = self.bins[0].unfitted_items


    def pack_unfitted(
            self,
            sort = False,
            bigger_first = True,
        ):

        for bin in self.bins:
            if len(bin.unfitted_items) > 0:
                #for i in range(3): # just in case make some re-runs
                if sort:
                    bin.unfitted_items.sort(key=lambda item: item.get_volume(), reverse=bigger_first)

                unfitted_items = deepcopy(bin.unfitted_items)
                bin.unfitted_items = []

                for item in unfitted_items:
                    fitted = self.pack_to_bin(bin, item)
                    if fitted:
                        print(f"successfully refitted from unfitted list of lenght={len(unfitted_items)}")
                        unfitted_items.remove(item)
                
                bin.unfitted_items = unfitted_items

    def get_average_fill_ratio(self) -> float:
        num_bins = len(self.bins)
        return 0 if num_bins < 1 else sum([b.get_fill_ratio() for b in self.bins]) / num_bins

    def get_num_items_fitted(self) -> int:
        return sum([len(b.items) for b in self.bins])

    def get_num_items_not_fitted(self) -> int:
        return sum([len(b.unfitted_items) for b in self.bins])

class IterativePacker:

    def __init__(self,
            num_iterations: int=10,
            num_restarts: int=0,
            pack_unfitted_again: bool=False
        ):

        self.num_iterations: int = num_iterations
        self.num_restarts = num_restarts
        self.pack_unfitted_again = pack_unfitted_again

    def pack(
            self,
            packer: Packer
        ) -> Packer:

        best_packer: Packer = self.pack_once(packer=deepcopy(packer))
        for i in range(self.num_restarts):
            best_fill_ratio = best_packer.get_average_fill_ratio()
            if best_fill_ratio > 0.99:
                break

            new_packer = self.pack_once(packer=deepcopy(packer))

            new_fill_ratio = new_packer.get_average_fill_ratio()
            if new_fill_ratio > best_fill_ratio:
                num_items_text = f"items_fitted={best_packer.get_num_items_fitted()}->{new_packer.get_num_items_fitted()}"
                print(f"found better packer: {i+1}, fill_ratio={round(best_fill_ratio, 4)}->{round(new_fill_ratio, 4)}, {num_items_text}")
                best_packer = deepcopy(new_packer)

        return best_packer

    def pack_once(
            self,
            packer: Packer
        ) -> Packer:
        
        num_items = len(packer.items)

        #point_cloud: np.ndarray = None

        # if packer.bins[0].get_volume() < 1000000000:
        #     x,y,z = int(packer.bins[0].width),int(packer.bins[0].height),int(packer.bins[0].depth)
        #     point_cloud = np.full(shape=(x,y,z), fill_value=False, dtype=bool)

        # Initial packing
        packer.pack(
                sort=True,
                bigger_first=True,
                pack_unfitted_again=self.pack_unfitted_again
            )

        packer_before: Packer = deepcopy(packer)
        packer_new: Packer = deepcopy(packer)

        fill_ratio_before = packer_before.bins[0].get_fill_ratio()
        fill_ratio_new = packer_new.bins[0].get_fill_ratio()

        for i in range(self.num_iterations):
            if fill_ratio_new > 0.99:
                return packer_new
            else:
                new_is_better = False
                if fill_ratio_new > fill_ratio_before:
                    new_is_better = True
                    packer_before = deepcopy(packer_new)
                    fill_ratio_before = packer_before.bins[0].get_fill_ratio()
                else:
                    packer_new = deepcopy(packer_before)
                    fill_ratio_new = packer_new.bins[0].get_fill_ratio()

                # reset packer, reorder items and pack again
                all_items = deepcopy(packer_new.bins[0].items + packer_new.bins[0].unfitted_items)
                packer_new.bins[0].items = []
                packer_new.bins[0].unfitted_items = []

                rnd1 = rnd.randint(0, num_items - 1)
                rnd2 = rnd.randint(0, num_items - 1)
                start_idx = min(rnd1, rnd2)
                end_idx = max(rnd1, rnd2)
                if end_idx - start_idx < 2:
                    end_idx = start_idx + 2

                action = ""
                random_value = rnd.random()
                if random_value < -0.15:
                    action = "permute"
                    packer_new.items = permute_slice(all_items, start_idx=start_idx, end_idx=start_idx+3)
                    #packer_new.items = permute_slice(all_items, start_idx=start_idx, end_idx=start_idx)
                elif random_value < -0.2:
                    action = "reverse"
                    #packer_new.items = reverse_slice(all_items, start_idx=start_idx, end_idx=end_idx)
                    packer_new.items = reverse_slice(all_items, start_idx=start_idx, end_idx=start_idx+4)
                else:
                    action = "swap"
                    packer_new.items = swap_idx(all_items, idx1=start_idx, idx2=end_idx)

                    # swap 2 times sometimes
                    if random_value > 10.5:
                        action = "swap2"
                        packer_new.items = swap_idx(all_items, idx1=rnd.randint(0, num_items - 1), idx2=rnd.randint(0, num_items - 1))

                    # swap 3 times sometimes
                    if random_value > 10.9:
                        action = "swap3"
                        packer_new.items = swap_idx(all_items, idx1=rnd.randint(0, num_items - 1), idx2=rnd.randint(0, num_items - 1))

                packer_new.pack(
                        sort=False,
                        #pack_unfitted_again=self.pack_unfitted_again
                    )
                
                fill_ratio_new = packer_new.bins[0].get_fill_ratio()

                #if new_is_better or i % 100 == 0 or i == self.num_iterations - 1:
                #if new_is_better:
                #    print(f"{i}: new_is_better={new_is_better}, action={action},  fill_ratio_before={int(fill_ratio_before*100)}%, fill_ratio_new={int(fill_ratio_new*100)}%, start_idx={start_idx}, end_idx={end_idx}")

        if fill_ratio_new > fill_ratio_before:
            return packer_new
        else:
            return packer_before




