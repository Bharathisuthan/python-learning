#!/usr/bin/env python
# coding: utf-8

y = 6


def add(a, b):
    result = a + b
    return result


def subt(a, b):
    result = a - b
    return result


def multi(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result


def remainder(a, b):
    result = a % b
    return result


def add10(a, b):
    result1 = a + 10
    result2 = b + 10
    return (result1, result2)


def prime(n):
    # Prime Numbers are always greater than 1
    if (n > 1):
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is not a prime number.")
                break
        else:
            print(n, "is a prime number.")
    # If the entered number is less than or equal to 1
    # then it is not prime number
    else:
        print(n, "is not a prime number")


def checkAnagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")
