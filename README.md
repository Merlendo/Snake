# Snake Game

This is a simple implementation of the classic Snake game in Python. The game is played in the console window, and the player controls the snake's movement to eat apples and score points.

## How to Play

1. Run the Python script in a console or terminal window.
2. Use the arrow keys (`↑`, `↓`, `←`, `→`) to control the snake's direction.
3. The snake will continuously move in the chosen direction.
4. The objective is to eat apples (`X`) to increase your score (`Score: X`).
5. The game ends if the snake collides with itself or the game borders.

## Game Controls

- **↑ (Up arrow):** Change snake direction to up.
- **↓ (Down arrow):** Change snake direction to down.
- **← (Left arrow):** Change snake direction to left.
- **→ (Right arrow):** Change snake direction to right.

## Game Elements

- **@:** Snake head
- **O:** Snake body
- **X:** Apple

## Code Structure

- **WIDTH and HEIGHT:** Dimensions of the game screen.
- **init_screen(width, height):** Initialize the game screen.
- **draw_screen(screen, score):** Display the game screen and current score.
- **draw_snake(snake, screen):** Draw the snake on the screen.
- **draw_apple(apple, screen):** Draw the apple on the screen.
- **generate_apple(snake):** Generate a new apple position.
- **move_snake(snake, snake_direction, eating):** Move the snake in the current direction.
- **check_collision(snake, apple, score, eating, run):** Check for collisions with apples, itself, or the borders.
- **get_key():** Get the key pressed by the player.
- **Main Game Loop:** Continuously update the game state, handle input, and check for collisions.

## Dependencies

- The game uses the `msvcrt` module for keyboard input, which is specific to Windows. If running on a different platform, consider using alternative input methods.

## Acknowledgments

This Snake game implementation is a basic example and can be expanded with additional features, levels, or graphical interfaces. Feel free to modify and enhance the code according to your preferences. Have fun playing!
