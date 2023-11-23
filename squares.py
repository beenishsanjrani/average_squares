from argparse import ArgumentParser

"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    total_weighted_squares = sum(weight * number**2 for number, weight in zip(list_of_numbers, effective_weights))

    total_weights = sum(effective_weights)

    average = total_weighted_squares / total_weights
    return average


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        tokens = s.split()
        first_token = tokens[0]
        if len(first_token) == 1 or (len(first_token) > 1 and not tokens[1:]):
            all_numbers.append(int(first_token))
    return all_numbers


if __name__ == "__main__":

    parser = ArgumentParser(description="So we can run it in the terminal")

    numbers_strings = ["1","2","4"]
    weight_strings = ["1","1","1"]        
    
    numbers = convert_numbers(numbers_strings)
    weights = convert_numbers(weight_strings)
    
    result = average_of_squares(numbers, weights)
    
    print(result)