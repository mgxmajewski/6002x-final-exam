import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    probability_of_reproduction = 1 - CURRENTRABBITPOP/MAXRABBITPOP
    for rabbit in range(CURRENTRABBITPOP):
        if random.random() <= probability_of_reproduction and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1



def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    probability_fox_eats_rabbit = CURRENTRABBITPOP/MAXRABBITPOP
    probability_fox_born = 1/3
    probability_fox_die = 0.1
    for fox in range(CURRENTFOXPOP):
        if random.random() <= probability_fox_eats_rabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= probability_fox_born:
                CURRENTFOXPOP += 1
            elif random.random() <= probability_fox_die and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1






def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_population = []
    fox_population = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_population.append(CURRENTRABBITPOP)
        fox_population.append(CURRENTFOXPOP)
    return rabbit_population, fox_population


print(runSimulation(200))
