import json
import os

class StatisticsRecorder:
    def save(self, folder, result):
        filename = os.path.join(folder, "statistics.json")
        data = {
            "distance": result.distance,
            "energy": result.energy,
            "execution_time": result.execution_time,
            "simulation_time": result.simulation_time,
            "blocked_moves": result.blocked_moves,
            "collisions": result.collisions
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Statistics Saved")