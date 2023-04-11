import copy


def line(grid_start):
    grid_start = list(map(list, grid_start))
    switch = {
            'U': lambda i, j: (i - 1, j),
            'D': lambda i, j: (i + 1, j),
            'L': lambda i, j: (i, j - 1),
            'R': lambda i, j: (i, j + 1),
            }
    def find_way(start, end):
        nonlocal grid_start


        def cell(i, j):
            len_i = len(grid_start)
            len_j = len(grid_start[0])
            if 0 <= i <= len_i - 1 and 0 <= j <= len_j - 1:
                return True
            return False


        def can_move_to(i, j, direction, grid):
            i, j = switch[direction](i, j)
            if cell(i, j):
                if grid[i][j] == 'X':
                    return True
                elif grid[i][j] == '+' and can_turn_from(i, j, direction, grid):
                    return True
                elif grid[i][j] == '-' and direction in ('L', 'R'):
                    return True
                elif grid[i][j] == '|' and direction in ('U', 'D'):
                    return True
            return False


        def can_turn_from(i, j, direction, grid):
            if direction in ('L', 'R'):
                if (cell(i + 1, j) and grid[i + 1][j] != ' ') ^ (cell(i - 1, j) and grid[i - 1][j] != ' '):
                    return True
                return False
            elif direction in ('U', 'D'):
                if (cell(i, j - 1) and grid[i][j - 1] != ' ') ^ (cell(i, j + 1) and grid[i][j + 1] != ' '):
                    return True
                return False
            return False


        def way(i, j, direction, grid = None):
            if grid is None:
                nonlocal grid_start
                grid = copy.deepcopy(grid_start)

            if(i, j) == end and grid_empty(grid):
                return True
            elif can_move_to(i, j, direction, grid):
                grid[i][j] = ' '
                i, j = switch[direction](i, j)
                if grid[i][j] == '+':
                    if direction in ('L', 'R'):
                         return any((way(i, j, 'U', grid), way(i, j, 'D', grid)))
                    elif direction in ('D', 'U'):
                         return any((way(i, j, 'L', grid), way(i, j, 'R', grid)))
                return way(i, j, direction, grid)
            else:
                return False


        def check_start(i, j):
            ways = 0
            if cell(i + 1, j) and grid_start[i + 1][j] not in (' ', '-'): ways += 1
            if cell(i - 1, j) and grid_start[i - 1][j] not in (' ', '-') != ' ': ways += 1
            if cell(i, j + 1) and grid_start[i][j + 1] not in (' ', '|') != ' ': ways += 1
            if cell(i, j - 1) and grid_start[i][j - 1] not in (' ', '|') != ' ': ways += 1
            if ways > 1:
                return False
            return True

        def grid_empty(grid):
            if any(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] not in(' ', 'X')):
                return False
            else:
                return True


        i, j = start
        if check_start(i, j):
            return any((way(i, j, 'U'), way(i, j, 'D'), way(i, j, 'R'), way(i, j, 'L')))
        else:
            return False


    X1, X2 = find_x(grid_start)
    return any((find_way(X1, X2), find_way(X2, X1)))


def find_x(grid):
    IsFirstX = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                if IsFirstX:
                    X1 = (i, j)
                    IsFirstX = False
                else:
                    X2 = (i, j)
                    return (X1, X2)