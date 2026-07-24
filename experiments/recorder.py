from experiments.trajectory import TrajectoryRecorder
from experiments.statistics import StatisticsRecorder

class ExperimentRecorder:
    """
    Coordinates saving all experiment outputs.
    """
    def __init__(self):
        self.trajectory = TrajectoryRecorder()
        self.statistics = StatisticsRecorder()

    def record(self, folder, result):
        self.trajectory.save(folder, result.trajectory)
        self.statistics.save(folder, result)