# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:09:49 2026

@author: Admin
"""
class Statistics:

    def __init__(self):

        self.total_moves = 0
        self.successful_moves = 0
        self.blocked_moves = 0
        self.collisions = 0
        self.out_of_bounds = 0
        self.total_distance = 0
        self.simulation_time = 0

    def reset(self):

        self.__init__()

    def summary(self):

        return {

            "Total Moves": self.total_moves,
            "Successful Moves": self.successful_moves,
            "Blocked Moves": self.blocked_moves,
            "Collisions": self.collisions,
            "Out of Bounds": self.out_of_bounds,
            "Distance": self.total_distance,
            "Simulation Time": self.simulation_time

        }