#!/usr/bin/python3
'''Simple module since it has only a simple function canUnlockAll(boxes).'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened.'''
    opened_boxes = [False for i in range(len(boxes))]
    keys = {0}
    while keys:
        cur_key = keys.pop()
        opened_boxes[cur_key] = True
        for key in boxes[cur_key]:
            if not opened_boxes[key]:
                keys.add(key)
    return sum(opened_boxes) == len(boxes)
