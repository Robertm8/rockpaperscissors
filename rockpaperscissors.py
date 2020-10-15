import random #imports module to take advantage of randint() function


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

def result(m):
    """"Updates various global variables based on input from battle() function."""
    global tie_count, loss_count, win_count, n #critical to declare global variables or it will think they are local
    if m == "tie":
        print("Tie!")
        tie_count += 1
        n += 1
        announce()
    elif m == "loss":
        print("Loss!")
        loss_count += 1
        n += 1
        announce()
    elif m == "win":
        print ("Win!")
        win_count += 1
        n += 1
        announce()

def battle(choice):
    """"The main if/else chain to compare user choice with random opponent choice."""
    enemy = random.randint(1, 3) #critical function for randomizing opponent choice. The 3 is INCLUSIVE.
    if choice == "Rock":
        if enemy == 1:
            print("Opponent chose Rock!")
            result("tie")
        elif enemy == 2:
            print("Opponent chose Paper!")
            result("loss")
        elif enemy == 3:
            print("Opponent chose Scissors!")
            result("win")
    elif choice == "Paper":
        if enemy == 1:
            print("Opponent chose Rock!")
            result("win")
        elif enemy == 2:
            print("Opponent chose Paper!")
            result("tie")
        elif enemy == 3:
            print("Opponent chose Scissors!")
            result("loss")
    elif choice == "Scissors":
        if enemy == 1:
            print("Opponent chose Rock!")
            result("loss")
        elif enemy == 2:
            print("Opponent chose Paper!")
            result("win")
        elif enemy == 3:
            print("Opponent chose Scissors!")
            result("tie")
    else:                                               #Else case for a wrong input. Does not use up a turn.
        print("Invalid choice. Choose again!")

    win_count, loss_count, tie_count, n = result(message, win_count, loss_count, tie_count, n)

    return win_count, loss_count, tie_count, n


def announce(win_count, loss_count, tie_count):
    """"Simple function that announces statistics."""
    print("Wins:", win_count, "Losses:", loss_count, "Ties:", tie_count)


play()
