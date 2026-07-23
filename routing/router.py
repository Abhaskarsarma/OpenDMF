from abc import ABC, abstractmethod

class Router(ABC):

    @abstractmethod
    def find_path(self, chip, start, goal):
        """
        Returns a list of coordinates.
        """
        pass