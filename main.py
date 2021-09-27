import square_def
from square_def import magic_square_state


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # initialise empty 3 by 3 grid
    grid = []
    grid.append([8, 1, 0])
    grid.append([0, 5, 7])
    grid.append([4, 9, 0])

    m = magic_square_state(grid)
    m.run_initialization()
    m.display_information()
    m.print_successors()
