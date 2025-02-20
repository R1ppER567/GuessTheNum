import os
import random
import msg_consts
from typing import Final

EX_CHAR: Final = "q"
NUM_RANGE: Final = (1, 10)  # [1, 10]
ATTEMPTS: Final = 5
YES_INPUT: Final = frozenset({"yes", "y", "1"})
NO_INPUT: Final = frozenset({"no", "n", "0"})


def clear() -> None:
    """Clears the console screen depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def get_user_guess() -> int:
    """Prompts the user to enter a number and validates the input.

    Returns:
        int: The user's guessed number.
    """
    while True:
        user_input = input(msg_consts.INPUT_MSG).strip()

        if user_input.isdigit():
            return int(user_input)
        print(msg_consts.DUMB_MSG)


def play_game() -> None:
    """Runs a single round of the game.

    A random number is generated, and the user has a limited number of
    attempts to guess it.
    """
    target_number = random.randint(*NUM_RANGE)

    for remaining_attempts in range(ATTEMPTS, 0, -1):
        print(msg_consts.GUESS_MSG.format(*NUM_RANGE))
        print(msg_consts.ATTEMPTS_MSG.format(remaining_attempts))

        user_guess = get_user_guess()
        if user_guess == target_number:
            clear()
            used_attempts = ATTEMPTS - remaining_attempts
            print(msg_consts.WIN_MSG.format(used_attempts))
            break

    clear()
    print(msg_consts.LOSE_MSG)


def play_again() -> bool:
    """Asks the user if he wants to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        user_input = input(msg_consts.PLAY_AGAIN_MSG).strip().lower()

        if user_input in YES_INPUT:
            return True
        if user_input in NO_INPUT:
            return False


def main() -> None:
    """Main game loop.

    Clears the screen, starts the game, and asks the user if they
    want to play again.
    """
    clear()

    while True:
        play_game()

        if not play_again():
            break

        clear()


if __name__ == "__main__":
    main()
