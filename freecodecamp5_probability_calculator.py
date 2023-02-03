import copy
import random


class Hat:
    def __init__(self, **hats):
        self.contents = []
        for k, v in hats.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m

