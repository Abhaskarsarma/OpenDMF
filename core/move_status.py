# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:09:26 2026

@author: Admin
"""

from enum import Enum

class MoveStatus(Enum):

    SUCCESS = 0
    OUT_OF_BOUNDS = 1
    BLOCKED = 2
    COLLISION = 3