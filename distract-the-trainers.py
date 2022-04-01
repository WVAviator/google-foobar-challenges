# Distract the Trainers
# =====================

# The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.

# The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

# You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!

# For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.

# How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

# Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

# Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

# The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

def isPowerOfTwo(n):
    return n and (not(n & (n - 1)))

def thumbWar(x, y):
    if (x + y) % 2 != 0: return 0
    if (x == y): return 2
    
    if isPowerOfTwo((x + y) // gcd(x, y)):
        return 2
    return 0

def gcd(a, b):
    if a == 0: return b
    if b == 0 : return a
    if a >= b: return gcd(b, a % b)
    return gcd(a, b % a)

def leastRemainingNumbersToMatch(target, pairs):
    numbers = {}
    matchedNumbers = set()
    for pair in pairs:
        if pair[0] in numbers:
            numbers[pair[0]] += 1
        else:
            numbers[pair[0]] = 1
        if pair[1] in numbers:
            numbers[pair[1]] += 1
        else:
            numbers[pair[1]] = 1
    numbers = sorted(numbers, key = lambda x: numbers[x])
    
    for n in numbers:
        for pair in pairs:
            if pair[0] in matchedNumbers or pair[1] in matchedNumbers:
                continue
            if n in pair:
                matchedNumbers.add(pair[0])
                matchedNumbers.add(pair[1])
    return target - len(matchedNumbers)

def solution(banana_list):
    pairs = set()
    for i in range(len(banana_list) - 1):
        for j in range(i + 1, len(banana_list)):
            result = thumbWar(banana_list[i], banana_list[j])
            if result == 0: 
                pairs.add((i, j))

    return leastRemainingNumbersToMatch(len(banana_list), pairs)
    


import time

def test(testName, expected, testFunction):

    formattedName = testName[:25] if len(testName) > 25 else testName.rjust(25)

    start = time.time()
    res = testFunction()
    end = time.time()

    passed = "PASSED" if res == expected else "FAILED"

    print(formattedName, "|", passed, "| Result:", res, "Expected:", expected, "Time:", end - start)


test("gcd 01", 6, lambda: gcd(270, 192))
test("gcd 02", 14, lambda: gcd(29834, 2352))
test("gcd 03", 155, lambda: gcd(1240, 27745))
test("gcd 04", 9856, lambda: gcd(995456, 8821120))

test("isPowerOfTwo 01", True, lambda: isPowerOfTwo(128))
test("isPowerOfTwo 02", False, lambda: isPowerOfTwo(129))
test("isPowerOfTwo 03", True, lambda: isPowerOfTwo(16777216))
test("isPowerOfTwo 04", False, lambda: isPowerOfTwo(134217720))

test("thumbWar 01", 0, lambda: thumbWar(1, 47))
test("thumbWar 02", 2, lambda: thumbWar(155, 93))
test("thumbWar 03", 0, lambda: thumbWar(155, 94))
test("thumbWar 04", 2, lambda: thumbWar(987, 33553445))
test("thumbWar 05", 2, lambda: thumbWar(32, 32))

test("leastRemainingMatches 01", 0, lambda: leastRemainingNumbersToMatch(4, {(0, 1), (2, 3), (1, 3)}))
test("leastRemainingMatches 02", 0, lambda: leastRemainingNumbersToMatch(4, {(0, 1), (2, 3), (1, 3), (0, 2), (2, 1), (3, 1)}))
test("leastRemainingMatches 03", 1, lambda: leastRemainingNumbersToMatch(9, {(0, 1), (2, 3), (1, 3), (0, 2), (2, 1), (3, 1), (4, 5), (5, 6), (6, 7), (7, 8)}))

test("solution 01", 2, lambda: solution([1, 1]))
test("solution 02", 0, lambda: solution([1, 7, 3, 21, 13, 19]))
test("solution 03", 4, lambda: solution([7, 1, 7, 1, 7, 8]))
test("solution 04", 0, lambda: solution([33553445, 987, 155, 94, 1, 47]))
test("solution 05", 60, lambda: solution([32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 32, 1, 1]))





# print(thumbWar(1, 47), recur(1, 47))
# print(thumbWar(155, 93), recur(155, 93))
# print(thumbWar(155, 94), recur(155, 94))
