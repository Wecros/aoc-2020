#!/usr/bin/env python

import fileinput


def compute_row(line):
    """Compute the row of the seat."""
    low: int = 0
    high: int = 127
    for char in line[:7]:
        diff: int = high - low
        if char == 'F':
            # lower half
            high -= int(diff / 2 + 0.5)

        elif char == 'B':
            # upper half
            low += int(diff / 2 + 0.5)
    return high


def compute_col(line):
    """Compute the column of the seat."""
    low: int = 0
    high: int = 7
    for char in line[7:]:
        diff: int = high - low
        if char == 'L':
            # lower half
            high -= int(diff / 2 + 0.5)
        elif char == 'R':
            # upper half
            low += int(diff / 2 + 0.5)
    return high


def main():
    highest_seatID = 0

    for line in fileinput.input():
        line = line.strip()
        # invalid input if the line isn't 7+3 characters long
        if len(line) != 10:
            continue
        row = compute_row(line)
        col = compute_col(line)
        seatID = row * 8 + col

        if seatID > highest_seatID:
            highest_seatID = seatID

    print(highest_seatID)


if __name__ == '__main__':
    main()
