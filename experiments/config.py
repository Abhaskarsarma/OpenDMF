from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class ExperimentConfig:
    """
    Stores all parameters required to execute one experiment.
    """

    # -----------------------------
    # Experiment Information
    # -----------------------------
    name: str
    algorithm: str

    # -----------------------------
    # Chip
    # -----------------------------
    chip_rows: int
    chip_cols: int

    # -----------------------------
    # Routing
    # -----------------------------
    start: Tuple[int, int]
    goal: Tuple[int, int]

    # -----------------------------
    # Obstacles
    # -----------------------------
    obstacles: List[Tuple[int, int]] = field(default_factory=list)

    # -----------------------------
    # Droplets
    # -----------------------------
    droplet_count: int = 1

    # -----------------------------
    # Electrical Parameters
    # -----------------------------
    voltage: float = 80.0
    frequency: float = 1000.0

    # -----------------------------
    # Simulation
    # -----------------------------
    random_seed: int = 42