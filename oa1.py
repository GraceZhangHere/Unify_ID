#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import numpy as np
from pylab import imshow, show, get_cmap
from numpy import random

def get_random():
    """
    Input requirements for generating random numbers
    :return: an array of rundum numbers
    """
    str1 = input("How many random numbers do you want to generate? Should be less than 10,000")
    num1 = int(str1)

    str2 = input('Each number should have a value bigger or equal to:')
    num2 = int(str2)

    str3 = input('Each number should have a value smaller or equal to:')
    num3 = int(str3)

    params = {
        'num': num1,
        'min': num2,
        'max': num3,
        'col': 1,
        'format': 'plain',
        'rnd': 'new',
        'base':10
    }
    r=requests.get('https://www.random.org/integers/?', params=params)
    raw_arr = r.text.strip().split('\n')
    int_arr = list(map(lambda x: int(x), raw_arr))
    print(int_arr)

def get_random2():
    """
    Input requirements for generating random numbers
    :return: an array of rundum numbers
    """
    params = {
        'num': 128,
        'min': 1,
        'max': 256,
        'col': 1,
        'format': 'plain',
        'rnd': 'new',
        'base':10
    }
    r=requests.get('https://www.random.org/integers/?', params=params)
    raw_arr = r.text.strip().split('\n')
    int_arr = list(map(lambda x: int(x), raw_arr))
    return int_arr

# this is to demonstrate how to generate a rgb bitmap from ramdom numbers
Z = random.random((128, 128))   # Test data
imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()

array_128 = get_random2()







