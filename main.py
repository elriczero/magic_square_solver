import square_def
from square_def import magic_square_node
from square_def import a_star_search

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # initialise empty 3 by 3 grid
    grid = []
    grid.append([8, 0, 0])
    grid.append([0, 0, 0])
    grid.append([0, 0, 0])

    initial_node = magic_square_node(grid)
    initial_node.run_initialization()
    initial_node.display_information()
    # initial_node.print_successors()


    # for i in range(len(initial_node.get_successors())):
    #     print("\nNew Node: ", i)
    #     ms_n = magic_square_node(initial_node.get_successors_states_grid(i),initial_node)
    #     ms_n.run_initialization()
    #     ms_n.display_information()
    #     ms_n.print_successors()

    a_star_search(initial_node)



