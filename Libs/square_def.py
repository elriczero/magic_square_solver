import copy


def display_grid(grid):
    # Display the 3x3 Display
    for i in range(3):
        print(grid[i])


def a_star_search(starting_node):
    open_set = []
    closed_set = []



class magic_square_node:
    def __init__(self, grid_start_state, parent=None):
        self.__numberOfRows = 3
        self.__numberOfCols = 3
        self.__grid_start_state = grid_start_state
        self.parent = parent
        self.successor_state = []
        self.sum_cols = []
        self.sum_rows = []
        self.available_numbers = []
        self.available_coordinates = []
        self.f = 0
        self.g = 0
        self.h = 0

    def get_start_state(self):
        return self.__grid_start_state

    def display_grid(self):
        # Display the 3x3 Display
        for i in range(3):
            print(self.__grid_start_state[i])

    def set_sum_rows(self):
        sum = 0
        return_list = []
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfCols):
                sum += self.__grid_start_state[x][y]
            return_list.append(sum)
            sum = 0
        self.sum_rows = return_list

    def set_sum_cols(self):
        sum = 0
        return_list = []
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfCols):
                sum += self.__grid_start_state[y][x]
            return_list.append(sum)
            sum = 0
        self.sum_cols = return_list

    def set_available_numbers(self):
        check_set = set()
        unused_numbers_list = []

        # Going through all the 3 x 3 table
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfCols):
                val = self.__grid_start_state[x][y]
                check_set.add(val)
        for index in range(1, 10):
            if index not in check_set:
                unused_numbers_list.append(index)
        self.available_numbers = unused_numbers_list

    def set_available_coordinates(self):
        coordinates_list = []
        for x in range(self.__numberOfRows):
            for y in range(self.__numberOfCols):
                if self.__grid_start_state[x][y] == 0:
                    coordinate = (x, y)
                    coordinates_list.append(coordinate)
        self.available_coordinates = coordinates_list

    def run_initialization(self):
        self.set_sum_cols()
        self.set_sum_rows()
        self.set_available_numbers()
        self.set_available_coordinates()
        self.set_successors()
        self.set_g()
        self.set_h()

    def display_information(self):
        self.display_grid()
        print("Sum of Colums:", self.sum_cols)
        print("Sum of Rows:", self.sum_rows)
        print("Available numbers: ", self.available_numbers)
        print("Available coordinates: ", self.available_coordinates)
        print("g is {:d} and h is {:d}".format(self.g, self.h))

    def set_successors(self):
        new_grid = copy.deepcopy(self.get_start_state())
        if (len(self.available_coordinates) != 0) and (len(self.available_numbers) != 0):
            coordinate = self.available_coordinates[0]
            for number in self.available_numbers:
                x = int(coordinate[0])
                y = int(coordinate[1])
                new_grid[x][y] = number
                # self.display_information()
                grid_copy = copy.deepcopy(new_grid)
                self.successor_state.append(grid_copy)

    def get_successors(self):
        return self.successor_state

    def print_successors(self):
        print("\nSuccessor States are:")
        for successor in self.successor_state:
            display_grid(successor)
            print("")

    def get_successors_states_grid(self, index):
        empty_list = []
        if len(self.successor_state) != 0:
            for successor in self.successor_state:
                empty_list.append(successor)
            return empty_list[index]
        return empty_list

    def set_g(self):
        self.g = sum(self.sum_rows) + sum(self.sum_cols)

    def set_h(self):
        self.h = 90 - self.g
