import random
import sys
import string

# Save the original randint function
_original_choices = random.choices
fixed_letters = list(string.ascii_letters)
fixed_digits = list(string.digits)
fixed_punctuation = list(string.punctuation)
# Override the randint function to return a fixed value
def _fixed_choices(population, k):
    if population == string.ascii_letters:
        return random.choices(fixed_letters, k=k)
    elif population == string.digits:
        return random.choices(fixed_digits, k=k)
    elif population == string.punctuation:
        return random.choices(fixed_punctuation, k=k)

random.choices = _fixed_choices

# Import the game script after overriding randint
import passgen

# Ensure the main function of guessnumber.py runs when guessnumber_testing.py is executed
if __name__ == "__main__":
    passgen.main()
