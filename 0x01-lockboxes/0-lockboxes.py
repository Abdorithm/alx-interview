#!/usr/bin/python3
""" Solve lockboxes """


def canUnlockAll(boxes):
    """ Return True if all boxes can be unlocked
        Return False otherwise """
    keys = [0]
    for i in range(len(boxes)):
        for new_key in boxes[i]:
            if new_key != i and new_key < len(boxes) and new_key not in keys:
                keys.append(new_key)
    return len(keys) == len(boxes)
