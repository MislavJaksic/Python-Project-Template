"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

from poetry_template.package_one import module_one


def main(args):
    """main() will be run if you run this script directly
    """
    x = 2
    y = 7

    print(module_one.add(x, y))  # -> 9
    print(module_one.multiply(x, y))  # -> 14


def run():
    """Entry point for the runnable script.
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
