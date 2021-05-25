
# In a lecture, there are 3 things you might do:
# listen,
# sleep,
# or Facebook
# (in a single lecture, you might do all, some, or none of them).
# Lectures are independent of each other, the probabilities associated
# with the activities are independent of each other, and they are all > 0.
# You are given the following class, Lecture, and the function, get_mean_and_std.

import random


class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb

    def get_listen_prob(self):
        return self.listen

    def get_sleep_prob(self):
        return self.sleep

    def get_fb_prob(self):
        return self.fb


def get_mean_and_std(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std



def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object

    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence
             interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION
    fb_probability = aLecture.get_fb_prob()
    sleep_probability = aLecture.get_sleep_prob()
    listen_probability = aLecture.get_listen_prob()
    all_events_happens_counter = []
    event_counter = 0
    for trials in range(N):
        if random.random() <= fb_probability and random.random() <= sleep_probability and random.random() <= listen_probability:
            event_counter += 1
            all_events_happens_counter.append(event_counter)
            event_counter = 0
        else:
            event_counter += 1

    sample_mean = get_mean_and_std(all_events_happens_counter)[0]
    std = get_mean_and_std(all_events_happens_counter)[1]
    sample_size = len(all_events_happens_counter)
    print(sample_size)
    se = std/sample_size**0.5
    ci = 2*std*1.96

    return sample_mean, ci



# sample test cases
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)

b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)
