"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Nov 9, 2023"
------------------------------------------------------------------------
"""

from threading import Thread
import time

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

# print("Sum is %d required %10.7f seconds" %f1(1000))

def that():
    print()
    print("Test for F1")
    print("F1 %d required %10.7f seconds" %f1(50))
    print("F1 %d required %10.7f seconds" %f1(500))
    print("F1 %d required %10.7f seconds" %f1(5000))
    print("F1 %d required %10.7f seconds" %f1(50000))
    print("F1 %d required %10.7f seconds" %f2(500000))
    print("F1 %d required %10.7f seconds" %f1(5000000))

def work():
    print()
    print("Test for F2")
    print("F2 %d required %10.7f seconds" %f2(50))
    print("F2 %d required %10.7f seconds" %f2(500))
    print("F2 %d required %10.7f seconds" %f2(5000))
    print("F2 %d required %10.7f seconds" %f2(50000))
    print("F2 %d required %10.7f seconds" %f2(500000))
    print("F2 %d required %10.7f seconds" %f2(5000000))


def this():
    print()
    print("Test for F3")
    print("F3 %d required %10.7f seconds" %f3(10))
    print("F3 %d required %10.7f seconds" %f3(1000))
    print("F3 %d required %10.7f seconds" %f3(10000))
    print("F3 %d required %10.7f seconds" %f3(100000))
    print("F3 %d required %10.7f seconds" %f3(1000000))
    print("F3 %d required %10.7f seconds" %f3(10000000))
# Never worked 




# that()
# work()
this()

# t1 = Thread(target= that)
# t1.start()

# t2 = Thread(target= work)
# t2.start()

# t3 = Thread(target= this)
# t3.start()



print("Hello")