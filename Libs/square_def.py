import copy

def display_grid(grid):
    # Display the 3x3 Display
    for i in range(3):
        print(grid[i])


class magic_square_state:
    def __init__(self, grid_start_state, parent=None):
        self.__grid_start_state = grid_start_state
        self.parent = parent
        self.successor_state = []
        self.sum_cols = []
        self.sum_rows = []
        self.available_numbers = []
        self.available_coordinates = []

    def get_start_state(self):
        return self.__grid_start_state

    def display_grid(self):
        # Display the 3x3 Display
        for i in range(3):
            print(self.__grid_start_state[i])

    def set_sum_rows(self):
        sum = 0
        return_list = []
        for i in range(3):
            for j in range(3):
                sum += self.__grid_start_state[i][j]
            return_list.append(sum)
            sum = 0
        self.sum_rows = return_list

    def set_sum_cols(self):
        sum = 0
        return_list = []
        for i in range(3):
            for j in range(3):
                sum += self.__grid_start_state[j][i]
            return_list.append(sum)
            sum = 0
        self.sum_cols = return_list

    def set_available_numbers(self):
        check_set = set()
        unused_numbers_list = []
        for i in range(3):
            for j in range(3):
                val = self.__grid_start_state[i][j]
                check_set.add(val)
        for i in range(9):
            index = i + 1
            if index not in check_set:
                unused_numbers_list.append(index)
        self.available_numbers = unused_numbers_list

    def set_available_coordinates(self):
        coordinates_list = []
        for i in range(3):
            for j in range(3):
                if self.__grid_start_state[i][j] == 0:
                    coordinate = (i, j)
                    coordinates_list.append(coordinate)
        self.available_coordinates = coordinates_list

    def run_initialization(self):
        self.set_sum_cols()
        self.set_sum_rows()
        self.set_available_numbers()
        self.set_available_coordinates()

    def display_information(self):
        self.display_grid()
        print("Sum of Colums:", self.sum_cols)
        print("Sum of Rows:", self.sum_rows)
        print("Available numbers: ", self.available_numbers)
        print("Available coordinates: ", self.available_coordinates)

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

    def get_successors(self):
        new_grid = copy.deepcopy(self.get_start_state())
        order = [2, 0, 1]
        possible_combinations = []
        aval_numbers = self.available_numbers
        for i in range(len(aval_numbers)):
            possible_combinations.append(aval_numbers)
            aval_numbers = [aval_numbers[i] for i in order]

        print("\nPossible Combinations: ", possible_combinations)

        for i in range(3):
            comb = possible_combinations[i]
            for j in range(3):
                coord = self.available_coordinates[j]
                x = int(coord[0])
                y = int(coord[1])
                new_grid[x][y] = comb[j]
            print("")
            self.display_information()
            var = copy.deepcopy(new_grid)
            self.successor_state.append(var)
            print(self.successor_state)

