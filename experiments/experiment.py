import time

from core.chip import Chip
from core.droplet import Droplet
from core.simulation import Simulation

from routing.astar import AStarRouter

from experiments.result import ExperimentResult
from experiments.logger import ExperimentLogger


class Experiment:

    def __init__(self, config):

        self.config = config

        self.logger = ExperimentLogger()

        self.chip = None
        self.simulation = None
        self.router = None
        self.droplet = None

    def run(self):

        print("=" * 60)
        print("Starting Experiment")
        print("=" * 60)

        start_time = time.perf_counter()

        # -----------------------------
        # Create Chip
        # -----------------------------
        self.chip = Chip(
            self.config.chip_rows,
            self.config.chip_cols
        )

        # -----------------------------
        # Add Obstacles
        # -----------------------------
        for row, col in self.config.obstacles:
            self.chip.block_cell(row, col)

        # -----------------------------
        # Create Droplet
        # -----------------------------
        self.droplet = Droplet(
            droplet_id=1,
            row=self.config.start[0],
            col=self.config.start[1]
        )

        self.chip.place_droplet(self.droplet)

        # -----------------------------
        # Create Simulation
        # -----------------------------
        self.simulation = Simulation(self.chip)

        # -----------------------------
        # Router
        # -----------------------------
        self.router = AStarRouter()

        path = self.router.find_path(
            self.chip,
            self.config.start,
            self.config.goal
        )

        # -----------------------------
        # Execute Path
        # -----------------------------
        for row, col in path[1:]:

            self.chip.move_droplet(
                self.droplet,
                row,
                col
            )

            self.simulation.step()

        execution_time = time.perf_counter() - start_time

        energy = self.chip.statistics.total_distance

        result = ExperimentResult(

            success=True,

            execution_time=execution_time,

            simulation_time=self.simulation.clock.now(),

            path_length=len(path),

            distance=self.chip.statistics.total_distance,

            energy=energy,

            total_moves=self.chip.statistics.total_moves,

            successful_moves=self.chip.statistics.successful_moves,

            blocked_moves=self.chip.statistics.blocked_moves,

            collisions=self.chip.statistics.collisions,

            trajectory=self.droplet.path

        )

        self.logger.save(
            self.config,
            result
        )

        print("\nExperiment Finished")

        return result