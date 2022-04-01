# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

class Node():
    def __init__(self, position):
        self.position = position
        
        self.gCost = 1
        self.hCost = 0
        self.fCost = 0
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)


def solution(map):
    
    startNode = Node((0, 0, 0))
    endNode = Node((len(map[0]) - 1, len(map) - 1, 0))
    
    openList = [startNode]
    closedList = set()

    while openList:
        currentNode = openList[0]
        currentIndex = 0

        for i in range(len(openList)):
            if openList[i].fCost < currentNode.fCost:
                currentNode = openList[i]
                currentIndex = i
        
        openList.pop(currentIndex)
        closedList.add(currentNode)

        if currentNode.position[0] == endNode.position[0] and currentNode.position[1] == endNode.position[1]:
            return currentNode.gCost

        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            neighborPosition = (currentNode.position[0] + offset[0], currentNode.position[1] + offset[1], currentNode.position[2])

            if neighborPosition[0] < 0 or neighborPosition[0] >= len(map[0]) or neighborPosition[1] < 0 or neighborPosition[1] >= len(map):
                continue

            if map[neighborPosition[1]][neighborPosition[0]] == 1:
                if currentNode.position[2] == 1:
                    continue
                neighborPosition = (neighborPosition[0], neighborPosition[1], 1)

            neighbor = Node(neighborPosition)

            if neighbor in closedList: 
                continue
            
            if neighbor in openList:

                openNodeIndex = openList.index(neighbor)
                if openList[openNodeIndex].gCost < currentNode.gCost + 1:
                    continue
                openList.pop(openNodeIndex)
                openList.append(neighbor)

            else:
                openList.append(neighbor)

            neighbor.gCost = currentNode.gCost + 1
            neighbor.hCost = endNode.position[0] - neighbor.position[0] + endNode.position[1] - neighbor.position[1]
            neighbor.fCost = neighbor.gCost + neighbor.hCost

    
    return -1


map1 = [[0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0]]
map2 = [[0,1,0,0,0], [0,1,0,1,0], [0,1,0,1,0], [0,1,0,1,0], [0,0,0,1,0]]
map3 = [[0,0,0,0,0,0,1,0,0,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,1,0,1,0], [0,0,0,0,1,0,0,0,1,0]]
map4 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
map5 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
map6 = [[0,1,0], [0,1,0], [0,1,0]]
map7 = [[0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0], [0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0]]
map8 = [[0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],[0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1],[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0],[0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0]]
map9 = [[0, 1],[1, 0]]
map10 = [[0, 1],[1, 1],[0, 1],[0, 0]]

from test import equals

equals("Test 1", 7, lambda: solution(map1))
equals("Test 2", 9, lambda: solution(map2))
equals("Test 3", 19, lambda: solution(map3))
equals("Test 4", 11, lambda: solution(map4))
equals("Test 5", 7, lambda: solution(map5))
equals("Test 6", 5, lambda: solution(map6))
equals("Test 7", 123, lambda: solution(map7))
equals("Test 8", 89, lambda: solution(map8))
equals("Test 9", 3, lambda: solution(map9))
equals("Test 10", 5, lambda: solution(map10))