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

    coins.sort(reverse=True)

    coin_count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            num_coins = remaining // coin
            coin_count += num_coins
            remaining -= num_coins * coin

        if remaining == 0:
            return coin_count

    return -1
