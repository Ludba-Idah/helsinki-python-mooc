def who_won(game_board: list):
    player1_score = 0
    player2_score = 0
    
    for row in game_board:

        for square in row:
            if square == 1:
                player1_score += 1
            elif square == 2:
                player2_score += 1
        
    if player1_score > player2_score:
        return 1
    elif player2_score > player1_score:
        return 2
    else:
        return 0



if __name__ == "__main__":
    game_board = [
            [1, 0, 2],
            [1, 1, 0],
            [2, 0, 2]
        ]
    print(who_won(game_board))