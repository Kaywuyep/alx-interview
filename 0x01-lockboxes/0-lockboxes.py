#!/usr/bin/python3
"""a lockbox module"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened using their keys.
    Args:
    boxes: A list of lists, where each inner list represents the keys
          found in a box.
    Returns:
      True if all boxes can be opened, False otherwise.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for b in range(1, len(boxes) - 1):
        visited = False  # boxes checked
        for idx in range(len(boxes)):
            visited = b in boxes[idx] and b != idx
            if visited:
                break
        if visited is False:
            return visited
    return True
