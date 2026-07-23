# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:08:46 2026

@author: Admin
"""

from enum import Enum


class CellState(Enum):
    EMPTY = 0
    OCCUPIED = 1
    OBSTACLE = 2

    MIXER = 3
    HEATER = 4
    DETECTOR = 5

    RESERVOIR = 6
    WASTE = 7
    WASH = 8