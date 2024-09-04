#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game
    """
    def sieve_and_prefix_sum(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        prefix_sum = [0] * (n + 1)
        for i in range(2, n + 1):
            if primes[i]:
                prefix_sum[i] = prefix_sum[i-1] + 1
                for j in range(i*i, n + 1, i):
                    primes[j] = False
            else:
                prefix_sum[i] = prefix_sum[i-1]
        return prefix_sum

    prefix_sum = sieve_and_prefix_sum(10000)

    maria_wins = 0
    ben_wins = 0

    for round in range(x):
        if round < len(nums):
            n = nums[round]
            prime_count = prefix_sum[n]
            if prime_count % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
