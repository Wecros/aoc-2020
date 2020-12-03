#!/usr/bin/env python

import fileinput
from typing import List


def get_input() -> List[str]:
    return [line.strip() for line in fileinput.input()]


def main():
    rows = get_input()
    row_len = len(rows[0])

    tree = '#'
    tree_count = 0
    loc = 0  # location number in the row

    for row in rows[1:]:
        loc = (loc + 3) % row_len

        if row[loc] == tree:
            tree_count += 1

    print(tree_count)


if __name__ == '__main__':
    main()
