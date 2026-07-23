# OpenDMF

<p align="center">

# 🧪 OpenDMF

### **Open Source Digital Microfluidics Simulation Framework**

*A modular research platform for Digital Microfluidic Biochip (DMFB) simulation, routing, scheduling, optimization, and future hardware integration.*

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Alpha-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# Overview

OpenDMF is an open-source research framework for **Digital Microfluidic Biochips (DMFBs)**.

The objective of OpenDMF is to provide a modular and extensible platform for

- Droplet Routing
- Scheduling
- Placement
- Placement–Path–Actuation (PPA) Optimization
- Machine Learning
- Biochip Design Automation
- Hardware Integration

The framework is designed for researchers, students, and educators working in digital microfluidics.

---

# Features

## Implemented

- Grid-based chip model
- Droplet representation
- Cell state management
- Simulation clock
- Statistics engine
- Experiment framework
- A* routing
- Experiment logging
- Snapshot history

---

# Planned

- Console visualization
- Matplotlib visualization
- GIF animation
- Dijkstra routing
- Lee routing
- Multi-droplet routing
- Scheduling engine
- Optimization algorithms
- Hardware controller

---

# Project Structure

```text
OpenDMF/
│
├── core/
├── routing/
├── experiments/
├── visualization/
├── optimization/
├── scheduler/
├── tests/
├── docs/
├── examples/
├── results/
│
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Abhaskarsarma/OpenDMF.git
```

Move into the directory

```bash
cd OpenDMF
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# Quick Start

```python
from experiments.experiment import Experiment
from experiments.config import ExperimentConfig

config = ExperimentConfig(...)

experiment = Experiment(config)

experiment.run()
```

---

# Current Status

Current Version

```
v0.2.1-alpha
```

Status

🟢 Active Development

---

# Development Roadmap

| Version | Features |
|----------|----------|
| v0.3 | Visualization Engine |
| v0.4 | Additional Routing Algorithms |
| v0.5 | Multi-Droplet Routing |
| v0.6 | Scheduling |
| v0.7 | PPA Optimization |
| v0.8 | Metaheuristic Optimization |
| v0.9 | Machine Learning |
| v1.0 | Stable Public Release |

---

# Documentation

Project documentation will be available in the `docs/` directory.

---

# Contributing

Contributions are welcome.

Future contributions include

- Routing algorithms
- Optimization methods
- Visualization
- Hardware interface
- Documentation

---

# Citation

A citation file (`CITATION.cff`) will be added in the next release.

---

# License

MIT License

---

# Author

**Dr. Padmanabha Sarma**

Biomedical Engineering Researcher

Research Interests

- Digital Microfluidics
- Medical Image Analysis
- Biomedical Signal Processing
- Artificial Intelligence
- Optimization
- Computational Modelling

---

## Vision

> **Building an open-source ecosystem for Digital Microfluidics research.**
