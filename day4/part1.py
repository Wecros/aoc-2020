#!/usr/bin/env python

import fileinput


def main():
    valid_passports = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport = {}

    for line in fileinput.input():
        # if line is blank, the whole password has been processed
        if line == '\n':
            if all([req in passport for req in required_fields]):
                valid_passports += 1
            passport = {}
            continue

        fields = line.split()
        for field in fields:
            key, value = field.split(':')
            passport[key] = value

    print(valid_passports)


if __name__ == '__main__':
    main()
