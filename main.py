import square_def
from square_def import magic_square_node


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # initialise empty 3 by 3 grid
    grid = []
    grid.append([8, 1, 0])
    grid.append([0, 5, 7])
    grid.append([4, 9, 0])

    m = magic_square_node(grid)
    m.run_initialization()
    m.display_information()
    m.print_successors()

    # print(type(m.get_successors()))
    # print(len(m.get_successors()))
    #
    # print(m.get_successors_states_grid(2))

    # for i in range(len(m.get_successors())):
    #     print("\nNew Node")
    #     ms_n = magic_square_node(m.get_successors_states_grid(i))
    #     ms_n.run_initialization()
    #     ms_n.display_information()
