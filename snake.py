# -*- coding: utf-8 -*-
import os
import time
import msvcrt
import random


# Screen informations
WIDTH = 15
HEIGHT = 10

# Initialize the screen
def init_screen(width, height):
    return [["." for _ in range(width)] for _ in range(height)]

# Draw the screen
def draw_screen(screen, score):
    os.system("cls")
    print(f"Score : {score}")
    for row in screen:
        print("".join(row))
    print()

# Draw the snake
def draw_snake(snake, screen):
    for pos in snake:
        row, col = pos
        screen[row][col] = "@" if pos == snake[0] else "O"
    return screen
 
# Draw the apple
def draw_apple(apple, screen):
    row, col = apple
    screen[row][col] = "X"
    return screen
    
# Generate the apple
def generate_apple(snake):
    row = random.randint(0, HEIGHT - 1)
    col = random.randint(0, WIDTH - 1)
    
    #Ckeck if the apple pos is not in the snake
    while (row, col) in snake:
        row = random.randint(0, HEIGHT - 1)
        col = random.randint(0, WIDTH - 1)
    return (row, col)
    
# Move the snake
def move_snake(snake, snake_direction, eating):
    head = snake[0]
    if snake_direction == "left":
        head = (head[0], head[1] - 1)
    if snake_direction == "right":
        head = (head[0], head[1] + 1)
    if snake_direction == "up":
        head = (head[0] - 1, head[1])
    if snake_direction == "down":
        head = (head[0] + 1, head[1])
    
    snake.insert(0, head)
    
    # Ckeck if the snake is eating an apple
    if not eating:
        snake.pop()
    eating = False

    return snake, eating  
 
# Manage the collision with the snake
def check_collision(snake, apple, score, eating, run):

    # Collision with apple
    if snake[0] == apple:
        eating = True
        score += 1
        apple = generate_apple(snake)
        
    # Collision with itself
    if snake[0] in snake[1:]:
        run = False
        print("collision avec le serpent")
    
    # Collision with the borders
    if snake[0][1] < 0 or snake[0][1] >= WIDTH or snake[0][0] < 0 or snake[0][0] >= HEIGHT:
        run = False
        print("collision avec le mur")
        
    return snake, apple, score, eating, run
        
# Get the key pressed
def get_key():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\xe0': # This line stop the lag between input
            key = msvcrt.getch()
        return key


snake = [(HEIGHT//2-1, WIDTH//2-1), (HEIGHT//2-1, WIDTH//2), (HEIGHT//2-1, WIDTH//2+1)]
snake_direction = "left"
apple = generate_apple(snake)
score = 0
eating = False

run = True
while run:
    # Get the key pressed
    key = get_key()
    
    # Change the direction of the snake according to the key pressed
    if key == b'M' and snake_direction != "left":
        snake_direction = "right"
    if key == b'K' and snake_direction != "right":
        snake_direction = "left"
    if key == b'H' and snake_direction != "down":
        snake_direction = "up"
    if key == b'P' and snake_direction != "up":
        snake_direction = "down"
    
    # Main game
    screen = init_screen(WIDTH, HEIGHT)
    screen = draw_snake(snake, screen)
    screen = draw_apple(apple, screen)
    draw_screen(screen, score)
    snake, eating = move_snake(snake, snake_direction, eating)
    snake, apple, score, eating, run = check_collision(snake, apple, score, eating, run)
    
    # Sleep to give time for the player to play
    time.sleep(0.25)

print("Game Over")

    
