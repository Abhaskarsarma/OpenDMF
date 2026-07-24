from routing.astar import AStarRouter
from routing.dijkstra import DijkstraRouter

class RouterFactory:
    ROUTERS = {
        "astar": AStarRouter,
        "dijkstra": DijkstraRouter

    }

    @staticmethod
    def create(name):

        key = name.lower()

        if key not in RouterFactory.ROUTERS:
            raise ValueError(
                f"Unknown routing algorithm: {name}"
            )

        return RouterFactory.ROUTERS[key]()