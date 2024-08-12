from .metrics import hamming_distance

class Worker:
    def __init__(self, start_range, end_range, target):
        self.start_range = start_range
        self.end_range = end_range
        self.position = self.random_start()
        self.target = target
        self.best_distance = self.calculate_distance()

    def random_start(self):
        return random.randint(self.start_range, self.end_range)

    def calculate_distance(self):
        return hamming_distance(self.position, self.target)

    def move_closer(self):
        if self.position < self.target:
            self.position += (self.target - self.position) // 2
        else:
            self.position -= (self.position - self.target) // 2
        self.best_distance = self.calculate_distance()

    def split_area(self):
        mid_point = (self.start_range + self.end_range) // 2
        return Worker(self.start_range, mid_point, self.target), Worker(mid_point + 1, self.end_range, self.target)

    def search(self):
        while self.best_distance > 0:
            self.move_closer()
        return self.position

def collaborative_search(workers):
    best_worker = min(workers, key=lambda w: w.best_distance)
    while best_worker.best_distance > 0:
        for worker in workers:
            if worker != best_worker and worker.best_distance > best_worker.best_distance:
                worker.start_range, worker.end_range = best_worker.split_area()[1].start_range, best_worker.split_area()[1].end_range
            worker.move_closer()
        best_worker = min(workers, key=lambda w: w.best_distance)
    return best_worker.position
