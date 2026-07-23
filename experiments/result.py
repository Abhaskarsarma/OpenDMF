from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ExperimentResult:

    success: bool

    execution_time: float

    simulation_time: int

    path_length: int

    distance: int

    energy: float

    total_moves: int

    successful_moves: int

    blocked_moves: int

    collisions: int

    trajectory: List[Tuple[int, int]]