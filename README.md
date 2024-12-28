# Cole's Terminal Blackjack Game

Welcome to **Cole's Terminal Blackjack Game**! This is a fun, text-based blackjack game you can play right in your terminal. Test your luck and strategy as you compete against the dealer to see who can come closest to 21 without going over.

## Features

- **Classic Blackjack Rules**: Includes options for betting, splitting, doubling down, and taking insurance.
- **Realistic Dealer Logic**: Dealer stands on 17+ and hits below.
- **Chips Management**: Start with 1000 chips and see how long you can last!
- **Customizable Deck Handling**: The deck reshuffles when fewer than 30 cards remain.

## Requirements

- Python 3

## How to Install and Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/terminal-blackjack.git
   cd terminal-blackjack
   ```

2. **Install Dependencies**:
   This project does not have any external dependencies. Python itself is all you need!

3. **Run the Game**:
   Execute the following command in your terminal:

   ```bash
   python main.py
   ```

## How to Play

1. Follow the instructions displayed in the terminal.
2. Start with 1000 chips and place your bets wisely.
3. Decide whether to hit, stay, double down, or split based on your hand.
4. Try to beat the dealer without going over 21.
5. Play until you run out of chips or decide to quit.

## Project Structure

- `main.py`: Entry point for the game logic.
- `utils.py`: Contains utility functions for gameplay mechanics such as evaluating hands and resolving bets.
- `Deck` and `Card` classes (from `src`): Handle card drawing and deck management.

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.
