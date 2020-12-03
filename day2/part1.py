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
        low, high = [int(limit) for limit in limits.split('-')]
        search = search[0]

        count = password.count(search)
        if count >= low and count <= high:
            valid_passwords += 1
        else:
            print(limits, search, password)

    print(valid_passwords)


if __name__ == '__main__':
    main()
