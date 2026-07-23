# Mathematical Model of OpenDMF

## 1. Introduction

Digital Microfluidic Biochips (DMFBs) manipulate discrete droplets on an array of electrodes using the principle of electrowetting-on-dielectric (EWOD). In OpenDMF, the physical chip is abstracted into a discrete mathematical model that enables simulation, routing, scheduling, and optimization of droplet movements.

The objective of the mathematical model is to represent the biochip, droplets, routing constraints, and optimization objectives in a computationally efficient manner while remaining extensible for future hardware integration.

---

# 2. Chip Representation

The Digital Microfluidic Biochip is modeled as a two-dimensional rectangular grid

```
Chip = (R,C)
```

where

- **R** = number of rows
- **C** = number of columns

Each element of the grid represents a single electrode.

The total number of electrodes is

```
N = R × C
```

Each electrode is uniquely identified by its coordinate

```
E(i,j)
```

where

```
0 ≤ i < R

0 ≤ j < C
```

---

# 3. Cell States

Each electrode (cell) can exist in one of several states.

| State | Description |
|--------|-------------|
| EMPTY | Available for movement |
| OCCUPIED | Contains a droplet |
| BLOCKED | Obstacle or unavailable |
| MODULE | Reserved functional module |

OpenDMF stores these states internally using the `CellState` enumeration.

---

# 4. Droplet Representation

A droplet is represented as

```
D = (x,y,t)
```

where

- x = row position
- y = column position
- t = simulation time

Additional droplet properties include

- Identifier
- Volume
- Velocity
- Current trajectory

The trajectory is stored as

```
Trajectory =
[(x0,y0),
(x1,y1),
...
(xn,yn)]
```

---

# 5. Neighbor Model

OpenDMF currently uses a four-neighbor grid.

```
        (x-1,y)

(x,y-1)  (x,y)  (x,y+1)

        (x+1,y)
```

Allowed movements are

```
UP
DOWN
LEFT
RIGHT
```

Future versions will support

- Diagonal movement
- Hexagonal electrodes
- Irregular chip layouts

---

# 6. Routing Path

A routing path is defined as

```
P =
{
D0,
D1,
...
Dn
}
```

where

```
D0
```

is the source position and

```
Dn
```

is the destination.

---

# 7. Distance Metric

OpenDMF currently uses Manhattan distance as the heuristic for A* routing.

```
h(n) = |xgoal−x| + |ygoal−y|
```

This heuristic is admissible for four-directional movement.

---

# 8. Path Cost

For a path

```
P
```

the routing cost is

```
Cost(P)
=
Σ MoveCost
```

Currently,

```
MoveCost = 1
```

for every valid movement.

Future versions may include

- Different electrode costs
- Congestion penalties
- Timing penalties
- Energy penalties

---

# 9. Simulation Time

Simulation proceeds in discrete clock cycles.

```
t = 0,1,2,...,T
```

One droplet movement corresponds to one simulation step.

---

# 10. Energy Model

In the current implementation

```
Energy
=
Number of Successful Moves
```

Future versions will incorporate

- Electrode capacitance
- Actuation voltage
- Switching frequency
- Experimental energy models

---

# 11. Optimization Objective

The routing algorithm seeks to minimize

```
f(P)
=
Path Length
+
Execution Time
+
Energy Consumption
```

subject to

- Chip boundaries
- Static obstacles
- Collision avoidance
- Module constraints

---

# 12. Future Extensions

The mathematical model will be extended to include

- Multi-droplet routing
- Dynamic obstacles
- Scheduling constraints
- Placement optimization
- Fault-tolerant routing
- Machine learning assisted routing
- Hardware-aware optimization

---

# Summary

OpenDMF currently models the Digital Microfluidic Biochip as a discrete graph where each electrode represents a node and droplet movements correspond to graph transitions.

This mathematical abstraction forms the basis for routing algorithms, scheduling methods, optimization techniques, and future hardware integration.