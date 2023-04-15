import random
import tkinter as tk

# Set up the game board
board = [[0 for j in range(4)] for i in range(4)]

# Create the game window
window = tk.Tk()
window.title("2048")

# Create the game canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Define the tile colors
colors = {
    0: "#CDC1B4",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

# Define the tile fonts
fonts = {
    0: ("Arial", 32),
    2: ("Arial", 32),
    4: ("Arial", 32),
    8: ("Arial", 32),
    16: ("Arial", 32),
    32: ("Arial", 32),
    64: ("Arial", 32),
    128: ("Arial", 28),
    256: ("Arial", 28),
    512: ("Arial", 28),
    1024: ("Arial", 24),
    2048: ("Arial", 24),
}

def draw_board():
    canvas.delete("all")
    for i in range(4):
        for j in range(4):
            x0 = j * 100 + 10
            y0 = i * 100 + 10
            x1 = (j + 1) * 100 - 10
            y1 = (i + 1) * 100 - 10
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[board[i][j]], outline="")

            if board[i][j] != 0:
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(board[i][j]), fill="black", font=fonts[board[i][j]])

def add_new_tile():
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    while board[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    board[i][j] = 2
import pickle

# Define the function to save the game state to a file

# Wait for user input and perform the corresponding action

def move_left():
    global board
    for i in range(4):
        for j in range(1, 4):
            if board[i][j] == 0:
                continue
            k = j
            while k > 0 and board[i][k-1] == 0:
                k -= 1
            if k > 0 and board[i][k-1] == board[i][j]:
                board[i][k-1] *= 2
                board[i][j] = 0
            elif k < j:
                board[i][k] = board[i][j]
                board[i][j] = 0


def move_right():
    global board
    for i in range(4):
        for j in range(2, -1, -1):
            if board[i][j] == 0:
                continue
            k = j
            while k < 3 and board[i][k+1] == 0:
                k += 1
            if k < 3 and board[i][k+1] == board[i][j]:
                board[i][k+1] *= 2
                board[i][j] = 0
            elif k > j:
                board[i][k] = board[i][j]
                board[i][j] = 0


def move_up():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                continue
            k = i
            while k > 0 and board[k-1][j] == 0:
                k -= 1
            if k > 0 and board[k-1][j] == board[i][j]:
                board[k-1][j] *= 2
                board[i][j] = 0
            elif k < i:
                board[k][j] = board[i][j]
                board[i][j] = 0

def move_down():
    global board
    for j in range(4):
        for i in range(2, -1, -1):
            if board[i][j] == 0:
                continue
            k = i
            while k < 3 and board[k+1][j] == 0:
                k += 1
            if k < 3 and board[k+1][j] == board[i][j]:
                board[k+1][j] *= 2
                board[i][j] = 0
            elif k > i:
                board[k][j] = board[i][j]
                board[i][j] = 0


def game_over():
    global board
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
    # If the game is over, display "Game Over" on the board
    canvas.create_text(200, 200, text="Game Over", font=("Arial", 32), fill="white")
    return True

def key_pressed(event):
    if event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()
    draw_board()
    if game_over():
        game_over()
    else:
        add_new_tile()

# Bind the key press event
canvas.bind("<Key>", key_pressed)
canvas.focus_set()

# Add two initial tiles
add_new_tile()
add_new_tile()


# Draw the initial board
draw_board()

# Start the game
window.mainloop()