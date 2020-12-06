#!/usr/bin/env python

import fileinput
import string


def main():
    possible_answers = dict.fromkeys(string.ascii_lowercase, True)
    person = {}
    yes_group_questions = 0

    line = '\n'
    for line in fileinput.input():
        # if line is blank, the whole group has been processed
        if line == '\n':
            yes_group_questions += len(possible_answers)
            possible_answers = dict.fromkeys(string.ascii_lowercase, True)
            continue
        # process the questions for one person
        for question in line.strip():
            person[question] = True

        # remove the possible answers based on the no answers of a person
        possible_answers = {
            k: v for k, v in possible_answers.items() if k in person
        }
        person = {}  # reset the person's answers

    # process the last input if no blank line was at the end of input
    if line != '\n':
        yes_group_questions += len(possible_answers)

    print(yes_group_questions)


if __name__ == '__main__':
    main()
