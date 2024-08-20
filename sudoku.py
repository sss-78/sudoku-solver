sample_grid = [
    [None, 2, 8, 6, 7, 3, None, 5, None],
    [None, 6, 9, 8, None, None, None, None, 7],
    [None, None, None, None, None, 4, 2, 6, 8],
    [None, None, 6, 3, None, None, None, None, None],
    [2, 9, None, None, None, None, None, 1, 6],
    [None, None, None, None, None, 9, 5, None, None],
    [None, 3, 1, 2, None, None, None, None, None],
    [7, None, None, None, None, 6, 1, None, None],
    [None, 4, None, 9, None, 1, 8, None, None]
]

sample_grid_solved = [
    [4, 2, 8, 6, 7, 3, 9, 5, 1],
    [1, 6, 9, 8, 2, 5, 4, 3, 7],
    [5, 7, 3, 1, 9, 4, 2, 6, 8],
    [8, 5, 6, 3, 1, 2, 7, 9, 4],
    [2, 9, 7, 5, 4, 8, 3, 1, 6],
    [3, 1, 4, 7, 6, 9, 5, 8, 2],
    [9, 3, 1, 2, 8, 7, 6, 4, 5],
    [7, 8, 5, 4, 3, 6, 1, 2, 9],
    [6, 4, 2, 9, 5, 1, 8, 7, 3]
]


sudoku_grid = [
    [None, None, 5, 8, None, None, 1, 2, None],
    [8, 9, 2, None, None, 6, 7, None, None],
    [None, 4, 1, None, 3, 2, 6, None, None],
    [9, None, 8, None, None, 3, None, None, None],
    [2, None, None, None, 5, None, 9, 1, None],
    [None, 1, None, 7, None, None, None, 3, None],
    [None, None, None, None, None, None, None, None, None],
    [None, 6, None, None, None, 1, None, None, None],
    [1, None, 9, None, 8, None, None, None, 4],
]

sudoku_grid_solved = [
    [6, 3, 5, 8, 7, 4, 1, 2, 9],
    [8, 9, 2, 5, 1, 6, 7, 4, 3],
    [7, 4, 1, 9, 3, 2, 6, 5, 8],
    [9, 5, 8, 1, 6, 3, 4, 7, 2],
    [2, 7, 3, 4, 5, 8, 9, 1, 6],
    [4, 1, 6, 7, 2, 9, 8, 3, 5],
    [3, 8, 7, 6, 4, 5, 2, 9, 1],
    [5, 6, 4, 2, 9, 1, 3, 8, 7],
    [1, 2, 9, 3, 8, 7, 5, 6, 4]
]

test_grid = [[5,3,None,None,7,None,None,None,None],[6,None,None,1,9,5,None,None,None],[None,9,8,None,None,None,None,6,None],[8,None,None,None,6,None,None,None,3],[4,None,None,8,None,3,None,None,1],[7,None,None,None,2,None,None,None,6],[None,6,None,None,None,None,2,8,None],[None,None,None,4,1,9,None,None,5],[None,None,None,None,8,None,None,7,9]]

sub_squares_idx = [
    [
        [0, 2, 0, 2],
        [0, 2, 3, 5],
        [0, 2, 6, 8]
    ],
    [
        [3, 5, 0, 2],
        [3, 5, 3, 5],
        [3, 5, 6, 8],
    ],
    [
        [6, 8, 0, 2],
        [6, 8, 3, 5],
        [6, 8, 6, 8]
    ]
]

def validate_grid(grid):
    # 0 - if grid is proper, 1 - If grid is completed
    result = [False, False]
    empty_cells = 0
    '''
    no duplicates in each row/col
    every row, col - [1, 9] or unique
    every 3x3 subsquare must be unique
    1 -> x - [0, 2], y - [0, 2]
    2 -> x - [0, 2], y - [3, 5]
    3 -> x - [0, 2], y - [6, 8]

    4 -> x - [3, 5], y - [0, 2]
    5 -> x - [3, 5], y - [3, 5]
    6 -> x - [3, 5], y - [6, 8]

    7 -> x - [6, 8], y - [0, 2]
    8 -> x - [6, 8], y - [3, 5]
    9 -> x - [6, 8], y - [6, 8]
    '''

    for row in grid:
        row_cells = set()
        for cell in row:
            if cell and cell in row_cells:
                result[0] = False
                return result
            else:
                if cell:
                    row_cells.add(cell)
                else:
                    empty_cells += 1
    
    for col in range(len(grid)):
        col_cells = set()
        for cells in range(len(grid)):
            if grid[cells][col] and grid[cells][col] in col_cells:
                result[0] = False
                return result
            else:
                if grid[cells][col]:
                    col_cells.add(grid[cells][col])
    
    iter = 1
    row_start, row_end = 0, 2
    col_start, col_end = 0, 2

    while iter <= len(grid):
        sub_square_cells = set()

        for row in range(row_start, row_end+1):
            for col in range(col_start, col_end+1):
                if grid[row][col] and grid[row][col] in sub_square_cells:
                    result[0] = False
                    return result
                else:
                    if grid[row][col]:
                        sub_square_cells.add(grid[row][col])

        iter += 1

        if col_end == len(grid) - 1:
            row_start += 3
            row_end += 3
            col_start, col_end = 0, 2
        else:
            col_start += 3
            col_end += 3
    
    result[0] = True
    result[1] = (empty_cells == 0)
    
    return result

# print(validate_grid(sample_grid))
# print(validate_grid(sample_grid_solved))


def get_row_cells(grid, row):
    row_cells = set()
    for cell in grid[row]:
        if cell:
            row_cells.add(cell)
    return row_cells

def get_col_cells(grid, col):
    col_cells = set()
    for cell in range(len(grid)):
        if grid[cell][col]:
            col_cells.add(grid[cell][col])
    return col_cells

def get_subsquare_cells(grid, row, col):
    subsquare_cells = set()
    row_start, row_end, col_start, col_end = sub_squares_idx[row//3][col//3]

    for row in range(row_start, row_end+1):
            for col in range(col_start, col_end+1):
                if grid[row][col]:
                    subsquare_cells.add(grid[row][col])
    
    return subsquare_cells   

def solve_grid_helper(grid, val):
    current_grid = []

    for row in grid:
        current_row = []
        for cells in row:
            current_row.append(cells)
        current_grid.append(current_row)
    
    if validate_grid(current_grid)[1]:
        val.append(current_grid)

    for row in range(len(grid)):
        for col in range(len(grid)):
            if not grid[row][col]:
                possible_values = set([x+1 for x in range(len(grid))])
                current_cells = set()
                current_cells.update(get_row_cells(grid, row))
                current_cells.update(get_col_cells(grid, col))
                current_cells.update(get_subsquare_cells(grid, row, col))

                # possible values
                possible_values = possible_values.difference(current_cells)
        
                # try out possible values
                for value in possible_values:
                    grid[row][col] = value
                    if validate_grid(grid)[0]:
                        solve_grid_helper(grid, val)
                        grid[row][col] = None
                    else:
                        grid[row][col] = None
                
                return 

def print_grid(grid):
    result = ''
    for row in grid:
        for col in row:
            if not col:
                result += '0 '
            else:
                result += str(col) + ' '
        result += '\n'
    return result
        
def solve_grid(grid):
    states = []
    result = ''
    found = False

    solve_grid_helper(grid, states)

    if len(states) >= 1:
        found = True
        result += 'Here is the solution:\n'
        
        for st in states:
            result += print_grid(st) + '\n'

    if not found:
        result = 'There is no solution for this specific puzzle'
    
    return result

sample = []
for i in range(9):
    sub_sample = []
    for j in range(9):
        sub_sample.append(0)
    sample.append(sub_sample)

print(solve_grid(sample))
# print(solve_grid(sample_grid))
# print(solve_grid(test_grid))
    
    

def generate_grid():
    pass


