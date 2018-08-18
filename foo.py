#!/usr/local/bin/python3

def mul2(num):
    return 2*num

if __name__ == "__main__":
    for num in range(10):
        print(f"{num} multiplied by 2 is {mul2(num)}")
