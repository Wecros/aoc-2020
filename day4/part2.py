#!/usr/bin/env python

import fileinput
import re


def validate_data(field: str, passport: dict) -> bool:
    # field must be present
    if field not in passport:
        return False
    value = passport[field]
    year = 0

    # four digit-year check
    if field in ('byr', 'iyr', 'eyr'):
        year = int(value)
        if len(value) != 4 and not value.isnumeric():
            return False

    if field == 'byr':
        return year >= 1920 and year <= 2002
    elif field == 'iyr':
        return year >= 2010 and year <= 2020
    elif field == 'eyr':
        return year >= 2020 and year <= 2030
    elif field == 'hgt':
        matched = re.match('([0-9]*)(cm|in)', value)
        if not matched:
            return False

        height: int = int(matched.group(1))
        unit: str = matched.group(2)
        if unit == 'cm':
            return height >= 150 and height <= 193
        return height >= 59 and height <= 76
    elif field == 'hcl':
        matched = re.match('#[0-9a-f]{6}', value)
        if not matched:
            return False
        return True
    elif field == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    elif field == 'pid':
        return len(value) == 9 and value.isnumeric()
    else:
        return False


def main():
    valid_passports = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport = {}

    for line in fileinput.input():
        # if line is blank, the whole password has been processed
        if line == '\n':
            if all([validate_data(req, passport) for req in required_fields]):
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
