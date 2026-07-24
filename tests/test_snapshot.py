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
    name="Snapshot_Test",
    algorithm="AStar",
    chip_rows=8,
    chip_cols=8,
    start=(0,0),
    goal=(7,7),
    obstacles=[
        (3,3),
        (3,4),
        (3,5),
        (4,5),
        (5,5)
    ]
)

experiment = Experiment(config)
result = experiment.run()
history = experiment.simulation.history

print("="*60)
print("Snapshot Test")
print("="*60)
print(f"Snapshots stored : {len(history)}")
first = history[0]
last = history[-1]
display_snapshot(last)