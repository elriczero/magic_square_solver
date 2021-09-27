# initialise empty 3 by 3 grid
grid = []
grid.append([8, 1, 0])
grid.append([0, 5, 7])
grid.append([4, 9, 0])


def display_grid(grid):
    for i in range(3):
        print(grid[i])


def sum_rows(grid):
    f_row = grid[0]
    s_row = grid[1]
    t_row = grid[2]
    sum_f_row = 0
    sum_s_row = 0
    sum_t_row = 0
    for i in f_row:
        sum_f_row += i
    for i in s_row:
        sum_s_row += i
    for i in t_row:
        sum_t_row += i
    sum_rows_list = [sum_f_row, sum_s_row, sum_t_row]
    return sum_rows_list

def sum_col(grid):
    for i in range(3):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_grid(grid)
    print(sum_rows(grid))
