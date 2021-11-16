import copy
import random


class Hat:

    # Initializing instance variables
    def __init__(self, **balls):
        self.contents = []
        for color, num in balls.items():
            for r in range(num):
                self.contents.append(color)

    # Removes balls at random but doesn't put it back in
    def draw(self, drawnum):
        result = []
        if drawnum >= len(self.contents):
            return self.contents
        for r in range(drawnum):
            d = random.choice(self.contents)
            result.append(d)
            self.contents.remove(d)
        return result

# Performs a pool of experiments and returns probability of certain events of occurring


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    for e in range(num_experiments):

        # Required variables
        di = {}
        hatcopy = copy.deepcopy(hat)
        tf = None

        # Draws certain number of balls
        lst = hatcopy.draw(num_balls_drawn)

        # Checks for the matching balls
        for item in lst:
            if item not in list(expected_balls):
                continue
            di[item] = di.get(item, 0) + 1

        # Confirms the match
        if len(expected_balls) != len(di):
            continue
        for k, v in expected_balls.items():
            if di[k] >= v:
                tf = True
            else:
                tf = False
                break
        if tf == True:
            match += 1

    # Returns probability of success
    return match / num_experiments
