# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:08:23 2021

@author: dkhurm
"""

def solution(xs):
    # Your code here
    xs = sorted(xs)[::-1]
    n = len(xs)
    
    if n == 1: 
        return str(xs[0])
    front = 0
    back = n - 1
    product_positives =  -1
    while front < n and xs[front] > 0:
        if product_positives == -1:
            product_positives = 1
        product_positives = product_positives * xs[front]
        front = front + 1
    product_negatives = -1
    while back - 1 >= 0 and xs[back] < 0 and xs[back - 1] < 0:
        if product_negatives == -1:
            product_negatives = 1
        product_pairs_negative = xs[back] * xs[back - 1]
        product_negatives = product_negatives * product_pairs_negative
        back = back - 2
    if product_negatives == -1 and product_positives == -1:
        return str(0)
    if product_negatives == -1:
        return str(product_positives)
    if product_positives == -1:
        return str(product_negatives)
    
    return str(product_positives * product_negatives)
    

solution([-2, -3, 4, -5])

solution([2, 0, 2, 2, 0])

solution([-2, -3, 1, 0, -5])

solution([0,0,0,-1])
