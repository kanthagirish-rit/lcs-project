"""
file: memoization.py
python version: 3.5
Authors : Kantha Girish, Akshay Karki
description: This file contains Memoized recursive algorithm to compute LCS of two string
sequences
"""

import sys
import numpy as np

num_recursive_calls = 0


def memoization(x, y):
    """
    :param x: string sequence
    :param y: string sequence
    :return: Length of longest common sub-sequence between x and y

    This function implements memoized algorithm to compute LCS of two strings x and y.
    """
    m = len(x)
    n = len(y)
    c = np.ones(shape=(m, n), dtype='int64')*-1
    return memoized_LCS(x, y, c)


def memoized_LCS(x, y, c):
    """
    :param x: string sequence
    :param y: string sequence
    :param c: a 2D numpy array of size (len(x), len(y)) initialized to -1.
    :return: recursive call to self, final return would be the length of Longest common
    sub-sequence of two strings.
    """
    global num_recursive_calls
    num_recursive_calls += 1
    if len(x) == 0 or len(y) == 0:
        return 0
    i = len(x) - 1
    j = len(y) - 1
    if c[i, j] > -1:
        return c[i, j]
    else:
        if x[-1] == y[-1]:
            q = 1 + memoized_LCS(x[:-1], y[:-1], c)
        else:
            q = max(memoized_LCS(x, y[:-1], c), memoized_LCS(x[:-1], y, c))
        c[i, j] = q
        return q


def test(x, y):
    """
    :param x: string pattern
    :param y: string pattern
    :return: Size of Longest common sub-sequence of x and y

    This function is a simple test function which runs when this file is run.
    """
    return memoization(x, y)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 " + __file__ + " acgt/bits")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            print("LCS length: " + str(test(x, y)))
            print("Number of recursive calls: " + str(num_recursive_calls))
