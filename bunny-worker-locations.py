import time

# Bunny Worker Locations
# ======================

# Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.

# The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

# For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers). 

# Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.

def solution(x, y):
    xIndex, yIndex, workerId = 1, 1, 1

    while xIndex < x:
        xIndex += 1
        workerId += xIndex

    while yIndex < y:
        yIndex += 1
        workerId += xIndex
        xIndex += 1

    return str(workerId)

from test import equals

equals("Test 1", "9", lambda: solution(3, 2))
equals("Test 2", "96", lambda: solution(5, 10))
equals("Test 3", "28", lambda: solution(7, 1))