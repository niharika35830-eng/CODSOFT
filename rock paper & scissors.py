import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose: r, p, or s")

    user = input("Your choice: ").lower()

    choices = ["r", "p", "s"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user not in choices:
        print("Invalid choice!")
        continue

    if user == computer:
        print("It's a Tie!")

    elif (user == "r" and computer == "s") or \
         (user == "p" and computer == "r") or \
         (user == "s" and computer == "p"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score:")
    print("You =", user_score)
    print("Computer =", computer_score)

    again = input("Play again? (y/n): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
