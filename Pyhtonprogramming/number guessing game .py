import random


def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter your choice (1/2/3): ")


    if choice == '1':
        return random.randint(1, 10),10
    elif choice == '2':
        return random.randint(1, 50),50
    elif choice == '3':
        return random.randint(1, 100),100
    else:
        print("Invalid choice. Defaulting to Easy mode (1-10).")
        return random.randint(1, 10),10
    
def play_game():
        secret , max_range = choose_difficulty()
        guess = None
        tries = 0

        while guess != secret:
            
            guess = int(input(f"Guess a number between 1 and {max_range}: "))
            tries += 1
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            elif guess == secret:
                print(f"Congratulations! You've guessed the number {secret} in {tries} tries.") 
            else:
                print("Invalid input. Please enter a valid number.")

while True:
    play_game()
    play_again = input("Do you want to play again?(yes/no): ")

    if play_again.lower() != 'yes':
                print("Thanks for playing,")
                break
    