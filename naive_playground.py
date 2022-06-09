from random import randint
from collections import namedtuple

Game = namedtuple('Game', ('game', 'title'))

def rock_paper_scissors():
    """Game 'Rock-Scissors-Paper'.
    ---
    Parameters:\n
    return: scores: float - Gamer`s result scores"""

    """Digitalize rules of the game"""
    WIN = 1
    WON = -1
    DRAW = 0
    
    STONE = 1
    SCISSORS = 2
    PAPER = 3
    
    actions = ('Noname', 'Stone', 'Scissors', 'Paper')
    
    """Scoring rules coding. May using list here is prefferable..."""
    scoring = dict([(STONE, dict([(STONE, DRAW), (SCISSORS, WIN),(PAPER, WON)])), 
                    (SCISSORS, dict([(STONE, WON), (SCISSORS, DRAW), (PAPER, WIN)])), 
                    (PAPER, dict([(STONE, WIN), (SCISSORS, WON), (PAPER, DRAW)]))])
    
    wins = 0
    while True:
        game_turns = int(input('Rounds number? '))
        if game_turns > 0:
            break
        else:
            print('Minimum round`s number is 1. Answer careful, please!')
            continue
        
            
    for turn in range(1, game_turns + 1):
        try:
            gamer_run = int(input(f"\nRound {turn}, your choice? (1 - Stone / 2 - Scissors / 3 - Paper): "))
            casino_run = randint(1, 3)

            print(f"Gamer`s choices: {actions[gamer_run]} - {actions[casino_run]}")
            scores = scoring[gamer_run][casino_run]
            """  'if' here just for output task"""
            if scores == WIN:
                wins += 1
                print('Congrats! You win')
            elif scores == WON:
                wins -= 1            
                print('Sorry, your opponent`s luck win.')
            else:
                print('Draw.')
        except:
            print('Forbidden choice. You won in this round, sorry!')
            wins -= 1
            
    return int(wins / game_turns * 100)


def guess_the_number(max_number:int = 5) -> float:
    """Game 'Guess the number'.
    ---
    Parameters:\n
    max_num: int - Maximum hidden number\n
    return: scores: float - Gamer`s result scores"""
    WIN_SHOW = '\n*** CONGRADULATION! BINGO! ***\n'
    attempts = 0
    attempts_record = []
    hidden_number = randint(1, max_number)

    while True:
        attempts += 1
        print(f"\nAttempt №{attempts}.")
        
        trying2guess = int(input(f"Which number (from 1 to {max_number}) shadowed? "))
        if trying2guess in attempts_record:
            print('Repited guessing. Enter another number!')
            attempts -= 1
            continue
        elif not trying2guess in range(1, max_number + 1):
            print('Illegal number (outborder)!')
            attempts -= 1
            continue            
        else:
            if trying2guess == hidden_number:
                print(WIN_SHOW)
                break
                
        attempts_record.append(trying2guess)
        
        end_of_game = input("Wrong.\nTry again? (Empty Enter - 'Yes', end of game - another input.): ")
        if end_of_game:
            print('\nOK not today... Don`t worry!')
            attempts = max_number + 1
            break
            
    return int((max_number - attempts + 1) / max_number * 100)


games = (Game(rock_paper_scissors, 'Rock-scuissors-paper'),
         Game(guess_the_number, 'Guess the number!'))

def mainMenu():
    """Main menu"""
    REQUEST_MESSAGE = '\nEnter game number (1-2 oe empty Enter for exit): '
    total_scores = 0

    while True:
        print(*[f"{idx + 1}: {game.title}" for idx, game in enumerate(games)], sep = '\n') 
        user_input = input(REQUEST_MESSAGE)
        if not user_input:
            print('<' * 3 + ' END OF GAMES ' + '>' * 3)
            break
        else:
            user_input = int(user_input)
            if not user_input in range(1, len(games) + 1):
                print(f"Absent game ({user_input}), try again, please!\n\n")
                continue
            else:
                game = games[user_input - 1]
                print(f"\nStart the '{game.title}'")
                scores = game.game()
                print(f"\nGame complete, your scores: {scores}")
                total_scores += scores
                print(f"Your total scores: {total_scores}\n{'='*10}\n\n")

    
print('\nLet`s play?\n')
mainMenu()
