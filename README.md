# Tetris Game README

## Overview
This project is a simple Tetris game implemented using Python and the Tkinter library. The game features various Tetris shapes, a grid system, and basic game mechanics such as moving and rotating shapes, clearing lines, and scoring. 

## Getting Started
### Prerequisites
- Python 3.x
- Tkinter library (usually included with standard Python installations)

### Running the Game
1. Ensure you have Python 3.x installed on your system.
2. Save the provided code in a Python file (e.g., `tetris.py`).
3. Open a terminal or command prompt and navigate to the directory containing the `tetris.py` file.
4. Run the game using the command:
   ```bash
   python tetris.py
   ```

### Controls
- **Left Arrow**: Move the shape left
- **Right Arrow**: Move the shape right
- **Down Arrow**: Move the shape down

## Code Structure
### Colors
- `BLACK`, `WHITE`, `GRAY`: Defined colors for the game elements.

### Grid Configuration
- `GRID_WIDTH`: Width of the grid (number of columns).
- `GRID_HEIGHT`: Height of the grid (number of rows).
- `BLOCK_SIZE`: Size of each block in the grid.

### Shape Classes
- `Shape`: Base class for all Tetris shapes. Includes methods for moving the shape down and sideways.
- `IShape`, `JShape`, `LShape`, `OShape`, `SShape`, `TShape`, `ZShape`: Derived classes representing the different Tetris shapes.

### TetrisGame Class
- Inherits from `tk.Tk` to create the main game window.
- Initializes the game window, grid, and current shape.
- Handles keyboard input for moving the shapes.
- Manages the game loop, updating the game state, and rendering the shapes on the canvas.

## Gameplay Mechanics
- The game starts with a random Tetris shape at the top of the grid.
- The shape can be moved left, right, or down using the arrow keys.
- When the shape reaches the bottom of the grid or collides with another shape, it becomes part of the grid.
- When a full line is formed, it is cleared, and the score is updated.
- A new random shape is generated, and the game continues.

## Scoring
- Lines are cleared when they are completely filled with blocks.
- The score is calculated based on the number of lines cleared at once.

## Customization
You can customize the game by:
- Changing the colors of the shapes and grid.
- Modifying the grid size and block size.
- Adjusting the speed of the game by changing the delay in the `update_game` method.

## Credits
This project was developed using the Tkinter library for the graphical interface and basic game mechanics.

Enjoy playing Tetris! 🎮
