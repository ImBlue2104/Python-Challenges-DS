# Import required modules
import random   # For generating a random number
import time     # For adding short delays to the output

# Generate a random number between 1 and 100 for the player to guess
number = random.randint(1, 100)

# Function to introduce the game
def intro():
    print("May I ask for your name?")
    
    # Declare name as global so we can access it in other functions
    global name
    name = input()
    
    # Welcome message
    print(name + ", we are going to play a game called:\n Guess The Number!!!")
    print("I am thinking of a number from 1 to 100, and I want you to guess it in 5 tries!")

    # Provide a hint: whether the number is even or odd
    if number % 2 == 0:
        x = 'even'
    else:
        x = 'odd'
    print("To make your life easier, I'll give you a hint:\nThe number is {}".format(x))
    
    # Short pause before starting
    time.sleep(0.5)
    print("Go Ahead...")

# Function for the player to make guesses
def pick():
    Guesses_Taken = 0  # Track the number of guesses taken
    
    while Guesses_Taken < 6:  # Player gets up to 5 valid guesses
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)  # Convert input to integer

            # Check if guess is within valid range
            if 1 <= guess <= 100:
                Guesses_Taken += 1  # Count valid guess

                # Give feedback based on guess
                if guess < number:
                    print('Your guess is too low')
                elif guess > number:
                    print("Your guess is too high")
                else:
                    break  # Correct guess, exit loop

                # Encourage the player to try again
                time.sleep(0.5)
                print("Try Again")

            else:
                # Handle out-of-range guesses
                print("Silly Goose! The number isn't in range!")
                time.sleep(0.25)
                print("Please enter a valid number:")

        except:
            # Handle invalid (non-numeric) input
            print(f"I don't think that '{enter}' is a number!")

    # After the loop, check if player guessed correctly
    if guess == number:
        Guesses_Taken = str(Guesses_Taken)
        print(f'Good job {name}, you guessed the number in {Guesses_Taken} tries!')
    else:
        print("Nope, I was thinking of " + str(number))

# Main game loop to allow replaying
playagain = "yes"
while playagain.lower() in ['yes', 'y']:
    intro()
    pick()
    print("Do you want to play again:")
    playagain = input()
