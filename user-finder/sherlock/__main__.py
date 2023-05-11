#! /usr/bin/env python3

"""
Sherlock: Find Usernames Across Social Networks Module

This module contains the main logic to search for usernames at social
networks.
"""


import sys


if __name__ == "__main__":
    minor = sys.version_info[1]

    major = sys.version_info[0]
    python_version = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}.{str(sys.version_info[2])}"

    if major != 3 or minor < 6:
        print("Sherlock requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)

    import sherlock
    sherlock.main()
