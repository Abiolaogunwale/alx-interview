#!/usr/bin/python3
# You have n number of locked boxes in front of you.
# Each box is numbered sequentially from 0 to n - 1
# and each box may contain keys to the other boxes.

# Write a method that determines if all the boxes can be opened.ockboxes

def canUnlockAll(boxes):
    x = len(boxes)
    item = [False] * x
    item[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for each in boxes[box]:
            if each >= 0 and each < x and not item[each]:
                item[each] = True
                stack.append(each)

    return all(item)
