# Ace Analyzer

Ace Analyzer is a Python and Pygame blackjack prototype created by a two-person team for the T9 Hackathon. It deals cards and provides a basic graphical interface for playing a hand against a dealer.

## What it does

- Deals a new hand from a shuffled, two-deck shoe.
- Lets the player draw another card with **Hit**.
- Runs the dealer's turn and prints a win, loss, or push comparison in the terminal when **Stand** is clicked.
- Starts another hand when **Continue** is clicked.
- Uses **Q** to quit. The **S** key also runs the dealer's turn, but unlike the Stand button it does not print the hand comparison.

The interface also displays **Double** and **Split** buttons, but those actions are not implemented; clicking them only prints a message in the terminal.

## Run locally

You need Python and Pygame installed. From the repository root, install Pygame and start the application:

```sh
python -m pip install pygame
python card_game.py
```

Run it from the repository root because the game loads its card artwork from `images/playing_cards.bmp` using a relative path.

## Technology

- Python
- Pygame for the window, drawing, input, and sprite rendering
- Bitmap card artwork in `images/playing_cards.bmp`

There is no dependency manifest or automated test suite in the repository.

## Status and limitations

This is a hackathon proof of concept, not a complete blackjack trainer. It does not implement card counting, strategy recommendations, or betting. Double and Split are placeholders, and the current hand scoring incorrectly counts Twos as 10, so game results are not always reliable. The project was built in under 24 hours; these limitations describe the code as it stands rather than a roadmap or finished features.

## Hackathon notes and credits

For their first hackathon, the two team members were proud to learn Python and Pygame and build a working graphical proof of concept in under 24 hours. They also learned from testing the game and collaborating across multiple live versions during development.

Built by the two-person T9 Hackathon team.
