#! /usr/bin/env python3
# author: Mark W. Naylor
# file:  hello.py
# date:  2018-Jan-28

def message(msg, name):
    output = "{0}, {1}.".format(msg, name)
    print(output)

def hello(name="world"):
    message("Herro", name)

def goodbye(name="world"):
    message("Goodbye", name)

def main():
    #hello()
    hello("David")
    #message("Out the back", "Jack")
    goodbye("David")

if __name__ == '__main__':
    main()
