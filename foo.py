#!/usr/local/bin/python3

def mul2(num):
    return 2*num

def print_times(num):
    for n in range(num):
        print("{} multiplied by 2 is {}".format(n, mul2(n)))


if __name__ == "__main__":
    print_times(10)
