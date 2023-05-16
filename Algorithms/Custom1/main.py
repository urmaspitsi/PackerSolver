import random as rnd
from copy import deepcopy
from typing import List

from .constants import RotationType, Axis
from .auxiliary_methods import intersect, set_to_decimal
from ..utils import permute_slice, reverse_slice, swap_idx

rnd.seed(10101)

DEFAULT_NUMBER_OF_DECIMALS = 3
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
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def format_numbers(self, number_of_decimals):
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.depth = set_to_decimal(self.depth, number_of_decimals)
        self.weight = set_to_decimal(self.weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.weight,
            self.position, self.rotation_type, self.get_volume()
        )

    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.depth, self.number_of_decimals
        )

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
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def format_numbers(self, number_of_decimals):
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.depth = set_to_decimal(self.depth, number_of_decimals)
        self.max_weight = set_to_decimal(self.max_weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        return "%s(%sx%sx%s, max_weight:%s) vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.max_weight,
            self.get_volume()
        )

    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.depth, self.number_of_decimals
        )

    def get_total_weight(self):
        total_weight = 0

        for item in self.items:
            total_weight += item.weight

        return set_to_decimal(total_weight, self.number_of_decimals)

    def put_item(self, item, pivot):
        fit = False
        valid_item_position = item.position
        item.position = pivot

        for i in range(0, len(RotationType.ALL)):
            item.rotation_type = i
            dimension = item.get_dimension()
            if (
                self.width < pivot[0] + dimension[0] or
                self.height < pivot[1] + dimension[1] or
                self.depth < pivot[2] + dimension[2]
            ):
                continue

            fit = True

            for current_item_in_bin in self.items:
                if intersect(current_item_in_bin, item):
                    fit = False
                    break

            if fit:
                if self.get_total_weight() + item.weight > self.max_weight:
                    fit = False
                    return fit

                self.items.append(item)

            if not fit:
                item.position = valid_item_position

            return fit

        if not fit:
            item.position = valid_item_position

        return fit

    def get_fill_ratio(self) -> float:
        bin_volume = self.width * self.height * self.depth
        filled_volume = sum([i.width * i.height * i.depth for i in self.items])
        return 0 if bin_volume < 0.00001 else filled_volume / bin_volume

class Packer:
    def __init__(self):
        self.bins: List[Bin] = []
        self.items: List[Item] = []
        self.unfit_items: List[Item] = []
        self.total_items: int = 0

    def add_bin(self, bin):
        return self.bins.append(bin)

    def add_item(self, item):
        self.total_items = len(self.items) + 1

        return self.items.append(item)

    def pack_to_bin(self, bin, item):
        fitted = False

        if not bin.items:
            response = bin.put_item(item, START_POSITION)

            if not response:
                bin.unfitted_items.append(item)

            return

        for axis in range(0, 3):
            items_in_bin = bin.items

            for ib in items_in_bin:
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

                if bin.put_item(item, pivot):
                    fitted = True
                    break
            if fitted:
                break

        if not fitted:
            bin.unfitted_items.append(item)

    def pack(
            self,
            sort = True,
            bigger_first = True,
        ):

        distribute_items = False

        for bin in self.bins:
            bin.format_numbers(DEFAULT_NUMBER_OF_DECIMALS)

        for item in self.items:
            item.format_numbers(DEFAULT_NUMBER_OF_DECIMALS)

        if sort:
            self.bins.sort(key=lambda bin: bin.get_volume(), reverse=bigger_first)

            self.items.sort(key=lambda item: item.get_volume(), reverse=bigger_first)

        for bin in self.bins:
            for item in self.items:
                self.pack_to_bin(bin, item)

            if distribute_items:
                for item in bin.items:
                    self.items.remove(item)

class IterativePacker:

    def __init__(self, num_iterations: int = 10):
        self.num_iterations: int = num_iterations

    def pack(
            self,
            packer: Packer
        ) -> Packer:
        
        num_items = len(packer.items)

        # Initial packing
        packer.pack(sort=True, bigger_first=True)
        #packer.pack(sort=False)

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

                packer_new.pack(sort=False)
                
                fill_ratio_new = packer_new.bins[0].get_fill_ratio()

                #if new_is_better or i % 100 == 0 or i == self.num_iterations - 1:
                #if new_is_better:
                #    print(f"{i}: new_is_better={new_is_better}, action={action},  fill_ratio_before={int(fill_ratio_before*100)}%, fill_ratio_new={int(fill_ratio_new*100)}%, start_idx={start_idx}, end_idx={end_idx}")

        if fill_ratio_new > fill_ratio_before:
            return packer_new
        else:
            return packer_before




