import os
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game board
def draw_board(paddle1_y, paddle2_y, ball_x, ball_y):
    # Clear the screen
    clear_screen()

    # Draw the game board
    for i in range(20):
        for j in range(50):
            if i == paddle1_y and j == 0:
                print('|', end='')
            elif i == paddle2_y and j == 49:
                print('|', end='')
            elif i == ball_y and j == ball_x:
                print('O', end='')
            else:
                print(' ', end='')
        print()

# Function to update the paddles' positions
def update_paddles(paddle1_y, paddle2_y, direction1, direction2):
    # Update the paddle positions based on the directions
    paddle1_y += direction1
    paddle2_y += direction2

    # Ensure the paddles do not go out of bounds
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y > 18:
        paddle1_y = 18
    
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y > 18:
        paddle2_y = 18
    
    return paddle1_y, paddle2_y

# Function to update the ball's position
def update_ball(ball_x, ball_y, ball_direction_x, ball_direction_y, paddle1_y, paddle2_y):
    # Update the ball's position
    ball_x += ball_direction_x
    ball_y += ball_direction_y

    # Reflect the ball if it hits a paddle
    if (ball_x == 1 and paddle1_y <= ball_y < paddle1_y + 2) or (ball_x == 48 and paddle2_y <= ball_y < paddle2_y + 2):
        ball_direction_x *= -1

    # Reflect the ball if it hits the top or bottom wall
    if ball_y == 0 or ball_y == 19:
        ball_direction_y *= -1
    
    return ball_x, ball_y, ball_direction_x, ball_direction_y

# Function to run the game
def run_game():
    # Initial game state
    paddle1_y = 9
    paddle2_y = 9
    ball_x = 24
    ball_y = 9
    ball_direction_x = 1
    ball_direction_y = 1

    # Game loop
    while True:
        # Draw the game board
        draw_board(paddle1_y, paddle2_y, ball_x, ball_y)

        # Get user input
        direction1 = 0
        direction2 = 0

        key = input("Use 'w' and 's' to control the left paddle, and 'i' and 'k' to control the right paddle: ")

        if key == 'w':
            direction1 = -1
        elif key == 's':
            direction1 = 1
        elif key == 'i':
            direction2 = -1
        elif key == 'k':
            direction2 = 1
        
        # Update the paddles' positions
        paddle1_y, paddle2_y = update_paddles(paddle1_y, paddle2_y, direction1, direction2)

        # Update the ball's position
        ball_x, ball_y, ball_direction_x, ball_direction_y = update_ball(ball_x, ball_y, ball_direction_x, ball_direction_y, paddle1_y, paddle2_y)

        # Delay for smooth gameplay
        time.sleep(0.1)

# Run the game
run_game()
ws
