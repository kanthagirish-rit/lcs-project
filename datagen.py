"""
file: datagen.py
python version: 3.5
Authors : Kantha Girish, Akshay Karki
description: This file contains functions to generate random string sequences for testing LCS
algorithms
"""

import numpy.random as rand
import sys
acgt = "acgt"
bits = "01"


def get_random_acgt(length, delta=None):
    """
    :param length: length of the strings to generate
    :param delta: number of characters that should differ between x and y. 0 < delta < length.
    :return: generated strings x and y which contain sequence of letters 'acgt'

    This function generates random sequence of `acgt` characters of given length. Given delta,
    which is in the range (0 < delta < length), the string y is generated with delta number
    of characters differing from x.
    """
    x = "".join([acgt[rand.randint(0, len(acgt))] for _ in range(length)])
    if delta is None:
        return x, x
    else:
        delta_idx = rand.permutation(len(x))[:delta]
        y = "".join([acgt[rand.randint(0, len(acgt))]
                     if i in delta_idx
                     else x[i]
                     for i in range(len(x))])
        return x, y


def get_random_bits(length, delta=None):
    """
    :param length: length of the string sequences to generate
    :param delta: number of characters that should differ between x and y. 0 < delta < length.
    :return: generated strings x and y which contain sequence of bits '01'

    This function generates random sequence of `01` characters of given length. Given delta,
    which is in the range (0 < delta < length), the string y is generated with delta number
    of characters differing from x.
    """
    x = "".join([bits[rand.randint(0, len(bits))] for _ in range(length)])
    if delta is None:
        return x, x
    else:
        delta_idx = rand.permutation(len(x))[:delta]
        y = "".join([bits[rand.randint(0, len(bits))]
                     if i in delta_idx
                     else x[i]
                     for i in range(len(x))])
        return x, y

functions = {
    "bits": get_random_bits,
    "acgt": get_random_acgt
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 " + __file__ + " acgt/bits N")
        print("acgt - generate sequences of acgt")
        print("bits- generate sequences of binary digits")
        print("N - length of the random strings to generate")
    else:
        type = sys.argv[1]
        size = int(sys.argv[2])
        delta = round(size * 0.3)
        if type in functions:
            x, y = functions[type](size, delta)
            with open(type + ".txt", 'w') as f:
                f.write(x + "\n" + y)
        else:
            print("unknown type, please specify valid type (acgt/bits)")
