# Mathematical Model

## Chip Representation

The Digital Microfluidic Biochip is represented as a two-dimensional grid:

```
Chip = (R, C)
```

where:

- `R` = number of rows
- `C` = number of columns

## Droplet State

A droplet is represented as:

```
D = (x, y, t)
```

where:

- `x` = row position
- `y` = column position
- `t` = simulation time

## Routing Path

```
P = {D0, D1, ..., Dn}
```

The objective is to minimize:

- Path length
- Execution time
- Energy consumption
- Number of blocked moves