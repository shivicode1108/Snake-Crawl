Snake Crawl Game

This project implements a simple Snake Crawl game using the Turtle graphics library in Python. The game features a snake that moves around the screen, grows longer upon eating food, and terminates upon colliding with the game boundaries or itself.

Object-Oriented Programming Concepts
1. Classes and Objects
The code follows the fundamental concept of OOP by organizing functionality into classes. Key classes in the project include:

Snake Class (snake.py):

Manages the snake's behavior, movement, and growth.
Uses the Turtle class to create segments of the snake.
Incorporates methods for snake movement (up, down, left, right), extension (extend), and overall movement (move).
Food Class (food.py):

Represents the food that the snake consumes.
Inherits from the Turtle class and defines its appearance and behavior.
Contains a method (refresh) to relocate the food to a new random position upon being consumed.
Scoreboard Class (scoreboard.py):

Manages the game's scoring system.
Utilizes the Turtle class to display and update the player's score.
Contains methods to update the scoreboard (update_Scoreboard), increase the score (increase_score), and handle game over scenarios (game_over).
2. Encapsulation
The project encapsulates related functionality within each class, providing a clean separation of concerns. For example, the Snake class encapsulates all aspects of snake behavior, while the Food class encapsulates food-related functionalities.

3. Inheritance
The Food and Scoreboard classes demonstrate the use of inheritance. They inherit from the Turtle class to leverage its features while extending or customizing behavior.

4. Abstraction
Each class abstracts complex functionalities into simpler, reusable methods. This abstraction enhances code readability, maintainability, and flexibility.

5. Polymorphism
Polymorphism is illustrated through the use of common methods (update_Scoreboard) across different classes, enabling uniform handling of specific tasks.

Getting Started
Follow the steps below to run the Snake Crawl game:

Install Python on your machine if not already installed.
Clone the repository.
Run main.py using a Python interpreter.
Dependencies
Python 3.x
Turtle Graphics Library
