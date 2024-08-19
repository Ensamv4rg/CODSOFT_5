def game(number_of_rounds=2):

    import random
    wins_to_end = int(number_of_rounds/2) + 1
    print(f'Game Starting. Best {wins_to_end} out of {number_of_rounds}')

    
    moves=['r','p','s']
    response_map = {'r':'p','p':'s','s':'r'} #Key=Move,Value= Move that beats it.
    output_map = {'r':'Rock','p':'Paper','s':'Scissors'}
    wins = {'bot':0,'player':0} #The first index is for the bot wins, second is for the player's wins.

    while number_of_rounds > 0:
        if wins['bot'] == wins_to_end or wins['player'] == wins_to_end:
            break

        bot_choice = random.choice(moves)
        player_choice = None

        while True:
            player_choice = input('Type in Rock,Paper,or Scissors to make a move').lower()
            if player_choice[0] not in moves:
                print( f'You entered and invalid input "{output_map[player_choice]}".Enter in Rock,Paper or Scissors' )
                continue
            break
        
        if bot_choice == response_map[player_choice]:

            wins['bot']+=1
            print(f"Bot played {output_map[bot_choice]}, you played {output_map[player_choice]}. Bot Wins this round!")

        elif player_choice == response_map[bot_choice]:

            wins['player']+=1
            print(f"Bot played {output_map[bot_choice]},you played {output_map[player_choice]}. You win this round!")

        else:
            print(f'Bot played {output_map[bot_choice]}, you played {output_map[player_choice]}. Tie')

        number_of_rounds -=1
    
    if wins['bot'] > wins['player']: return 'Bot'
    if wins['player'] > wins['bot']:return 'Player'
    return 'Tie'


def check(winner):

    if winner == 'Tie':

        print('Hmmm. There seems to be a tie')

        while True:

            response = input('Would you like to play a tie breaker round? (Y/N):')
            if response.lower()[0] not in ['y','n']:
                print('Invalid Response entered. Enter Y for Yes and N for No')
                continue

            elif response.lower()[0] == 'y':
                print('Starting Tie Breaker Round')
                tie_winner = game(3)
                return check(tie_winner)
            else:return 'No One'

            

    return winner