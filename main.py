import square_def
from square_def import magic_square_state


# def display_grid(grid):
#     # Display the 3x3 Display
#     for i in range(3):
#         print(grid[i])
#
#
# def sum_rows(grid):
#     sum = 0
#     return_list = []
#     for i in range(3):
#         for j in range(3):
#             sum += grid[i][j]
#         return_list.append(sum)
#         sum = 0
#     return return_list
#
#
# def sum_col(grid):
#     sum = 0
#     return_list = []
#     for i in range(3):
#         for j in range(3):
#             sum += grid[j][i]
#         return_list.append(sum)
#         sum = 0
#     return return_list
#
#
# def get_available_numbers(grid):
#     check_set = set()
#     unused_numbers_list = []
#     for i in range(3):
#         for j in range(3):
#             val = grid[i][j]
#             check_set.add(val)
#     for i in range(9):
#         index = i + 1
#         if index not in check_set:
#             unused_numbers_list.append(index)
#     return unused_numbers_list
#
#
# def get_available_coordinates(grid):
#     coordinates_list = []
#     for i in range(3):
#         for j in range(3):
#             if grid[i][j] == 0:
#                 coordinate = (i, j)
#                 coordinates_list.append(coordinate)
#     return coordinates_list
#
#
# def get_successors(grid, available_coordinates, available_numbers):
#     order = [2, 0, 1]
#     possible_combinations = []
#     grid = grid
#     return_successor_list = []
#     for i in range(len(available_numbers)):
#         possible_combinations.append(available_numbers)
#         available_numbers = [available_numbers[i] for i in order]
#
#     print(possible_combinations)
#     # print("")
#     for no_comb in range(3):
#         print("")
#         an_comb = possible_combinations[no_comb]
#         for i in range(3):
#             coord = available_coordinates[i]
#             x = int(coord[0])
#             y = int(coord[1])
#             grid[x][y] = an_comb[i]
#             # print("")
#         display_grid(grid)
#         return_successor_list.append(grid)
#         # return_successor_list.append(new_grid)
#         # print("")
#     # return return_successor_list
#     return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # display_grid(grid)
    # print("")
    # print(sum_rows(grid))
    # print(sum_col(grid))
    # print("")
    # print(get_available_numbers(grid))
    # print("")
    # print(get_available_coordinates(grid))
    #
    # print(get_successors(grid, get_available_coordinates(grid), get_available_numbers(grid)))
    #
    # display_grid(grid)

    # initialise empty 3 by 3 grid
    grid = []
    grid.append([8, 1, 0])
    grid.append([0, 5, 7])
    grid.append([4, 9, 0])

    m = magic_square_state(grid)
    m.run_initialization()
    m.display_information()
    m.get_successors()
    print("")
