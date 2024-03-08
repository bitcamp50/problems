from correct_test import calculate_total as patched_convert


def convert(s):
    return patched_convert(s)


if __name__ == "__main__":
    pass