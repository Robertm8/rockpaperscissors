import random  # imports module to take advantage of randint() function


def play():
    """
    Starts a new game and handles all game stats.
    """

    win_count = 0
    loss_count = 0
    tie_count = 0
    n = 0

    print("Welcome to the Rock/Paper/Scissors World Championship League.")
    print("You'll face off against ten opponents.")
    print("Your first challenger awaits.")

    rounds = int(input("Enter how many rounds you would like to play for: "))
    while n < rounds:
        for y in range(1, 4):  # Simple loop for creating some visual breaks between lines of text
            print(".")
        print("Choose Rock, Paper, or Scissors")
        choice = input()
        win_count, loss_count, tie_count, n = battle(choice, win_count, loss_count, tie_count, n)  # calls the main function

    print("Win percentage:", str(int(100 * (win_count / (win_count + loss_count + tie_count)) // 1)) + "%")  # Ending stats


def battle(choice, win_count, loss_count, tie_count, n):
    """"The main if/else chain to compare user choice with random opponent choice."""
    enemy = random.randint(1, 3)  # critical function for randomizing opponent choice. The 3 is INCLUSIVE.
    message = ""
    if choice == "Rock":
        if enemy == 1:
            print("Opponent chose Rock!")
            message = "tie"
        elif enemy == 2:
            print("Opponent chose Paper!")
            message = "loss"
        elif enemy == 3:
            print("Opponent chose Scissors!")
            message = "win"
    elif choice == "Paper":
        if enemy == 1:
            print("Opponent chose Rock!")
            message = "win"
        elif enemy == 2:
            print("Opponent chose Paper!")
            message = "tie"
        elif enemy == 3:
            print("Opponent chose Scissors!")
            message = "loss"
    elif choice == "Scissors":
        if enemy == 1:
            print("Opponent chose Rock!")
            message = "loss"
        elif enemy == 2:
            print("Opponent chose Paper!")
            message = "win"
        elif enemy == 3:
            print("Opponent chose Scissors!")
            message = "tie"
    else:                                               # Else case for a wrong input. Does not use up a turn.
        print("Invalid choice. Choose again!")

    win_count, loss_count, tie_count, n = result(message, win_count, loss_count, tie_count, n)

    return win_count, loss_count, tie_count, n


def result(m, win_count, loss_count, tie_count, n):
    if m == "tie":
        print("Tie!")
        tie_count += 1
        n += 1
    elif m == "loss":
        print("Loss!")
        loss_count += 1
        n += 1
    elif m == "win":
        print("Win!")
        win_count += 1
        n += 1

    announce(win_count, loss_count, tie_count)

    return win_count, loss_count, tie_count, n


def announce(win_count, loss_count, tie_count):
    """"Simple function that announces statistics."""
    print("Wins:", win_count, "Losses:", loss_count, "Ties:", tie_count)


play()
