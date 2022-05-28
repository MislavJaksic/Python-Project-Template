"""
    poetry-template.py
    ------------------

    Runs the project.

    :copyright: 2019 MislavJaksic
    :license: MIT License
"""
import argparse
import sys
from typing import Dict, Any

from loguru import logger

from poetry_template.package_one import module_one

log_message = "who={username}, what={object}/{status}, where={system}/{application}/{component}/{source}, when={timestamp}/{timezone}, why={reason}, how={action}"


def main() -> None:
    """main() will be run if you run this script directly"""
    args = get_cli_arguments()

    print("Command line interface arguments:{}".format(args))
    x = args["first"]
    y = args["second"]

    logger.info(
        log_message,
        username="1",
        object="2",
        status="3",
        system="4",
        application="5",
        component="6",
        source="7",
        timestamp="8",
        timezone="9",
        reason="10",
        action="11",
    )

    print(module_one.add(x, y))
    print(module_one.multiply(x, y))


def get_cli_arguments() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="Welcome to the command line interface!", epilog="Thank you for using the program!")

    parser.add_argument("-x", "--first", type=int, required=True, help="First number")
    parser.add_argument("-y", "--second", type=int, required=True, help="Second number")
    parser.add_argument("-list", "--multiple", action="append", help="Can be specified many times")
    parser.add_argument("-tuple", "--triple", nargs=3, metavar=("password", "username", "secret"), help="(password, username, secret) tuple")
    parser.add_argument("-move", "--move", choices=["rock", "paper", "scissors"], help="Can only input a choice")

    return vars(parser.parse_args())


def run() -> None:
    """Entry point for the runnable script."""
    sys.exit(main())


if __name__ == "__main__":
    """main calls run()."""
    run()
