import random
import sys
import string


_original_choices = random.choices


def mock_choices(population, k):
    if population == string.ascii_letters:
        return ['N', 'o', 'K', 'i', 'A'] # Fixed characters for letters
    elif population == string.digits:
        return ['2', '0', '2', '4'] # Fixed characters for digits
    elif population == string.punctuation:
        return ['?','.','@', '!'] # Fixed characters for punctuation


def mock_shuffle(items):
    return items 
random.choices = mock_choices
random.shuffle = mock_shuffle

import passgen


if __name__ == "__main__":
    passgen.main()
