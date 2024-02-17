import random

print("Welcome To Cows and Bulls Game!")
print("Guess the 2-digit Secret Number")
print("-------------------------------")

def is_valid_guess(guess):
    return guess.isdigit() and len(guess) == 2

def play_game():
    secret_number = str(random.randint(10, 99))
    chances = 7

    while chances > 0:
        player_guess = input("Enter your 2-digit Guess Number: ")

        if not is_valid_guess(player_guess):
            print("Invalid input. Please enter a 2-digit number.")
            continue

        if secret_number == player_guess:
            print("*** Yes! You are Correct ***")
            print("*** Congratulations! You won the Game! ***")
            return "win"

        bulls = 0
        cows = 0

        for i in range(2):
            if player_guess[i] == secret_number[i]:
                bulls += 1
            elif player_guess[i] in secret_number:
                cows += 1

        print("Bulls - ", bulls)
        print("Cows - ", cows)

        chances -= 1
        print("Chances left:", chances)

        if chances == 0:
            print("*** You Lost! ***")
            print("*** The Secret Number was", secret_number, "***")
            return "lose"

    return "quit"

result = play_game()

if result == "lose" or result == "win":
    print("If you want to continue, press '0'; otherwise, press '1'.")
    option = input("Enter your Option : ")

    if option == '1':
        print("*** Better Luck Next time! ***")
    elif option != '0':
        print("Invalid Option")
    else:
        print("Game restarted...")
        play_game()
