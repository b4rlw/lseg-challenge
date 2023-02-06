# %%
import re
from typing import Generator
import numpy as np


# %%
class LightGrid:
    def __init__(self, grid_dims: tuple, instr_filepath: str) -> None:
        self.grid_rows, self.grid_cols = grid_dims
        self.instr_filepath = instr_filepath
        self.matrix = np.zeros((self.grid_rows, self.grid_cols))

    def parse_instr(
        self,
    ) -> Generator[tuple[str, tuple[int, int], tuple[int, int]], None, None]:
        structure = r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)"
        with open(f"{self.instr_filepath}", "r", encoding="utf-8") as file:
            for line in file:
                string = line.strip()
                match = re.search(structure, string)
                if match:
                    operation = match.group(1)
                    bl_coord = self.coord_conv(*map(int, match.group(2).split(",")))
                    tr_coord = self.coord_conv(*map(int, match.group(3).split(",")))
                    yield operation, bl_coord, tr_coord

    def coord_conv(self, x: int, y: int) -> tuple[int, int]:
        new_origin = (0, self.grid_rows - 1)
        shifted_coord = np.array([x, y]) - np.array(new_origin)
        transformed_coord = np.array([[0, -1], [1, 0]]) @ shifted_coord
        return tuple(transformed_coord)

    def turn_on(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] = 1

    def turn_off(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] = 0

    def toggle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] = (
            1 - self.matrix[x2 : x1 + 1, y1 : y2 + 1]
        )

    def main(self) -> None:
        for operation, bl_coord, tr_coord in self.parse_instr():
            match operation:
                case "turn on":
                    self.turn_on(*bl_coord, *tr_coord)
                case "turn off":
                    self.turn_off(*bl_coord, *tr_coord)
                case "toggle":
                    self.toggle(*bl_coord, *tr_coord)
        return np.sum(self.matrix).astype(int)


class LightGridUpgraded(LightGrid):
    def turn_on(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] += 1

    def turn_off(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] -= 1
        self.matrix = np.maximum(self.matrix, 0)

    def toggle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.matrix[x2 : x1 + 1, y1 : y2 + 1] += 2
