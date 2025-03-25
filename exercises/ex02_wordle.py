"""I am creating a Worlde code."""

__author__: str = "730575668"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(any_length: str, single_char: str) -> bool:
    """Searching for letters within the word."""
    # This code defines two variables, one a length of the unknown word, the other a search for a character within that word.
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    # It asserts that the character must be exactly 1 in length and if it is not, will debug the error and proceed to a while loop identifying if that charcter is contained at any index of the word.
    index = 0
    while index < len(any_length):
        if any_length[index] == single_char:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Codifies the guesses."""
    assert len(guess) == len(secret)
    # Emojified takes two parameters against each other, one being the user's guessed letter and the other the secret word, and asserts that the length of the guess must equal the length of the secret word.
    emoji_result = ""
    index = 0
    # This function then evaluates where in the word the user's guessed letter can be found.
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        index += 1
    return emoji_result


# If it is in the same index as the secret word, it will return a green box, the same letter but a different index, a yellow box, and a letter nowhere in the word, a white box.


def input_guess(expected_length: int) -> str:
    """Prompts user for guesses until provided expected length."""
    guess = input(f"Enter a {expected_length} character word.")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


# This function utilizes the length of the word to prompt the user to type a word that matches the number of characters it suggests.
# If the user does not match the number of characters in the word, it will ask them to try again, reiterating the word's length.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    max_turns = 6
    won = False
    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        # This loop allows the game to continue by running if the user has not won and has 6 or less turns remaining.
        if guess == secret:
            won = True
            print(f"You won in {turns}/{max_turns} turns!")
        turns += 1
    # This continues the loop by identifying if the user has guessed the word in under six turns. If not, it will return to the beginning of the loop with an additional turn added to the count.
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


# If the user does not win, it will identify the loss as an "X" and prompt for an attempt later.


if __name__ == "__main__":
    main(secret="houses")
# Allows the game to be played in the "Run" of its Trailhead.
