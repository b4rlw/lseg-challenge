# %%
import os
import numpy as np
from lseg_challenge.lightshow import LightGrid, LightGridUpgraded


grid_dims = (1000, 1000)
instr_filepath = os.path.join("data", "test_input.txt")


def test_valid_bounds():
    lg = LightGrid(grid_dims, instr_filepath)
    for _, bl_coord, tr_coord in lg.parse_instr():
        x1, y1 = bl_coord
        x2, y2 = tr_coord
        assert x2 <= x1
        assert y2 >= y1


def test_parse_instr():
    lg = LightGrid(grid_dims, instr_filepath)
    generator = lg.parse_instr()
    assert list(generator) == [
        ("turn on", (999, 0), (0, 999)),
        ("turn off", (500, 499), (499, 500)),
        ("toggle", (500, 0), (499, 999)),
    ]


def test_coord_conv():
    lg = LightGrid(grid_dims, instr_filepath)
    assert lg.coord_conv(*(0, 0)) == (999, 0)
    assert lg.coord_conv(*(999, 0)) == (999, 999)
    assert lg.coord_conv(*(0, 999)) == (0, 0)
    assert lg.coord_conv(*(999, 999)) == (0, 999)


def test_turn_on():
    part_1 = LightGrid((3, 3), instr_filepath)
    part_1.turn_on(*(2, 0), *(0, 2))
    assert np.array_equal(part_1.matrix, np.ones((3, 3)))

    part_2 = LightGridUpgraded((3, 3), instr_filepath)
    part_2.turn_on(*(2, 0), *(0, 2))
    part_2.turn_on(*(2, 0), *(0, 2))
    assert np.array_equal(part_2.matrix, 2 * np.ones((3, 3)))


def test_turn_off():
    part_1 = LightGrid((3, 3), instr_filepath)
    part_1.matrix = np.ones((3, 3))
    part_1.turn_off(*(2, 0), *(0, 2))
    assert np.array_equal(part_1.matrix, np.zeros((3, 3)))

    part_2 = LightGridUpgraded((3, 3), instr_filepath)
    part_2.matrix = np.array([[1, 2, 1], [2, 1, 2], [1, 2, 1]])
    part_2.turn_off(*(2, 0), *(0, 2))
    part_2.turn_off(*(2, 0), *(0, 2))
    assert np.array_equal(part_2.matrix, 2 * np.zeros((3, 3)))


def test_toggle():
    part_1 = LightGrid((3, 3), instr_filepath)
    part_1.matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    part_1.toggle(*(2, 0), *(0, 2))
    inverted = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    assert np.array_equal(part_1.matrix, inverted)

    part_2 = LightGridUpgraded((3, 3), instr_filepath)
    part_2.toggle(*(2, 0), *(0, 2))
    assert np.array_equal(part_2.matrix, 2 * np.ones((3, 3)))


def test_main():
    part_1 = LightGrid(grid_dims, instr_filepath)
    result_1 = part_1.main()
    assert result_1 == 998004

    part_2 = LightGridUpgraded(grid_dims, instr_filepath)
    result_2 = part_2.main()
    assert result_2 == 1003996


# %%
