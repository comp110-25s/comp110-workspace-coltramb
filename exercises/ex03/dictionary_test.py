"""Testing practice with dictionary funcutions."""

__author__: str = "730575668"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len

import pytest


def test_invert_use_case1():
    """Unique key-value pair test inversion."""
    assert invert({"a": "b", "c": "d"}) == ({"b": "a", "d": "c"})


def test_invert_use_case_2():
    """Single key value test inversion."""
    assert invert({"banana": "orange"}) == {"orange": "banana"}


def test_invert_edge_case():
    """Duplicate value test inversion, expecting a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use_case_1():
    """Multiple unique value appearance counting test."""
    assert count(["banana", "orange", "strawberry", "orange", "strawberry"]) == {
        "banana": 1,
        "orange": 2,
        "strawberry": 2,
    }


def test_count_use_case_2():
    """Test of single repeated element counting in list."""
    assert count(["bottle", "bottle", "bottle"]) == {"bottle": 3}


def test_count_edge_case():
    """An empty list test with the expected result of an empty dictionary."""
    assert count([]) == {}


def test_favorite_color_use_case_1():
    """Finding most common color in normal case test."""
    assert favorite_color({"Jeff": "blue", "Sarah": "green", "Fred": "blue"}) == "blue"


def test_favortie_color_use_case_2():
    """Finding most common color in unique scenario test"""
    assert favorite_color({"Jeff": "green", "Sarah": "red", "Fred": "blue"}) == "green"


def test_favorite_color_edge_case():
    """Tie for favorite color, first encourntered color expected to be the most popular test."""
    assert (
        favorite_color(
            {"Jeff": "red", "Sarah": "orange", "Fred": "red", "Jon": "orange"}
        )
        == "red"
    )


def test_bin_len_use_case_1():
    """Binning words with unique words by length test."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2():
    """Binning words with duplicate words by length test."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case():
    """Binning words with an empty list by length, with the expectation of an empty dictionary test."""
    assert bin_len([]) == {}
