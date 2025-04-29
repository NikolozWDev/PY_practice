# rock paper scissors
import random

options = ['rock', 'paper', 'scissors']
wins = 0
looses = 0

is_running = True

while is_running:
    computer_move = random.choice(options)
    player_move = input('q tu quit (rock, paper, scissors): ')
    if player_move == 'q':
        is_running = False
    if player_move not in options:
        continue
    if player_move == computer_move:
        print(f'Tie')
        print(f'PC: {computer_move}, User: {player_move}')
        print(f'Scores: wins: {wins}, looses: {looses}')
    elif player_move == 'rock' and computer_move == 'scissors' or player_move == 'scissors' and computer_move == 'paper' or player_move == 'paper' and computer_move == 'rock':
        print(f'you win')
        print(f'PC: {computer_move}, User: {player_move}')
        wins += 1
        print(f'Scores: wins: {wins}, looses: {looses}')
    else:
        print(f'you loose')
        print(f'PC: {computer_move}, User: {player_move}')
        looses += 1
        print(f'Scores: wins: {wins}, looses: {looses}')
print('thanks for playing')