import numpy as np

grid = np.full((10,10), False, dtype=bool)

example = 'turn on 0,0 through 3,3'

coords = example.split(' ')
if coords[0] == 'turn':
    coords[0:2] = [' '.join(coords[0:2])]

coords[1] = tuple(map(int, coords[1].split(',')))  # type: ignore
coords[-1] = tuple(map(int, coords[-1].split(',')))  # type: ignore

if coords[0] == 'turn on':
    start_col, start_row = coords[1]
    end_col, end_row = coords[-1]
    grid[start_row:end_row+1, start_col:end_col+1] = True

print(grid)
