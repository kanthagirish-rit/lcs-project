"""
file: hlcs.py
python version: 3.5
Authors : Kantha Girish, Akshay Karki
description: This file contains Hirschberg's linear space quadratic time dynamic programming
algorithm to compute Longest Common Sub-sequence of two string sequences
"""

import numpy as np
import sys


def alg_b(m, n, A, B):
    """
    :param m: length of string A
    :param n: length of string B
    :param A: String sequence
    :param B: String sequence
    :return: Returns the final row of DP table computed using Hirschberg's algorithm B
    """
    K = np.zeros(shape=(2, n+1), dtype='int64')
    for i in range(m):
        K[0, :] = K[1, :]
        for j in range(n):
            if A[i] == B[j]:
                K[1, j+1] = K[0, j] + 1
            else:
                K[1, j+1] = max(K[1, j], K[0, j+1])
    return K[1, :]


def alg_c(m, n, A, B, reconstruct=False):
    """
    :param m: length of string A
    :param n: length of string B
    :param A: String sequence
    :param B: String sequence
    :param reconstruct: A boolean indicating whether to reconstruct the string or not.
    Default False
    :return: Reconstructed Longest common subsequence
    """
    if n == 0:
        return ""
    elif m == 1:
        if A in B:
            return A
        else:
            return ""
    else:
        i = m // 2
        L1 = alg_b(i, n, A[:i], B)
        L2 = alg_b(m-i, n, A[i:][::-1], B[::-1])
        if reconstruct:
            k = np.argmax(L1 + L2[::-1])
            return alg_c(i, k, A[:i], B[:k], reconstruct) \
                + alg_c(m-i, n-k, A[i:], B[k:], reconstruct)
        else:
            return int(np.amax(L1 + L2[::-1]))


def test(A, B, reconstruct):
    """
    :param x: string sequence
    :param y: string sequence
    :return: Size of LCS

    This function is a simple test function which runs when this file is run.
    """
    return alg_c(len(A), len(B), A, B, reconstruct)

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("Usage: python3 " + __file__ + " acgt/bits 0/1")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("0- don't reconstruct LCS, 1-reconstruct LCS")
    else:
        file = sys.argv[1] + ".txt"

        with open(file, 'r') as f:
            x = f.readline().strip()
            y = f.readline().strip()
            reconstruct = False

            if len(sys.argv) == 3:
                reconstruct = int(sys.argv[2]) == 1
            if reconstruct:
                print("LCS length: " + str(len(test(x, y, reconstruct))))
            else:
                print("LCS length: " + str(test(x, y, reconstruct)))
