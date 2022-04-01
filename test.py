import time
def equals(testName, expected, testFunction):

    formattedName = testName[:25] if len(testName) > 25 else testName.rjust(25)

    start = time.perf_counter()
    res = testFunction()
    end = time.perf_counter()

    passed = "PASSED" if res == expected else "FAILED"

    print(formattedName, "|", passed, "| Result:", res, "Expected:", expected, "Time:", end - start)

def lengthEquals(testName, expected, testFunction):
    formattedName = testName[:25] if len(testName) > 25 else testName.rjust(25)

    start = time.perf_counter()
    res = testFunction()
    end = time.perf_counter()

    passed = "PASSED" if len(res) == expected else "FAILED"

    print(formattedName, "|", passed, "| Result:", len(res), "Expected:", expected, "Time:", end - start)

def executesInTimeLimit(testName, timeLimit, testFunction):
    formattedName = testName[:25] if len(testName) > 25 else testName.rjust(25)

    start = time.perf_counter()
    res = testFunction()
    end = time.perf_counter()

    executionTime = end - start

    passed = "PASSED" if executionTime < timeLimit else "FAILED"

    print(formattedName, "|", passed, "| Time Limit:", timeLimit, "Executed In:", executionTime)
