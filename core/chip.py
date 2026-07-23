from core.cell import Cell
from core.cell_state import CellState
from core.move_status import MoveStatus
from core.statistics import Statistics


class Chip:

    """
    Represents the complete DMF chip.
    """

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols
        self.statistics = Statistics()
        self.grid = [
            [Cell(r, c) for c in range(cols)]
            for r in range(rows)
        ]

    # ------------------------------------------------

    def is_valid_cell(self, row, col):
        return (
            0 <= row < self.rows
            and
            0 <= col < self.cols
        )

    # ------------------------------------------------

    def block_cell(self, row, col):

        if self.is_valid_cell(row, col):
            cell = self.grid[row][col]
            cell.blocked = True
            cell.state = CellState.OBSTACLE

    # ------------------------------------------------

    def place_droplet(self, droplet):

        if not self.is_valid_cell(
            droplet.row,
            droplet.col
        ):

            raise ValueError("Invalid position.")

        cell = self.grid[droplet.row][droplet.col]

        if cell.blocked:
            raise ValueError("Blocked cell.")
        if cell.droplet is not None:
            raise ValueError("Occupied cell.")

        cell.droplet = droplet
        cell.state = CellState.OCCUPIED

    # ------------------------------------------------

    def move_droplet(

        self,
        droplet,
        new_row,
        new_col

    ):

        self.statistics.total_moves += 1

        if not self.is_valid_cell(new_row, new_col):
            self.statistics.out_of_bounds += 1
            return MoveStatus.OUT_OF_BOUNDS

        target = self.grid[new_row][new_col]

        if target.blocked:
            self.statistics.blocked_moves += 1
            return MoveStatus.BLOCKED

        if target.droplet is not None:
            self.statistics.collisions += 1
            return MoveStatus.COLLISION

        old = self.grid[droplet.row][droplet.col]
        old.droplet = None
        old.state = CellState.EMPTY
        droplet.move_to(new_row, new_col)
        target.droplet = droplet
        target.state = CellState.OCCUPIED
        self.statistics.successful_moves += 1
        self.statistics.total_distance += 1
        return MoveStatus.SUCCESS

    # ------------------------------------------------

    def render_console(self):

        print()
        print("=" * (self.cols * 4 + 1))

        for r in range(self.rows):

            line = "|"

            for c in range(self.cols):

                cell = self.grid[r][c]

                if cell.state == CellState.OBSTACLE:

                    symbol = " X "

                elif cell.droplet is not None:

                    symbol = f"D{cell.droplet.id}"

                    if len(symbol) == 2:

                        symbol += " "

                else:

                    symbol = " . "

                line += symbol + "|"

            print(line)

            print("-" * (self.cols * 4 + 1))