#!/usr/bin/env python

import fileinput


def main():
    group = {}
    yes_questions = 0

    line = '\n'
    for line in fileinput.input():
        # if line is blank, the whole group has been processed
        if line == '\n':
            yes_questions += len(group)
            group = {}
            continue
        for question in line.strip():
            group[question] = True
    # process the last input if no blank line was at the end of input
    if line != '\n':
        yes_questions += len(group)

    print(yes_questions)


if __name__ == '__main__':
    main()
