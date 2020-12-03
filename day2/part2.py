#!/usr/bin/env python

import fileinput
from typing import List


def get_input() -> List[str]:
    return [line.strip() for line in fileinput.input()]


def main():
    password_list = get_input()
    valid_passwords = 0

    for entry in password_list:
        limits, search, password = entry.split()
        low, high = [int(limit) - 1 for limit in limits.split('-')]
        search = search[0]

        correct = False
        password_length = len(password)
        if high > password_length:
            # index out of range
            continue

        if password[low] == search:
            correct = not correct
        if password[high] == search:
            correct = not correct

        if correct:
            valid_passwords += 1

    print(valid_passwords)


if __name__ == '__main__':
    main()
