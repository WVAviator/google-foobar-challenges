# The Grandest Staircase Of Them All
# ==================================

# With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options. 

# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

# #
# ##
# 21

# When N = 4, you still only have 1 staircase choice:

# #
# #
# ##
# 31
 
# But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

# #
# #
# #
# ##
# 41

# #
# ##
# ##
# 32

# Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

possibleConifgurations = set([])

def serialize(list):
    return ",".join(map(str, list))


def checkSteps(steps):
    
    if (serialize(steps)) in possibleConifgurations:
        # print(steps, " is not valid [duplicate]")
        return False
    
    last = steps[0]
    for i in range(1, len(steps)):
        if steps[i] >= last:
            # print(steps, " is not valid")
            return False
        last = steps[i]
    possibleConifgurations.add(serialize(steps))
    # print(steps, " is valid")
    return True

def dropStep(steps):
    
    for i in range(len(steps)):

        if steps[len(steps) - 1] > 1:
            steps.append(0)
        
        if i < len(steps) - 1 and steps[i + 1] == steps[i] - 1 or steps[i] == 0: continue
        for j in range(i + 1, len(steps)):
            
            steps[i] -= 1
            steps[j] += 1

            if checkSteps(steps):
                dropStep(steps)

            steps[j] -= 1
            steps[i] += 1
        
        if steps[len(steps) - 1] == 0:
            steps.pop()
            
    return

def solution1(n):
    
    possibleConifgurations.clear()
    
    steps = [n - 1, 1]

    checkSteps(steps)
    dropStep(steps)

    return len(possibleConifgurations)

def isPrime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

def addAll(n):
    if n == 0: return 0
    return n + addAll(n - 1)

def solution(n):
    
    table = [1] + [0] * n

    for i in range(n):
        for j in range(n, i, -1):

            table[j] += table[j - i - 1]
    return table[n] - 1


from test import equals

equals("Test 1", 1, lambda: solution(3))
equals("Test 2", 1, lambda: solution(4))
equals("Test 3", 2, lambda: solution(5))
equals("Test 4", 3, lambda: solution(6))
equals("Test 5", 5, lambda: solution(8))
equals("Test 6", 9, lambda: solution(10))
equals("Test 7", 487067745, lambda: solution(200))

equals("CheckSteps Test 1", True, lambda: checkSteps([3, 2, 1]))
equals("CheckSteps Test 2", True, lambda: checkSteps([5, 4, 2, 1]))
equals("CheckSteps Test 3", False, lambda: checkSteps([3, 3, 1]))
