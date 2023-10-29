# Yahtzee Dice: Python Implementation

## Due Nov. 10, 2023
## Note, This assignement is equivalent to 2.5 other homework assignments. 

[GitHub Classroom Link](https://classroom.github.com/a/_GbvyVON)

## Objective

In this exercise, you will implement the logic for simulating dice rolls in a Yahtzee game. You will build upon Python's object-oriented programming features and advanced data structures to accomplish this.

You will build this package using best practices for Python package development using Pyscaffold. This will include adding docstring, type annotations - in the docstring, and unit tests to your code. You should achieve a code coverage of at least 80% for your unit tests. You could write this code on your own, but I assume that you will be much more effective working with ChatGPT as an assistant. 

## Rules of the Game of Yahtzee

Yahtzee is a dice game that combines elements of chance and strategy. Below are the detailed rules for playing Yahtzee:

### Components

- 5 six-sided dice
- A score sheet for each player to record scores
- A cup for shaking dice (optional)

### Objective

The objective of the game is to accumulate the highest score by rolling the five dice to make certain combinations, as outlined on the score sheet.

### Number of Players

The game can be played by one or more players. In multi-player settings, players take turns rolling the dice. Here, we will focus on implementing the single player version of the game.

### Turn Sequence

1. **Roll Dice**: At the beginning of each turn, the player rolls all five dice.
2. **Keep or Re-roll**: After the initial roll, the player can choose to keep some or all dice and re-roll the remaining ones. This can be done up to two more times (for a total of three rolls per turn).
3. **Scoring**: After the final roll, the player must choose a category on their score sheet to fill in with the score from that turn. Each category can only be used once.

### Scoring Categories

#### Upper Section

1. **Aces**: Sum of all aces rolled
2. **Twos**: Sum of all twos rolled
3. **Threes**: Sum of all threes rolled
4. **Fours**: Sum of all fours rolled
5. **Fives**: Sum of all fives rolled
6. **Sixes**: Sum of all sixes rolled

If a player scores at least 63 points in the upper section, they receive a bonus of 35 points.

#### Lower Section

1. **Three-of-a-Kind**: At least three dice showing the same face; scores the sum of those three dice.
2. **Four-of-a-Kind**: At least four dice showing the same face; scores the sum of those four dice.
3. **Full House**: A three-of-a-kind and a pair; scores a flat 25 points.
4. **Small Straight**: Four consecutive dice; scores a flat 30 points.
5. **Large Straight**: Five consecutive dice; scores a flat 40 points.
6. **Yahtzee**: All five dice showing the same face; scores a flat 50 points. Additional Yahtzees score a bonus.
7. **Chance**: Any combination; scores the sum of all five dice.

### End of the Game

The game ends when all players have filled in all categories on their score sheets.

### Winner

The player with the highest total score (upper section, lower section, and any bonuses) is the winner.

### Strategy

Players must balance between aiming for high-scoring categories and securing easier, lower-scoring categories to minimize the risk of being forced to take zero scores in later turns.

By understanding these rules and employing strategic decisions, players aim to achieve the highest score possible.

## Guide to Writing the Code

### File: `dice.py`

#### Requirements

- `random` library for generating random numbers
- `dataclasses` library for creating data classes
- `typing` library for type annotations

#### Code Structure

Your `dice.py` should include two classes:

1. `Dice`: Represents a single die with a customizable number of sides.
2. `YahtzeeDice`: Inherits from `Dice` and represents a set of dice in a Yahtzee game.

---

#### Instructions

##### Step 1: Import Required Libraries

First, import the required libraries at the beginning of your Python file.

```python
import random
from dataclasses import dataclass, field
from typing import List
```

##### Step 2: Create the `Dice` Class

Create a class named `Dice` using Python's `@dataclass` decorator.

###### Attributes

- `sides`: An integer that stores the number of sides on the dice (default should be 6).
- `current_value`: An integer that stores the current value shown by the dice. It should be initialized to `None` and should not be set during object creation (`init=False`).

###### Methods

- `roll`: A method that generates a random integer between 1 and `sides`, updates `current_value`, and returns it.

```python
@dataclass
class Dice:
    # Your code here
```

##### Step 3: Create the `YahtzeeDice` Class

Create another class named `YahtzeeDice` that inherits from `Dice`.

###### Attributes

- `num_dice`: An integer representing the number of dice in the set (default should be 5).
- `dice_set`: A list that will contain individual `Dice` objects. Initialize this attribute in the `__post_init__` method.

###### Methods

- `__post_init__`: Initializes the set of dice in `dice_set`.
- `roll_all`: Rolls all the dice in `dice_set` and returns a list of the rolled values.
- `get_values`: Returns a list containing the current values of all dice in `dice_set`.

```python
@dataclass
class YahtzeeDice(Dice):
    # Your code here
```

### File: `player.py`

#### Requirements

- Import classes from existing files: `Scoring`, `YahtzeeDice`
- Import function: `display_dice`

#### Code Structure

Your `player.py` file should include two classes:

1. `Player`: Manages a player's overall state in the Yahtzee game.
2. `PlayerTurn`: A nested class within `Player` that handles the logic for a single turn.

---

#### Instructions

##### Step 1: Import Required Libraries and Modules

First, import the required libraries and modules at the beginning of your Python file.

```python
from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice
```

##### Step 2: Create the `Player` Class

Create a class named `Player` that inherits from the `Scoring` class.

###### Attributes

- `name`: A string to store the player's name. Use `input()` to get this value during initialization.
- `score`: An integer to store the player's overall score (initially set to 0).

```python
class Player(Scoring):
    # Your code here
```

##### Step 3: Create the Nested `PlayerTurn` Class

Inside the `Player` class, create a nested class named `PlayerTurn`.

###### Attributes

- `yahtzee_dice`: An object of type `YahtzeeDice` to represent the dice set for the turn.
- `rolls_left`: An integer representing the number of rolls left in the turn (initially set to 3).
- `held_dice`: A list to store the indices of dice that are being held.

###### Methods

- `roll`: Rolls all dice not being held, updates their values, and decrements `rolls_left`.
- `hold`: Accepts a list of indices and updates `held_dice` to hold those dice.
- `get_state`: Returns a dictionary containing the current state of the turn (`dice_values`, `rolls_left`, `held_dice`).

```python
class PlayerTurn:
    # Your code here
```
---

### File: `scoring.py`

#### Requirements

- `collections` library for `Counter`

#### Code Structure

Your `scoring.py` file should include a single class:

1. `Scoring`: Manages the scoring for a Yahtzee game.

---

#### Instructions

##### Step 1: Import Required Libraries

Start by importing the required library.

```python
from collections import Counter
```

##### Step 2: Create the `Scoring` Class

Create a class named `Scoring`.

###### Attributes

- `score_card`: A dictionary to store the scores for each category.
- `all_categories`: A set containing all possible scoring categories.

###### Methods

- `calculate_score`: Given a category and dice values, calculates the score for that category.
- `mark_score`: Records a score for a given category in `score_card`.
- `get_score_card`: Returns the current `score_card`.
- `is_category_used`: Checks if a category has already been used.
- `remaining_categories`: Returns a list of remaining categories.
- `num_remaining_categories`: Returns the number of remaining categories.
- `num_used_categories`: Returns the number of used categories.
- `is_full`: Checks if the scorecard is full.
- `display_score_card`: Displays the scorecard in a user-friendly format in the terminal.

```python
class Scoring:
    # Your code here
```

##### Step 3: Implement Score Calculation Logic

Implement the `calculate_score` method using the following logic:

1. For single-number categories (aces, twos, etc.), the score is the sum of dice showing that number.
2. For "Three of a Kind" and "Four of a Kind," the score is the sum of the three/four dice showing the same number.
3. "Full House" scores the sum of all dice.
4. "Small Straight" and "Large Straight" score 25 and 30 points, respectively.
5. "Yahtzee" scores 50 points.
6. "Chance" scores the sum of all dice.

Use Python's `Counter` class to count occurrences of each die value.

### File: `display_dice.py`

#### Requirements

- `typing` library for type annotations

---

#### Instructions

##### Step 1: Import Required Libraries

First, import the required libraries at the beginning of your Python file.

```python
from typing import List, Dict
```

##### Step 2: Create the `display_dice` Function

Create a function named `display_dice` that takes two arguments:

1. `values` (List[int]): A list of integers representing the current face-up values of the dice.
2. `held_indices` (List[int], optional): A list of integers representing the indices of dice that are held. Default is an empty list.

###### Function Signature

```python
def display_dice(values: List[int], held_indices: List[int] = []):
    # Your code here
```

##### Step 3: Define ASCII Art for Dice Faces

Within the function, define a dictionary `dice_faces` that maps each die value to its ASCII art representation. The ASCII art should be a list of strings, each representing a row of the die face.

For example, for a die showing `1`, the ASCII representation might be:

```
["-----", "|   |", "| o |", "|   |", "-----"]
```

##### Step 4: Implement ANSI Color Coding

Use ANSI escape codes to change the color of the text for held dice. For instance, you can use `\033[92m` for green text and `\033[0m` to reset to the default color.

##### Step 5: Construct and Display the ASCII Art

Iterate over each die value and its index. Use the index to determine whether the die is held (and should therefore be colored). Append the appropriate lines to a list of strings, each representing a row of the display.

Finally, print each row to display the ASCII art.

### File: `play_yahtzee.py`

#### Requirements

- Import classes and functions from existing files: `Player`, `display_dice`

---

#### Instructions

##### Step 1: Import Required Classes and Functions

Import the required classes and functions at the beginning of your Python file.

```python
from player import Player
from display_dice import display_dice
```

##### Step 2: Create the `PlayYahtzee` Class

Create a class named `PlayYahtzee`.

###### Attributes

- `player`: An object of type `Player` that will manage the player's state throughout the game.

###### Methods

- `roll`: Initiates a dice roll and displays the results.
- `choose_category`: Allows the player to choose a scoring category.
- `start_new_turn`: Resets the game state for a new turn.
- `turn`: Manages a single turn in the game.
- `play_game`: The main game loop that calls other methods to progress the game.
- `generate_block_art`: Generates ASCII art for the game-over screen.
- `game_over`: Ends the game and displays the final score.

```python
class PlayYahtzee:
    # Your code here
```

##### Step 3: Implement the Game Logic

1. **roll**: Starts a new turn, displays the score card, rolls the dice, and displays the results.
2. **choose_category**: Prompts the player to choose a scoring category. Validates the category and updates the score.
3. **start_new_turn**: Initializes a new turn by creating a `PlayerTurn` object.
4. **turn**: Manages a single turn, handling actions like rolling, holding dice, and choosing a scoring category.
5. **play_game**: The main game loop that continues until the score card is full.
6. **generate_block_art**: Generates a block of ASCII art to congratulate the player at the end of the game.
7. **game_over**: Displays the final score and exits the game.

##### Step 4: Main Execution

Under the `__name__ == '__main__':` guard, instantiate the `PlayYahtzee` class and call its `play_game` method to start the game.

```python
if __name__ == '__main__':
    game = PlayYahtzee()
    game.play_game()
```

## Grading

### Overall Weightage

- This assignment is equivalent to 2.5 other homework assignments.

## Grading Categories

### Code Quality (30 points)

#### Readability (10 points)

- Code is well-organized and easy to read: 5 points
- Effective use of comments and docstrings: 5 points

#### Modularity (10 points)

- Code is effectively divided into functions/classes: 5 points
- Proper use of libraries and modules: 5 points

#### Best Practices (10 points)

- Follows PEP 8 guidelines: 5 points
- Use of idiomatic Python: 5 points

### Functionality (40 points)

#### `dice.py` (15 points)

- Implementation of `Dice` class: 5 points
- Implementation of `YahtzeeDice` class: 10 points

#### `player.py` (10 points)

- Implementation of `Player` and nested `PlayerTurn` classes: 10 points

#### `scoring.py` (10 points)

- Implementation of `Scoring` class: 10 points

#### `display_dice.py` (5 points)

- Proper ASCII art display and coloring: 5 points

### Unit Tests and Code Coverage (20 points)

- At least 80% code coverage: 10 points
- Test cases cover edge conditions: 10 points

### Documentation (10 points)

- Comprehensive README: 5 points
- Inline code documentation (type annotations and descriptive docstrings): 5 points

### Bonus Points

#### Advanced Features (up to 10 points)

- Additional features like multiplayer support, GUI, etc.