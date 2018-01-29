#! /usr/bin/env python3
# author: Mark W. Naylor
# file:  my_app.py
# date:  2018-Jan-28

import sys

import hello

def main():
    if len(sys.argv) > 1:
        hello.hello(sys.argv[1])
    else:
        hello.hello()

if __name__ == '__main__':
    main()
