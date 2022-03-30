#!/usr/bin/env python3
#Let's make an example of decorators
def dif(func):
    def inner(a,b):
        print("Let's make a ",func.__name__)
        return func(a,b)
    return inner

@dif
def sum(a,b):
    return a+b

print(sum(1,2))
