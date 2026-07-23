import json
import csv
import platform
import sys
from pathlib import Path
from dataclasses import asdict
from datetime import datetime


class ExperimentLogger:

    experiment_counter = 1

    def __init__(self):

        self.root = Path("results")
        self.root.mkdir(exist_ok=True)

    # --------------------------------------------------

    def save(self, config, result):

        folder = self.create_folder(config)

        self.save_config(folder, config)

        self.save_metadata(folder)

        self.save_result(folder, result)

        self.save_statistics(folder, result)

        self.save_trajectory(folder, result)

        self.save_readme(folder, config, result)

        print("\nExperiment Saved Successfully")

        print(folder)

    # --------------------------------------------------

    def create_folder(self, config):

        today = datetime.now().strftime("%Y%m%d")

        exp_id = f"EXP-{today}-{ExperimentLogger.experiment_counter:04d}"

        ExperimentLogger.experiment_counter += 1

        folder = self.root / f"{exp_id}_{config.name}"

        folder.mkdir(exist_ok=True)

        return folder

    # --------------------------------------------------

    def save_config(self, folder, config):

        with open(folder / "config.json", "w") as f:

            json.dump(
                asdict(config),
                f,
                indent=4
            )

    # --------------------------------------------------

    def save_metadata(self, folder):

        metadata = {

            "Project": "OpenDMF",

            "Version": "0.2.1",

            "Python": sys.version,

            "Platform": platform.platform(),

            "Date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        with open(folder / "metadata.json", "w") as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

    # --------------------------------------------------

    def save_result(self, folder, result):

        with open(folder / "result.json", "w") as f:

            json.dump(
                asdict(result),
                f,
                indent=4
            )

    # --------------------------------------------------

    def save_statistics(self, folder, result):

        with open(folder / "statistics.csv", "w", newline="") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(["Metric", "Value"])

            writer.writerow(["Simulation Time", result.simulation_time])

            writer.writerow(["Execution Time", result.execution_time])

            writer.writerow(["Distance", result.distance])

            writer.writerow(["Energy", result.energy])

            writer.writerow(["Total Moves", result.total_moves])

            writer.writerow(["Successful Moves", result.successful_moves])

            writer.writerow(["Blocked Moves", result.blocked_moves])

            writer.writerow(["Collisions", result.collisions])

    # --------------------------------------------------

    def save_trajectory(self, folder, result):

        with open(folder / "trajectory.csv", "w", newline="") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(["Step", "Row", "Column"])

            for step, (r, c) in enumerate(result.trajectory):

                writer.writerow([step, r, c])

    # --------------------------------------------------

    def save_readme(self, folder, config, result):

        with open(folder / "README.md", "w") as f:

            f.write("# OpenDMF Experiment\n\n")

            f.write(f"Experiment : {config.name}\n\n")

            f.write(f"Algorithm : {config.algorithm}\n\n")

            f.write(f"Chip Size : {config.chip_rows} x {config.chip_cols}\n\n")

            f.write(f"Distance : {result.distance}\n\n")

            f.write(f"Simulation Time : {result.simulation_time}\n\n")

            f.write(f"Energy : {result.energy}\n\n")

            f.write(f"Status : {'SUCCESS' if result.success else 'FAILED'}\n")