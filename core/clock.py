# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:17:13 2026

@author: Admin
"""

class Clock:

    """
    Simulation Clock
    """

    def __init__(self):

        self.time = 0

    def tick(self):

        self.time += 1

    def reset(self):

        self.time = 0

    def now(self):

        return self.time