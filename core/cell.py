from core.cell_state import CellState


class Cell:

    """
    Represents one electrode on the DMF chip.
    """

    def __init__(self, row: int, col: int):

        self.row = row
        self.col = col
        self.state = CellState.EMPTY
        self.blocked = False
        self.droplet = None
        self.module = None

    def is_empty(self):

        return (
            self.state == CellState.EMPTY
            and
            self.droplet is None
        )