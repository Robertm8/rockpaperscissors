import random #imports module to take advantage of randint() function

print("Welcome to the Rock/Paper/Scissors World Championship League.")
print("You'll face off against ten opponents.")
print("Your first challenger awaits.")

def announce():
    """"Simple function that announces statistics."""
    print("Wins:", win_count, "Losses:", loss_count, "Ties:", tie_count)

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
    if choice.lower() == "rock":
        if enemy == 1:
            print("Opponent chose Rock!")
            result("tie")
        elif enemy == 2:
            print("Opponent chose Paper!")
            result("loss")
        elif enemy == 3:
            print("Opponent chose Scissors!")
            result("win")
    elif choice.lower() == "paper":
        if enemy == 1:
            print("Opponent chose Rock!")
            result("win")
        elif enemy == 2:
            print("Opponent chose Paper!")
            result("tie")
        elif enemy == 3:
            print("Opponent chose Scissors!")
            result("loss")
    elif choice.lower() == "scissors":
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

win_count = 0
loss_count = 0
tie_count = 0
n = 1

while n < 11:
    for y in range(1, 4): #Simple loop for creating some visual breaks between lines of text
        print(".")
    print("Choose Rock, Paper, or Scissors")
    battle(input()) #calls the main function
print("Win percentage:", str(int(100 * (win_count / (win_count + loss_count + tie_count)))) + "%") #Ending stats
