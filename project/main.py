# snake_water_gun.py
import random
import time

CHOICES = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
WIN_RULES = {
    ('s', 'w'): 'player',   # Snake drinks Water -> player wins
    ('w', 'g'): 'player',   # Water beats Gun -> player wins
    ('g', 's'): 'player'    # Gun beats Snake -> player wins
}
# If not in WIN_RULES but choices differ -> computer wins. If same -> tie.

def decide_winner(player, computer):
    if player == computer:
        return 'tie'
    return WIN_RULES.get((player, computer), 'computer')

def get_player_choice():
    while True:
        choice = input("Choose (s)nake, (w)ater or (g)un — or (q)uit: ").strip().lower()
        if choice == 'q':
            return 'q'
        if choice in CHOICES:
            return choice
        print("Invalid input. Use s / w / g or q to quit.")

def play_round():
    player = get_player_choice()
    if player == 'q':
        return None  # signal to quit
    computer = random.choice(list(CHOICES.keys()))
    result = decide_winner(player, computer)
    print(f"You chose: {CHOICES[player]}  |  Computer chose: {CHOICES[computer]}")
    if result == 'tie':
        print("Result: It's a tie!\n")
    elif result == 'player':
        print("Result: You win this round!\n")
    else:
        print("Result: Computer wins this round.\n")
    return result

def main():
    print("=== Snake Water Gun ===")
    print("Rules: Snake beats Water, Water beats Gun, Gun beats Snake.")
    rounds = 0
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (enter 0 to exit): "))
            if rounds < 0:
                print("Please enter 0 or a positive number.")
                continue
            if rounds == 0:
                print("Goodbye!")
                return
            break
        except ValueError:
            print("Please enter a valid integer.")

    scores = {'player': 0, 'computer': 0, 'tie': 0}
    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} of {rounds} ---")
        outcome = play_round()
        if outcome is None:  # player chose to quit early
            break
        scores[outcome] += 1
        # small pause for better UX
        time.sleep(0.4)

    print("\n=== Final Score ===")
    print(f"You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")
    if scores['player'] > scores['computer']:
        print("Overall: You win the match! 🎉")
    elif scores['player'] < scores['computer']:
        print("Overall: Computer wins the match. Better luck next time!")
    else:
        print("Overall: It's a draw! Well played.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()