#!/bin/python3

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = 10000000001
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)


