#! /usr/bin/env python3
# author: Mark W. Naylor
# file:  hello.py
# date:  2018-Jan-28

def hello(name="world"):
    print("Hello, {0}.".format(name))

def main():
    hello()
    hello("David")

if __name__ == '__main__':
    main()
