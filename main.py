from experiments.config import ExperimentConfig
from experiments.experiment import Experiment

def display_snapshot(snapshot):

    print("\nSnapshot at Time =", snapshot.time)
    print("=" * 35)

    for row in snapshot.grid:

        line = ""

        for cell in row:

            if cell.blocked:
                line += " X "

            elif cell.droplet is not None:
                line += " D "

            else:
                line += " . "

        print(line)


config = ExperimentConfig(

    name="AStar_Example",

    algorithm="AStar",

    chip_rows=8,

    chip_cols=8,

    start=(0, 0),

    goal=(7, 7),

    obstacles=[
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 5),
        (5, 5)
    ]
)

experiment = Experiment(config)

result = experiment.run()

snapshot = experiment.simulation.snapshot()

print(snapshot.time)

print("\n" + "="*60)
print("Snapshot Test")
print("="*60)

history = experiment.simulation.history

print(f"Number of snapshots: {len(history)}")

for i, snapshot in enumerate(history):
    print(f"Snapshot {i}: Time = {snapshot.time}")
    
##########################################################
#history = experiment.simulation.history
print(f"Snapshots stored: {len(history)}")

first = history[0]
last = history[-1]

print("\nFirst Snapshot")
print("----------------")
print("Time:", first.time)

print("\nLast Snapshot")
print("----------------")
print("Time:", last.time)

print("\nObject IDs")
print(id(history[0]))
print(id(history[1]))
print(id(history[2]))

display_snapshot(history[-1])
#########################################################

print(result)