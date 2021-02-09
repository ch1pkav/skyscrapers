"""
Module for checking skyscraper board

Github:
https://github.com/ch1pkav/skyscrapers
"""
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    skyscraper_file = open(path, "r")

    skyscraper_rows = [row[:-1] for row in skyscraper_file.readlines()]

    skyscraper_file.close()

    return skyscraper_rows



def left_to_right_check(input_line: str, pivot: str):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    if pivot=="*":
        return True

    pivot = int(pivot)
    skyscrapers = input_line[1:-1]

    highest = skyscrapers[0]
    visible = 1

    for skyscraper in skyscrapers:
        if skyscraper>highest:
            visible+=1
            highest = skyscraper

    if pivot==visible:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
        '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for row in board:
        if "?" in row:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique height, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for row in board[1:-1]:
        if len(set(row[1:-1])) != len(row[1:-1]):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    for row in board[1:-1]:
        left_visibility = left_to_right_check(row, row[0])
        right_visibility = left_to_right_check(row[::-1], row[-1])
        if not (right_visibility and left_visibility):
            return False

    return True

def flip_board(board: list):
    """
    Flips board for easier vertical checking.

    >>> flip_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    ['*44****', '*125342', '*23451*', '2413251', '154213*', '*35142*', '***5***']
    """
    dimensions = len(board[1])
    flipped_board = []

    for i in range(dimensions):

        row = ""
        for j in range(dimensions):
            row += board[j][i]

        flipped_board.append(row)

    return flipped_board


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    flipped_board = flip_board(board)
    if not (check_uniqueness_in_rows(flipped_board) and check_horizontal_visibility(flipped_board)):
        return False

    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)

    if not (check_not_finished_board(board) and check_horizontal_visibility(board) and check_columns(board) and check_uniqueness_in_rows(board)):
        return False

    return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))

