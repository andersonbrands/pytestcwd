import sys
from typing import List


def main(params: List[str] = None):
    pass


def console_script_entry():
    main(sys.argv[1:])
    pass


if __name__ == '__main__':
    console_script_entry()
