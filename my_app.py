#! /usr/bin/env python3
# author: Mark W. Naylor
# file:  my_app.py
# date:  2018-Jan-28

import sys

import message

def main():
    if len(sys.argv) > 1:
        message.hello(sys.argv[1])
    else:
        message.hello()

if __name__ == '__main__':
    main()
