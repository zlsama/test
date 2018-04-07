#!/usr/bin/env python
# encoding: utf-8
# author: zhangli  time:2018/4/7

def is_prime(n):
    if n<=2:
        return True
    i=2
    while i**i<n:
        if n%i==0:
            return False
        i+=1
    return True


