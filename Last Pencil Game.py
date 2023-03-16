player_1 = 'John'
bot = 'Jack'
players = [player_1, bot]
pencils = 0
turn = ''
winner = ''


def bot_play(penc):

    if penc % 4 == 0:
        return 3
    elif penc % 4 == 3:
        return 2
    elif penc % 4 == 2:
        return 1

    return 1


while True:

    try:

        pencils = int(input('How many pencils would you like to use:\n'))

        # Validation if the pencils input:
        if pencils < 0:
            print('The number of pencils should be numeric')
            continue
        elif pencils == 0:
            print("The number of pencils should be positive")
            continue

        # Validation of the player names input:
        while True:

            turn = input('Who will be the first (John, Bot):\n')

            if turn not in players:
                print(f"Choose between {player_1} and {bot}")

            else:
                break

    except ValueError:
        print('The number of pencils should be numeric')

    while pencils > 0:

        print(pencils * '|')

        # Validation of withdrawn pencils:
        while True:

            if turn == player_1:
                taken_pencils = input(f"{turn}'s turn!\n")

                if taken_pencils not in '123':
                    print("Possible values: '1', '2' or '3'")

                elif int(taken_pencils) > pencils:
                    print("Too many pencils were taken")

                else:
                    break

            else:
                print(f"{bot}'s turn!")
                taken_pencils = bot_play(pencils)
                print(bot_play(pencils))
                break

        pencils -= int(taken_pencils)

        turn = player_1 if turn == bot else bot

        # Win condition:
        if pencils == 0:
            winner = bot if turn == bot else player_1
            print(f"{winner} won!")
            break

    if winner:
        break