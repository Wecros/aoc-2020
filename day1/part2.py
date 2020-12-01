#!/usr/bin/env python

import fileinput
from typing import List


def get_input() -> List[int]:
    return [int(line.strip()) for line in fileinput.input()]


def main():
    entries = get_input()
    match = 2020
    for entry1 in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry1 + entry2 + entry3 == match:
                    print(entry1 * entry2 * entry3)
                    return


if __name__ == '__main__':
    main()
