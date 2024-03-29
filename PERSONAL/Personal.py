'''
Created on Jul 31, 2023

@author: abdulbasitolagunju
'''
import time

a = "boy"
print(type(a))



def f1(n):
    start = time.time()
    for i in range(n):
        a = i
    end = time.time()
    return n, end-start

def f2(n):
    start = time.time()
    for i in range(n*n):
        a = i
    end = time.time()
    return n, end-start

def f3(n):
    start = time.time()
    k = 1
    for i in range(n):
        for j in range(k):
            a = j
        k*= 2
    end = time.time()
    return n, end-start



print()
print("Test for F2")
print("F2 %d required %10.7f seconds" %f2(50))
# print("F2 %d required %10.7f seconds" %f2(500))
# print("F2 %d required %10.7f seconds" %f2(5000))
# print("F2 %d required %10.7f seconds" %f2(50000))
# print("F2 %d required %10.7f seconds" %f2(500000))
# print("F2 %d required %10.7f seconds" %f2(5000000))




