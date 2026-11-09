# Ace Analyzer

Ace Analyzer is a Python/Pygame blackjack prototype created for the T9 Hackathon. It provides a graphical table for playing hands against a dealer. Although the original idea was to help people learn card counting, the current game does not track or teach card counting.

## What works today

- Starts a round with a player hand and a dealer hand, each dealt two cards from a shuffled two-deck shoe.
- Shows the dealer's first card and hides the other until the dealer plays.
- Lets the player hit, stand, and start another round with the on-screen controls.
- On stand, plays the dealer's hand until it reaches 17, then compares hand values and prints the outcome in the terminal.

The hand-value code attempts to score Aces as 1 or 11 and face cards as 10. This is an early prototype, and its scoring and round behavior have known gaps (see [Limitations](#limitations)).

## Run locally

You need Python, Pygame, and a desktop environment that can open a Pygame window. Run these commands from the repository root; the game loads its card artwork using a relative path.

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install Pygame and start the game:

```bash
python -m pip install pygame
python card_game.py
```

There is no dependency manifest or automated test suite in the repository; Pygame is the external runtime dependency.

## Controls

| Input | Current behavior |
| --- | --- |
| **Hit** | Deal one card to the player's hand. |
| **Stand** | Play the dealer's hand and print the result to the terminal. |
| **Continue** | Deal another round. |
| **S** | Play the dealer's hand, but does not print a round result. |
| **Q** | Quit. |
| **Double / Split buttons** | Displayed in the interface but not implemented as playable actions. |

## Technology

- Python
- Pygame for the desktop interface, drawing, events, and image loading
- Bitmap assets in `images/` for the table background and playing cards

## Limitations and status

This is a hackathon proof of concept, not a finished blackjack or card-counting trainer. Card counting, strategy recommendations, betting, and in-game instructions are not implemented. Results appear in the terminal rather than in the game window. The Double and Split buttons are placeholders, and the scoring currently treats a Two as 10; deck exhaustion and other blackjack edge cases are also not handled robustly. Use it as an example of an early Pygame project, not as a reliable rules implementation.

Built by a two-member team during their first hackathon, the project was an opportunity to learn Python and Pygame while producing a playable starting point.
