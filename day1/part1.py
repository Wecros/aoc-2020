#!/usr/bin/env python

import fileinput
from typing import List


def get_input() -> List[int]:
    return [int(line.strip()) for line in fileinput.input()]


def main():
    entries = get_input()
    for entry in entries:
        for another_entry in entries:
            if entry + another_entry == 2020:
                print(entry * another_entry)
                return


if __name__ == '__main__':
    main()
