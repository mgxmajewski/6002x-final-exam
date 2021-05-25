import random, pylab


# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


def count_longest_run(trial):
    result = 1
    max_result = 0
    last_seen = trial[0]

    for v in trial[1:]:
        if v == last_seen:
            result += 1
        else:
            if result > max_result:
                max_result = result
            last_seen = v
            result = 1

    # just in case the longest sequence would be at the end of your list...
    if result > max_result:
        max_result = result
    return max_result



# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    trial_results = []
    for trials in range(numTrials):
        rolls_results = []
        for rolls in range(numRolls):
            rolls_results.append(die.roll())
        trial_results.append(rolls_results)
    rolls_results = []

    longest_runs = []
    for trial in trial_results:
        longest_runs.append(count_longest_run(trial))

    longest_run_sum = sum(longest_runs)
    longest_run_mean = longest_run_sum/numTrials

    makeHistogram(longest_runs, 10, 'roll', 'value', title=None)

    return longest_run_mean


# One test case

# print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 5, 10))
print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))