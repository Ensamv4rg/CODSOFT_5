from engine import game,check

number_of_rounds=int(input('How many rounds would you like to play?: '))
winner = game(number_of_rounds)
print(f'{check(winner)} Wins!')
