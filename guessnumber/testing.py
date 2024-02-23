import random
import sys

# Save the original randint function
_original_randint = random.randint

# Override the randint function to return a fixed value
def _fixed_randint(start, end):
    # You can adjust this value based on the testing scenario
    return 5

random.randint = _fixed_randint

# Import the game script after overriding randint
import guessnumber

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    guessnumber.main()
