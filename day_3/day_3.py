from copy import deepcopy

def get_num_trees(trajectory, move_right, move_down):
    # Don't want to edit the original input.
    trajectory = deepcopy(trajectory)
    total = 0
    x_index = 0
    y_index = 0
    rows = len(trajectory)
    cols = len(trajectory[0])
    # Continue until the current x index exceeds the number of row indices.
    while x_index < rows-1:
        x_index += move_down
        # Use mod to reset y position to be back within original trajectory map.
        y_index = (y_index + move_right) % cols
        if trajectory[x_index][y_index] == ".":
            trajectory[x_index][y_index] = "O"
        elif trajectory[x_index][y_index] == "#":
            trajectory[x_index][y_index] = "X"
            total += 1
    return total


if __name__ == "__main__":
    trajectory = [list(line.strip()) for line in open("input.txt")]
    print("Part 1:")
    print(get_num_trees(trajectory, 3, 1))
    print("Part 2:")
    total = 1
    total *= get_num_trees(trajectory, 1, 1)
    total *= get_num_trees(trajectory, 3, 1)
    total *= get_num_trees(trajectory, 5, 1)
    total *= get_num_trees(trajectory, 7, 1)
    total *= get_num_trees(trajectory, 1, 2)
    print(total)
