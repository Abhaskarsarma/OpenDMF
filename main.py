from experiments.config import ExperimentConfig
from experiments.experiment import Experiment

from visualization.console_renderer import ConsoleRenderer
from visualization.matplotlib_renderer import MatplotlibRenderer

from reports.reporter import Reporter

def main():
    config = ExperimentConfig(
        name="Dijkstra_Example",
        algorithm="Dijkstra",
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
    #renderer = ConsoleRenderer(delay=0.2)
    renderer = MatplotlibRenderer()
    renderer.render(experiment.simulation.history)
    reporter = Reporter()
    reporter.print_summary(result)

if __name__ == "__main__":
    main()