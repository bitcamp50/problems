import random
import sys

# Save the original randint function
_original_randint = random.choice

# Override the randint function to return a fixed value
def _fixed_choice(seq):
    # You can adjust this value based on the testing scenario
    return "Yes"

random.choice = _fixed_choice

# Import the game script after overriding randint
import magicball

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    magicball.main()
