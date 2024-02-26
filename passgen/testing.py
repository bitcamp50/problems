import random
import sys
import string

# Save the original randint function
_original_randint = random.randint

# Override the randint function to return a fixed value
def _fixed_choices(population, k):
    if population == string.ascii_letters:
        return ['a', 'b', 'c']
    elif population == string.digits:
        return ['1', '2']
    elif population == string.punctuation:
        return ['@', '!']

random.choices = _fixed_choices

# Import the game script after overriding randint
import passgen

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    passgen.main()
