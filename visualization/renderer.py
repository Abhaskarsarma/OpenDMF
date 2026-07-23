from abc import ABC, abstractmethod


class Renderer(ABC):
    """
    Base class for all visualization engines.
    Every renderer should inherit from this class.
    """

    @abstractmethod
    def render(self, history):
        """
        Render the simulation history.
        """
        pass