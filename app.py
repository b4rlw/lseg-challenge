import os
from lseg_challenge.lightshow import LightGrid, LightGridUpgraded


if __name__ == "__main__":
    grid_dims = (1000, 1000)
    instr_filepath = os.path.join("data", "coding_challenge_input.txt")

    part_1 = LightGrid(grid_dims, instr_filepath)
    result_1 = part_1.main()
    print(f"Part 1 result: {result_1}")

    part_2 = LightGridUpgraded(grid_dims, instr_filepath)
    result_2 = part_2.main()
    print(f"Part 2 result: {result_2}")
