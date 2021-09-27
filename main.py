# initialise empty 3 by 3 grid
grid = []
grid.append([8, 1, 0])
grid.append([0, 5, 7])
grid.append([4, 9, 0])


def display_grid(grid):
    for i in range(3):
        print(grid[i])


def sum_rows(grid):
    sum = 0
    return_list = []
    for i in range(3):
        for j in range(3):
            sum += grid[i][j]
        return_list.append(sum)
        sum = 0
    return return_list

def sum_col(grid):
    sum = 0
    return_list = []
    for i in range(3):
        for j in range(3):
            sum += grid[j][i]
        return_list.append(sum)
        sum = 0
    return return_list

def get_available_numbers(grid):
    check_set = set()
    unused_numbers_list = []
    for i in range(3):
        for j in range(3):
            val = grid[i][j]
            check_set.add(val)
    for i in range(9):
        index = i+1
        if index not in check_set:
            unused_numbers_list.append(index)
    return unused_numbers_list



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_grid(grid)
    print("")
    print(sum_rows(grid))
    print(sum_col(grid))
    print("")
    print(get_available_numbers(grid))
