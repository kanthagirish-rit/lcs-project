#!/bin/sh

FORMAT="%MKB, %E"

# Shell script to run experiments on all four algorithms for various lengths of string
# sequences

# Run experiments until size 25 for all four
max=25
for i in `seq 2 $max`
do
    echo "$i"
    python3 datagen.py acgt "$i";
    time -f "$i, $FORMAT" -o recursive_0.txt -a python3 recursive.py acgt 0 >> \
    recursive_0_calls.txt ;
    time -f "$i, $FORMAT" -o recursive_1.txt -a python3 recursive.py acgt 1 >> \
    recursive_1_calls.txt ;
    time -f "$i, $FORMAT" -o memoization.txt -a python3 memoization.py acgt >> \
    re_memoization.txt;
    time -f "$i, $FORMAT" -o dynamic_0.txt -a python3 dynamicprog.py acgt 0;
    time -f "$i, $FORMAT" -o dynamic_1.txt -a python3 dynamicprog.py acgt 1;
    time -f "$i, $FORMAT" -o hlcs_0.txt -a python3 hlcs.py acgt 0;
    time -f "$i, $FORMAT" -o hlcs_1.txt -a python3 hlcs.py acgt 1;
done

# Run experiments from size 25 to 200 for three algorithms except Naive recursive algorithm
max=200
for i in `seq 25 $max`
do
    echo "$i"
    python3 datagen.py acgt "$i";
    time -f "$i, $FORMAT" -o memoization.txt -a python3 memoization.py acgt >> \
    re_memoization.txt;
    time -f "$i, $FORMAT" -o dynamic_0.txt -a python3 dynamicprog.py acgt 0;
    time -f "$i, $FORMAT" -o dynamic_1.txt -a python3 dynamicprog.py acgt 1;
    time -f "$i, $FORMAT" -o hlcs_0.txt -a python3 hlcs.py acgt 0;
    time -f "$i, $FORMAT" -o hlcs_1.txt -a python3 hlcs.py acgt 1;
done

# Run experiments for DP and Hirschberg's algorithm for sizes until 10,000
max=10000
for i in `seq 300 100 $max`
do
    echo "$i"
    python3 datagen.py acgt "$i";
    time -f "$i, $FORMAT" -o dynamic_0.txt -a python3 dynamicprog.py acgt 0;
    time -f "$i, $FORMAT" -o dynamic_1.txt -a python3 dynamicprog.py acgt 1;
    time -f "$i, $FORMAT" -o hlcs_0.txt -a python3 hlcs.py acgt 0;
    time -f "$i, $FORMAT" -o hlcs_1.txt -a python3 hlcs.py acgt 1;
done
