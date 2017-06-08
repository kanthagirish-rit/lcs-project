"""
file: dynamicprog.py
python version: 3.5
Authors : Kantha Girish, Akshay Karki
description: This file contains bottom up dynamic programming algorithm to compute Longest
Common Sub-sequence of two string sequences
"""

import datagen
import numpy as np
import sys


def dp_lcs(x, y, reconstruct=False):
    """
    :param x: string sequence
    :param y: string sequence
    :param reconstruct: Boolean to indicate whether to reconstruct a string or not. Default
    False
    :return: Length of longest common sub-sequence between x and y

    This function implements dynamic programming algorithm to compute LCS of two strings x and y.
    """
    m, n = len(x), len(y)

    if m == 0 or n == 0:
        return 0
    else:
        l = np.zeros(shape=(m + 1, n + 1), dtype='int64')
        if reconstruct:
            b = np.array([[""] * (n + 1)] * (m + 1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    l[i, j] = l[i-1, j-1] + 1
                    if reconstruct:
                        b[i, j] = "d"
                elif l[i-1, j] >= l[i, j-1]:
                    l[i, j] = l[i-1, j]
                    if reconstruct:
                        b[i, j] = "u"
                else:
                    l[i, j] = l[i, j-1]
                    if reconstruct:
                        b[i, j] = "l"
        if reconstruct:
            i, j = m, n
            lcs = ""
            while i > 0 and j > 0:
                if b[i, j] == "d":
                    lcs = x[i-1] + lcs
                    i -= 1
                    j -= 1
                elif b[i, j] == "u":
                    i -= 1
                else:
                    j -= 1
            return lcs
        else:
            return l[m][n]


def test(x, y, reconstruct):
    """
    :param x: string sequence
    :param y: string sequence
    :return: Size of LCS

    This function is a simple test function which runs when this file is run.
    """
    return dp_lcs(x, y, reconstruct)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python3 " + __file__ + " acgt/bits 0/1")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("0 - without reconstruction, 1 - with reconstruction")
    else:
        file = sys.argv[1] + ".txt"
        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = False

            if len(sys.argv) == 3:
                reconstruct = int(sys.argv[2]) == 1
            if reconstruct:
                lcs = test(x, y, reconstruct)
                print("LCS length: " + str(len(lcs)))
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
