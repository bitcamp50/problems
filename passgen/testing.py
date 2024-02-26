import random
import sys
import string

# Save the original randint function
_original_choices = random.choices
random.seed(42)
# Override the randint function to return a fixed value
def _fixed_choices(population, k):
    if population == string.ascii_letters:
        return list("<hbO")
    elif population == string.digits:
        return list("23")
    elif population == string.punctuation:
        return list(":!")

random.choices = _fixed_choices

# Import the game script after overriding randint
import passgen

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    passgen.main()
