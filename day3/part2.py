#!/usr/bin/env python

import fileinput
from typing import List


def get_input() -> List[str]:
    return [line.strip() for line in fileinput.input()]


def traverse_slope(slope, right, down):
    row_len = len(slope[0])
    tree = '#'
    tree_count = 0
    loc = 0  # location number in the row

    going_down = 1
    for row in slope[1:]:
        if going_down < down:
            going_down += 1
            continue
        else:
            going_down = 1

        loc = (loc + right) % row_len

        if row[loc] == tree:
            tree_count += 1

    return tree_count


def main():
    rows = get_input()
    print(traverse_slope(rows, 3, 1))
    result = (traverse_slope(rows, 1, 1) *
              traverse_slope(rows, 3, 1) *
              traverse_slope(rows, 5, 1) *
              traverse_slope(rows, 7, 1) *
              traverse_slope(rows, 1, 2))

    print(result)


if __name__ == '__main__':
    main()
