"""Advent of Code <year> Day <day>
"""


import os
import utility


logger = utility.get_logger(__name__)


def main():
    input_file = utility.input_path(__file__)
    with open(input_file, 'r') as file:
        report = file.readlines()
    print(*report)


if __name__ == '__main__':
    utility.monitor_execution(main)
