# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:17:37 2026

@author: Admin
"""

from core.clock import Clock
from core.snapshot import Snapshot


class Simulation:

    """
    Controls the entire DMF simulation.
    """

    def __init__(self, chip):

        self.chip = chip
        self.clock = Clock()
        self.history = []
        self.history.append(self.snapshot())

    def snapshot(self):

        return Snapshot(
            time=self.clock.now(),
            grid=self.chip.grid,
            statistics=self.chip.statistics
        )
    
    def step(self):

        self.clock.tick()
        self.chip.statistics.simulation_time = self.clock.now()
        self.history.append(self.snapshot())

    def reset(self):

        self.clock.reset()
        
