from copy import deepcopy

class Snapshot:

    def __init__(self, time, grid, statistics):

        self.time = time

        # Deep copy ensures the snapshot never changes
        self.grid = deepcopy(grid)

        self.statistics = deepcopy(statistics)