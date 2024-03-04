from enum import Enum


class Chessboard:
    def __init__(self, turn, figures=None, game_over=None):
        self.turn = turn   # FigureColor.WHITE
        self.figures = {1}
        self.game_over = False

    def new_game(self):
        self.figures = {
            'A1': {'color': FigureColor.WHITE, 'name': FigureName.ROOK},
            'B1': {'color': FigureColor.WHITE, 'name': FigureName.KNIGHT},
            'C1': {'color': FigureColor.WHITE, 'name': FigureName.BISHOP},
            'D1': {'color': FigureColor.WHITE, 'name': FigureName.QUEEN},
            'E1': {'color': FigureColor.WHITE, 'name': FigureName.KING},
            'F1': {'color': FigureColor.WHITE, 'name': FigureName.BISHOP},
            'G1': {'color': FigureColor.WHITE, 'name': FigureName.KNIGHT},
            'H1': {'color': FigureColor.WHITE, 'name': FigureName.ROOK},
            'A2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'B2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'C2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'D2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'E2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'F2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'G2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},
            'H2': {'color': FigureColor.WHITE, 'name': FigureName.PAWN},

            'A8': {'color': FigureColor.BLACK, 'name': FigureName.ROOK},
            'B8': {'color': FigureColor.BLACK, 'name': FigureName.KNIGHT},
            'C8': {'color': FigureColor.BLACK, 'name': FigureName.BISHOP},
            'D8': {'color': FigureColor.BLACK, 'name': FigureName.QUEEN},
            'E8': {'color': FigureColor.BLACK, 'name': FigureName.KING},
            'F8': {'color': FigureColor.BLACK, 'name': FigureName.BISHOP},
            'G8': {'color': FigureColor.BLACK, 'name': FigureName.KNIGHT},
            'H8': {'color': FigureColor.BLACK, 'name': FigureName.ROOK},
            'A7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'B7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'C7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'D7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'E7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'F7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'G7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
            'H7': {'color': FigureColor.BLACK, 'name': FigureName.PAWN},
        }
        self.turn = FigureColor.WHITE
        self.game_over = False
        print(f'A new game! Figures have been added')

    def surrender(self):
        self.game_over = True
        winner = FigureColor.WHITE if self.turn == FigureColor.BLACK else FigureColor.BLACK
        print(f"Game over: {self.game_over} | {winner} wins by surrender!")


class Figure:
    def __init__(self, color=None, name=None, start_cell=None, end_cell=None):
        self.color = color
        self.name = name
        self.start_cell = start_cell
        self.end_cell = end_cell

    def make_move(self, board):
        if self.is_valid_input_cells() and self.is_valid_move(board):
            del board.figures[self.start_cell]
            board.figures[self.end_cell] = {'color': self.color, 'name': self.name}
            print(f'[{self.start_cell} --> {self.end_cell}] The move was made')

    def pawn_move(self, board):
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print(f'Start: \n{self.start_cell} - {self.end_cell}')
        side_identify = 2

        # first move
        if board.turn == FigureColor.WHITE:
            first_move_points = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
            if self.start_cell in first_move_points:
                side_identify = 1
                pass
            else:
                print(f'Initial start_cell error for the {board.turn.name} player')
                return False
        elif board.turn == FigureColor.BLACK:
            first_move_points = ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7']
            if self.start_cell in first_move_points:
                side_identify = -1
                pass
            else:
                print(f'Initial start_cell error for the {board.turn.name} player')
                return False

        first_move_letter = str(self.start_cell[0])
        first_move_number = str(int(self.start_cell[1]) + (2 * side_identify))
        first_move = ''.join([first_move_letter, first_move_number])
        print(first_move)
        num_list = '12345678'

        # usual move
        end_cell_number = (num_list.index(self.end_cell[1]) + 1)
        print(end_cell_number)
        print(str((int(self.start_cell[1]) - 1) + (1 * side_identify)))
        usual_move_number = self.is_valid_cells_index(str((int(self.start_cell[1]) - 1) + (1 * side_identify)))
        usual_move = ''.join([str(self.start_cell)[0], str(usual_move_number)])
        print(usual_move)

        # attacks
        start_cell_letter_index = alpha_list.index(list(self.start_cell)[0])
        attack_letters = list([str(alpha_list[start_cell_letter_index - 1]), str(alpha_list[start_cell_letter_index + 1])])
        attack_numbers = list([str(int(self.start_cell[1]) + 1), str(int(self.start_cell[1]) - 1)])
        attack_list = [elem_1 + elem_2 for elem_1 in attack_letters for elem_2 in attack_numbers]

    def knight_move(self, board):
        l_list = 'ABCDEFGH'
        n_list = '12345678'
        print(self.start_cell)
        print(self.end_cell)

        letter_index = (l_list.index(str(self.start_cell[0])))
        number_index = (n_list.index(str(self.start_cell[1])))

        where_can_move_pattern = (-2, -2, -1, -1, 1, 1, 2, 2)
        where_can_move_dirty_indexes = []
        where_can_move_clear_indexes = []
        where_can_move_valid_values_l = []
        [where_can_move_dirty_indexes.append(letter_index + i) for i in where_can_move_pattern]
        [where_can_move_clear_indexes.append(i) for i in where_can_move_dirty_indexes if 0 <= int(i) <= 7]
        print([where_can_move_valid_values_l.append(l_list[i]) for i in where_can_move_clear_indexes])
        print(where_can_move_valid_values_l)
        print(f'end_cells_check: {where_can_move_dirty_indexes}')
        print(f'index: {letter_index}')

        where_can_move_pattern = (-1, 1, -2, 2, -2, 2, -1, 1)
        where_can_move_dirty_indexes = []
        where_can_move_clear_indexes = []
        where_can_move_valid_values_n = []
        [where_can_move_dirty_indexes.append(number_index + i) for i in where_can_move_pattern]
        [where_can_move_clear_indexes.append(i) for i in where_can_move_dirty_indexes if 0 <= int(i) <= 7]
        print([where_can_move_valid_values_n.append(n_list[i]) for i in where_can_move_clear_indexes])
        print(where_can_move_valid_values_n)
        print(f'end_cells_check: {where_can_move_dirty_indexes}')
        print(f'index: {letter_index}')

        where_can_move = []
        [where_can_move.append(i + j) for i, j in zip(where_can_move_valid_values_l, where_can_move_valid_values_n)]
        where_can_move_set = list(set(where_can_move))
        print(where_can_move_set)

    def is_valid_move(self, board):
        if self.end_cell in board.figures:
            print(f'Field [{self.end_cell}] is not available for the move, select another field')
            return False
        else:
            return True

    def is_valid_cells_index(self, cell):
        if 0 <= int(cell) <= 7:
            return cell
        else:
            print(f'Incorrect index of element: {cell}')
            return False

    def is_valid_input_cells(self):
        if not (self.start_cell[0] in "ABCDEFGH" and self.start_cell[1] in "12345678"):
            print(f'Start cell value is not correct')
            return False
        if not (self.end_cell[0] in "ABCDEFGH" and self.end_cell[1] in "12345678"):
            print(f'End cell value is not correct')
            return False
        else:
            return True

class FigureColor(Enum):
    WHITE = 1
    BLACK = 2


class FigureName(Enum):
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6



chessboard = Chessboard(FigureColor.BLACK)
chessboard.new_game()

figure = Figure(FigureColor.BLACK, FigureName.KING, 'A2', 'A3').make_move(chessboard)
# figure = Figure(FigureColor.BLACK, FigureName.PAWN, 'C7', 'E8').knight_move(chessboard)



