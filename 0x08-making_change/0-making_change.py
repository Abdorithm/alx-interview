#!/usr/bin/python3
"""
Making change module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of coin denominations available.
    total (int): The target amount to make change for.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if total is 0 or less.
         Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    dp = [0] * (total + 1)

    for i in range(1, total + 1):
        dp[i] = float('inf')
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
