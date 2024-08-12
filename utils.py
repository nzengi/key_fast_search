import random

def random_walk(start, end):
    return random.randint(start, end)

def min_distance_worker(workers):
    return min(workers, key=lambda w: w.best_distance)
