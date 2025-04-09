"""Practice with dictionary functions."""

__author__: str = "730575668"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Swaps keys and values to invert a given dictionary."""
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            raise KeyError("Inverted dictionary contains duplicate values!")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Will produce a dictionary where each key is a unique value in the given list and each value associated as the number of the times that value appread in the input list."""
    appearance_dict = {}
    for value in values:
        if value in appearance_dict:
            appearance_dict[value] += 1
        else:
            appearance_dict[value] = 1
    return appearance_dict


def favorite_color(color: dict[str, str]) -> str:
    """Using a dictionary of favorite colors associated with names, this will return the most frequently appearing color"; a tie will return the first color encountered."""
    color_count = count(list(color.values()))
    max_count = max(color_count.values())
    for color in color.values():
        if color_count[color] == max_count:
            return color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Will return dictionary with string lengths being keys and sets of words that length with be values given a list of strings."""
    dict_length = {}
    for word in words:
        length = len(word)
        if length in dict_length:
            dict_length[length].add(word)
        else:
            dict_length[length] = {word}
    return dict_length
