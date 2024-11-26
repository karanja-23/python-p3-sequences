#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])    
    else:
        for i in range(2, length):
            my_list.append(my_list[i-1] + my_list[i-2])
        print(my_list)     

print(print_fibonacci(10))  