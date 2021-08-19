# -*- coding: utf-8 -*-
"""
정수 N개의 합
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오
Created on Wed Aug 18 23:14:11 2021

@author: taebe
"""

def n_sum(_n):
    t_sum = 0
    for i in _n:
        t_sum += i
    return t_sum
