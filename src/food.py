# from src.grid.grid import BasicGrid
from src.grid.structure import GridStructure


class Food(GridStructure):
    """
        Manage a food on the grid.
    """

    def __init__(self, grid, cell, color: tuple, value: int):
        super().__init__(grid, [cell], color)

        self.value = value
        self.char_label = 'f'
