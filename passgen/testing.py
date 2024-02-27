import random
import sys
import string

# Save the original randint function
_original_choices = random.choices
fixed_letters = list("hbO")
fixed_digits = list("23")
fixed_punctuation = list("<:")
# Override the randint function to return a fixed value
def _fixed_choices(population, k):
    if population == string.ascii_letters:
        return fixed_letters[:k]
    elif population == string.digits:
        return fixed_digits[:k]
    elif population == string.punctuation:
        return fixed_punctuation[:k]

random.choices = _fixed_choices

# Import the game script after overriding randint
import passgen

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    passgen.main()
