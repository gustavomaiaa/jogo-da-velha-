import numpy as np

# tabuleiro
def print_board(board):
    symbols = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        print('|'.join([symbols[cell] for cell in row]))
        print('-' * 5)

def check_winner(board):
    for row in board:
        if abs(sum(row)) == 3:
            return np.sign(sum(row))
    for col in board.T:
        if abs(sum(col)) == 3:
            return np.sign(sum(col))
    if abs(np.sum(np.diag(board))) == 3:
        return np.sign(np.sum(np.diag(board)))
    if abs(np.sum(np.diag(np.fliplr(board)))) == 3:
        return np.sign(np.sum(np.diag(np.fliplr(board))))
    return 0


def is_full(board):
    return not (board == 0).any()

# utilizando algoritmo minimax p/ IA conseguir realizar a leitura do jogo e encontrara a melhor jogada
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner != 0:
        return winner * (10 - depth)
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = 1
                    score = minimax(board, depth + 1, False)
                    board[i, j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = -1
                    score = minimax(board, depth + 1, True)
                    board[i, j] = 0
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
                board[i, j] = 1
                score = minimax(board, 0, False)
                board[i, j] = 0
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = np.zeros((3, 3), dtype=int)
    print("Jogo da Velha - IA vs. Jogador")
    while True:
        print_board(board)
        if check_winner(board) != 0 or is_full(board):
            break
        
        while True:
            try:
                row, col = map(int, input("Digite linha e coluna (0-2): ").split())
                if board[row, col] == 0:
                    board[row, col] = -1
                    break
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente.")
        
        if check_winner(board) != 0 or is_full(board):
            break
        

        move = best_move(board)
        if move:
            board[move] = 1
    
    print_board(board)
    winner = check_winner(board)
    if winner == 1:
        print("A IA venceu!")
    elif winner == -1:
        print("Você venceu!")
    else:
        print("Empate!")

if __name__ == "__main__":
    play_game()
