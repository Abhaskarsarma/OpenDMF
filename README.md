\# OpenDMF

\### Open Source Digital Microfluidics Simulation Framework



<p align="center">

&#x20; <b>A modular Python framework for Digital Microfluidic Biochip (DMFB) simulation, routing, scheduling, optimization, and future hardware integration.</b>

</p>



\---



\## Overview



OpenDMF is an open-source simulation framework for \*\*Digital Microfluidic Biochips (DMFBs)\*\*. The project is designed to provide a modular, extensible, and reproducible platform for researchers, educators, and students working in the field of digital microfluidics.



The framework aims to bridge the gap between algorithm development and real-world implementation by supporting the complete workflow from simulation and optimization to future hardware control.



OpenDMF is being developed with the long-term vision of becoming a comprehensive research platform for:



\- Digital Microfluidic Biochips (DMFB)

\- Placement, Path, and Actuation (PPA) Optimization

\- Droplet Routing Algorithms

\- Scheduling Algorithms

\- Biochip Design Automation

\- Machine Learning-based Optimization

\- Hardware-in-the-Loop Simulation

\- Real DMFB Controller Integration



\---



\# Current Features



\### Core Simulation Engine



\- Grid-based DMFB chip model

\- Droplet representation

\- Cell state management

\- Simulation clock

\- Statistics collection

\- Experiment framework



\### Routing



\- A\* Path Planning



\### Experiment Management



\- Experiment configuration

\- Automatic experiment logging

\- Experiment metadata

\- Result serialization



\### Simulation Recording



\- Complete droplet trajectory

\- Snapshot history

\- Simulation replay support

\- Execution statistics



\---



\# Project Architecture



```

&#x20;                   OpenDMF



&#x20;     +-------------------------------+

&#x20;     |         Experiment            |

&#x20;     +-------------------------------+

&#x20;                  |

&#x20;       +----------+-----------+

&#x20;       |                      |

&#x20;    Simulation            Routing

&#x20;       |                      |

&#x20;    Snapshot              A\* Router

&#x20;       |

&#x20;  Statistics Engine

&#x20;       |

&#x20;  Experiment Logger

```



The modular architecture allows each component to evolve independently while maintaining a clean separation of responsibilities.



\---



\# Repository Structure



```

OpenDMF/



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



├── main.py

├── README.md

├── requirements.txt

└── LICENSE

```



\---



\# Mathematical Foundation



The simulator models a Digital Microfluidic Biochip as a two-dimensional discrete grid



\\\[

Chip = (R,C)

\\]



where each electrode corresponds to one computational cell.



A droplet state is represented as



\\\[

D=(x,y,t)

\\]



where



\- \\(x\\) : row coordinate

\- \\(y\\) : column coordinate

\- \\(t\\) : simulation time



Routing algorithms determine an optimal path



\\\[

P=\\{D\_0,D\_1,\\ldots,D\_n\\}

\\]



while minimizing routing cost, execution time, and energy consumption.



\---



\# Current Version



```

OpenDMF v0.2.1-alpha

```



Status:



✅ Core architecture completed



\---



\# Development Roadmap



\## Version 0.3



\- Visualization Engine

\- Console Renderer

\- Matplotlib Renderer

\- GIF Animation



\---



\## Version 0.4



Additional Routing Algorithms



\- Dijkstra

\- Lee Algorithm

\- BFS

\- DFS



Algorithm benchmarking



\---



\## Version 0.5



Multi-Droplet Simulation



\- Collision avoidance

\- Deadlock detection

\- Concurrent routing



\---



\## Version 0.6



Scheduling Engine



\- Assay scheduling

\- Resource allocation

\- Module management



\---



\## Version 0.7



Placement–Path–Actuation (PPA) Optimization



\---



\## Version 0.8



Optimization Algorithms



\- Genetic Algorithm

\- Particle Swarm Optimization

\- Simulated Annealing

\- Ant Colony Optimization



\---



\## Version 0.9



Machine Learning Integration



\- Congestion prediction

\- Routing prediction

\- Intelligent scheduling



\---



\## Version 1.0



First stable public release



\---



\# Installation



Clone the repository



```bash

git clone https://github.com/Abhaskarsarma/OpenDMF.git

```



Move into the project



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



\---



\# Research Vision



OpenDMF is being developed as a long-term open-source research platform for Digital Microfluidics.



The ultimate objective is to integrate



\- Simulation

\- Optimization

\- Artificial Intelligence

\- Experimental Validation

\- Real Hardware Control



within a single unified framework.



\---



\# Contributing



Contributions are welcome.



Future contributions may include



\- Routing algorithms

\- Scheduling algorithms

\- Optimization methods

\- Visualization tools

\- Hardware interfaces

\- Documentation improvements



\---



\# Citation



If you use OpenDMF in your research, please cite the project.



A formal citation file (`CITATION.cff`) will be added in future releases.



\---



\# License



This project is released under the MIT License.



\---



\# Author



\*\*Dr. Padmanabha Sarma\*\*



Biomedical Engineering Researcher



Research Interests



\- Digital Microfluidics

\- Medical Image Analysis

\- Biomedical Signal Processing

\- Artificial Intelligence

\- Optimization Algorithms

\- Computational Modelling



\---



\## OpenDMF



\*"Building the next generation open-source platform for Digital Microfluidics research."\*

