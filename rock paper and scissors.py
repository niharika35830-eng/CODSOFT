import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose: rock, paper, or scissors")

    user = input("Your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user not in choices:
        print("Invalid choice!")
        continue

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score:")
    print("You =", user_score)
    print("Computer =", computer_score)

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
