import copy


def display_grid(grid):
    # Display the 3x3 Display
    for i in range(3):
        print(grid[i])


def node_backchain(end_node):
    return_path = []
    while end_node:
        new_grid = copy.deepcopy(end_node.get_start_state())
        return_path.append(new_grid)
        end_node = end_node.get_parent()
    return_path.reverse()
    return return_path


def a_star_search(starting_node, debugging_enabled=False):
    solution_found = False
    nodes_visited = 0
    open_set = []
    closed_set = []
    open_set.append(starting_node)

    while open_set:
        winner_index = 0
        winner_g_value = 90
        if len(open_set) > 1:
            for index in range(len(open_set)):
                if (open_set[index].get_h() < winner_g_value):
                    winner_g_value = open_set[index].get_h()
                    winner_index = index
            open_set_node = open_set.pop(winner_index)
        else:
            open_set_node = open_set.pop(winner_index)  # Start exploring Open Set Node

        # ENABLE_DEBUG
        if debugging_enabled and nodes_visited > 0:
            print("\nWinner node is: {:d}\n_________________________".format(winner_index))
            open_set_node.display_information()
        # ENABLE_DEBUG

        closed_set.append(open_set_node)  # Add the node to the closet set
        nodes_visited += 1
        # Check if Magic Square node is already completed
        if open_set_node.is_magic_square_completed() and open_set_node.is_valid_grid_sum():
            solution_found = True
            print("\n\nSolution was found at depth: ", nodes_visited)
            node_backchain_list = node_backchain(open_set_node)
            print("")
            # ENABLE BACKCHAIN PRINTING
            enable_backchain_print = False
            # enable_backchain_print = True
            if enable_backchain_print:
                for grid in node_backchain_list:
                    display_grid(grid)
                    print("")
            open_set_node.display_grid()
            stop_execution = input("Want to find more solutions?[Y/N]: ")
            # Check if stop_execution it's different from an empty string
            if stop_execution:
                # Check if contains no
                if str(stop_execution).lower().find('n') == 0:
                    return solution_found

        # ENABLE_DEBUG
        if debugging_enabled:
            print("\nChildren nodes are: \n__________________________")
        # ENABLE_DEBUG

        for i in range(len(open_set_node.get_successors())):
            if debugging_enabled:
                print("\nNew Node: ", i)
            initial_state = []
            parent = open_set_node
            initial_state = open_set_node.get_successors()
            ms_n = MagicSquareNode(initial_state[i], parent)
            ms_n.run_initialization()
            if debugging_enabled:
                ms_n.display_information()
            open_set.append(ms_n)
            # if debugging_enabled:
            #     ms_n.print_successors()
    print("No solution was found after {} nodes visited.".format(nodes_visited))
    return solution_found


class MagicSquareNode:
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

    def get_parent(self):
        return self.parent

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
                # test_node = MagicSquareNode(grid_copy)
                # test_node.run_initialization()
                self.successor_state.append(grid_copy)

    def get_successors(self):
        return self.successor_state

    def print_successors(self):
        print("\nSuccessor States are: ", len(self.successor_state))
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

    # Actual traveled distance or how far are we from out goal
    def set_g(self):
        self.g = sum(self.sum_rows) + sum(self.sum_cols)

    # Heuristics for the problem
    def set_h(self):
        self.h = 90 - self.g

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def is_magic_square_completed(self):
        result = True
        if self.g == 90 and len(self.available_numbers) == 0:
            return True
        else:
            return False

    def is_valid_grid_sum(self):
        is_valid_sum = True
        for sc in self.sum_cols:
            if sc < 15:
                is_valid_sum = False
        for sr in self.sum_rows:
            if sr < 15:
                is_valid_sum = False
        return is_valid_sum
