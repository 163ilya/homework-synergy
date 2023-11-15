import random

def draw_board(board):
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i + 1], '|', board[i + 2], '|')

def is_cell_occupied(board, i):
    return board[int(i)] in ["X", "O"]

def get_player_move(board, symbol):
    i = input(f"Введите номер ячейки, в которую хотите поставить свой {symbol}")
    while (i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']) or is_cell_occupied(board, i):
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            i = input("Введите цифру от 0 до 8\n")
        elif is_cell_occupied(board, i):
            i = input("К сожалению, эта ячейка занята, выберите любую свободную\n")
    return int(i)

def get_computer_move(board, symbol):
    free_i = [i for i in range(len(board)) if board[i] not in ["X", "O"]]
    if not free_i:
        return None
    return random.choice(free_i)

def check_win(board, symbol):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            print(f"Победили {board[i]}")
            return True

    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6]:
            print(f"Победили {board[i]}")
            return True

    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        print(f"Победили {board[4]}")
        return True
    return False

def is_board_full(board):
    return all(cell in ["X", "O"] for cell in board)

def main():
    board = [str(i) for i in range(9)]
    computer_symbol = 'X'
    player_symbol = 'O'
    draw_board(board)
    while True:
        computer_i = get_computer_move(board, computer_symbol)
        if computer_i is None:
            print("Ничья! Игра завершена.")
            break
        board[computer_i] = computer_symbol
        print("Доска после хода компьютера")
        draw_board(board)
        if check_win(board, computer_symbol):
            break
        if is_board_full(board):
            print("Ничья! Игра завершена.")
            break
        player_i = get_player_move(board, player_symbol)
        board[player_i] = player_symbol
        print("Доска после хода игрока")
        draw_board(board)
        if check_win(board, player_symbol):
            break
        if is_board_full(board):
            print("Ничья! Игра завершена.")
            break

main()
