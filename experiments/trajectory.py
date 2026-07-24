import csv
import os

class TrajectoryRecorder:
    """
    Saves droplet trajectory to CSV.
    """
    def save(self, folder, trajectory):
        filename = os.path.join(folder, "trajectory.csv")
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Time",
                "Row",
                "Column"
            ])

            for t, (row, col) in enumerate(trajectory):
                writer.writerow([
                    t,
                    row,
                    col
                ])
        print("Trajectory Saved")