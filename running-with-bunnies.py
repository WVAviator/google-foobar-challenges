#!/usr/bin/env python2.6
# Running with Bunnies
# ====================

# You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast! Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close. 

# The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

# In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

# Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

# For instance, in the case of
# [
#   [0, 2, 2, 2, -1],  # 0 = Start
#   [9, 0, 2, 2, -1],  # 1 = Bunny 0
#   [9, 3, 0, 2, -1],  # 2 = Bunny 1
#   [9, 3, 2, 0, -1],  # 3 = Bunny 2
#   [9, 3, 2, 2,  0],  # 4 = Bulkhead
# ]
# and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:

# Start End Delta Time Status
#     -   0     -    1 Bulkhead initially open
#     0   4    -1    2
#     4   2     2    0
#     2   4    -1    1
#     4   3     2   -1 Bulkhead closes
#     3   4    -1    0 Bulkhead reopens; you and the bunnies exit

# With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the solution is [1, 2].

def hasNegativeCycle(edges):
    
    distances = {}
    for edge in edges:
        if edge[0] not in distances:
            distances[edge[0]] = float('inf')
        if edge[1] not in distances:
            distances[edge[1]] = float('inf')

    distances[edges[0][0]] = 0

    for i in range(len(edges)):
        for edge in edges:
            if distances[edge[0]] + edge[2] < distances[edge[1]]:
                distances[edge[1]] = distances[edge[0]] + edge[2]

    for edge in edges:
        if distances[edge[0]] + edge[2] < distances[edge[1]]:
            return True

    return False

def extractEdges(times):
    edges = []
    for i in range(len(times)):
        for j in range(len(times[i])):
            if (i != j):
                edges.append([i, j, times[i][j]])
    return edges

def getCheapestPath(edges, start, end):
    distances = {}
    for edge in edges:
        if edge[0] not in distances:
            distances[edge[0]] = float('inf')
        if edge[1] not in distances:
            distances[edge[1]] = float('inf')

    distances[start] = 0

    for i in range(len(edges)):
        for edge in edges:
            if distances[edge[0]] + edge[2] < distances[edge[1]]:
                distances[edge[1]] = distances[edge[0]] + edge[2]

    return distances[end]

def getAllPermutations(array, size):
    
    if size == 1:
        return [array]
       
    
    permutations = []
    for i in range(size):

        if array not in permutations:
            permutations.append(array[:])
        getAllPermutations(array, size - 1)

        if size & 1:
            array[0], array[size - 1] = array[size - 1], array[0]
        else:
            array[i], array[size - 1] = array[size - 1], array[i]
    
    return permutations

def getAllPaths(numberOfBunnies):
    
    bunnies = [n + 1 for n in range(numberOfBunnies)]
    combinations = []
    getAllItemCombinations(bunnies, combinations)
    paths = []
    for combination in combinations:
        perms = getAllPermutations(combination, len(combination))
        for perm in perms:
            perm.insert(0, 0)
            perm.append(numberOfBunnies + 1)
            paths.append(perm)
    return paths


def getAllItemCombinations(items, combinations):
    
    if len(items) < 1:
        return
    if not items in combinations:
        combinations.append(items)
    
    for item in items:
        newItems = items[:]
        newItems.remove(item)
        getAllItemCombinations(newItems, combinations)
        
def arraySum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
                


def solution(times, time_limit):
    
    edges = extractEdges(times)
    if hasNegativeCycle(edges):
        return [b - 1 for b in range(1, len(times) - 1)]
    
    paths = getAllPaths(len(times) - 2)

    longestPath = []
    longestPathWorkerIds = 1000
    for path in paths:
        if len(path) < len(longestPath):
            continue
        cost = 0
        for i in range(len(path) - 1):
            cost += getCheapestPath(edges, path[i], path[i + 1])
        if cost <= time_limit:
            if len(longestPath) == len(path):
                    pathSum = arraySum(path)
                    if pathSum < longestPathWorkerIds:
                        longestPath = path
                        longestPathWorkerIds = pathSum
            elif len(longestPath) < len(path):
                longestPath = path
                longestPathWorkerIds = arraySum(path)

    sortedPath = sorted(longestPath)
    bunnies = sortedPath[1:-1]
    bunnies = [b - 1 for b in bunnies]
    return bunnies


from test import equals


equals("hasNegativeCycle 01", True, lambda: hasNegativeCycle([[0, 1, 1], [1, 2, -2], [2, 0, 0]]))
equals("hasNegativeCycle 01", False, lambda: hasNegativeCycle([[0, 1, 1], [1, 2, -1], [2, 0, 0]]))
equals("hasNegativeCycle 01", True, lambda: hasNegativeCycle([[0, 1, 1], [1, 2, -2], [2, 3, 0], [3, 0, 0], [0, 2, 0]]))

equals("getCheapestPath 01", 2, lambda: getCheapestPath([[0,2,2], [0,1,0], [0,6,0], [6,5,0],[5,7,3],[1,4,1],[1,5,0],[2,4,1],[2,3,0],[3,7,2],[4,7,1],[1,2,3]], 0, 7))
equals("getCheapestPath 02", 1, lambda: getCheapestPath([[0,1,0], [1,3,1], [0,2,2], [2,3,1]], 0, 3))
equals("getCheapestPath 03", 289, lambda: getCheapestPath([[0, 1, 144], [1, 2, 144], [2, 3, 1], [0, 3, 290]], 0, 3))

equals("solution 01", [1, 2], lambda: solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
equals("solution 02", [0, 1, 2], lambda: solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [-2, 3, 2, 2, 0]], 1))
equals("solution 03", [0, 1], lambda: solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))





