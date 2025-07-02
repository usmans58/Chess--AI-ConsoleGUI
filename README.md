# Chess AI Console GUI

This is a console-based chess game with a simple graphical interface built using Python and Pygame. It includes an AI opponent powered by the Minimax algorithm.

## 🧠 Features

- Play against a friend locally or challenge the AI.
- AI uses a depth-limited Minimax algorithm to determine optimal moves.
- Legal move validation with check, checkmate, and stalemate detection.
- Undo last move functionality.
- Simple GUI built with `pygame` and chess piece images.

## 🗂️ Project Structure

```
Chess--AI-ConsoleGUI/
├── ChessMain.py          # Main file to run the game
├── ChessEngine.py        # Core chess logic and game state management
├── SmartMoveFinder.py    # AI logic using Minimax
├── images/               # Chess piece images
└── README.md             # Project documentation
```

## 🕹️ Controls

- Click on a piece to select it and click on the destination square to move.
- Press `z` to undo the last move.

## 🚀 Getting Started

### Requirements

- Python 3.x
- Pygame

### Installation

1. Clone the repository:

```bash
git clone https://github.com/usmans58/Chess--AI-ConsoleGUI.git
cd Chess--AI-ConsoleGUI
```

2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python ChessMain.py
```

## 🧠 AI Logic

The AI uses the **Minimax algorithm** with a simple board evaluation based on piece values. It searches future states up to a limited depth to choose the best move.

## 🔧 Possible Improvements

- Add castling, en passant, and draw by repetition support.
- Improve the evaluation function to account for position, mobility, and king safety.
- Add difficulty levels by varying AI search depth.
- Enhance GUI with animations and sound effects.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created by [Usman](https://github.com/usmans58)
