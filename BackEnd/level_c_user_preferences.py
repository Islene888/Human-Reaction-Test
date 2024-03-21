

import tkinter as tk
import random
import time
import json


def read_user_settings():
    try:
        with open('user_settings.json', 'r') as file:
            settings = json.load(file)
            return settings
    except FileNotFoundError:
        print("Settings file not found. Please run user_setup.py to configure your settings.")
        exit()


user_settings = read_user_settings()
input_method = user_settings.get('input_method', 'buttons')

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan']
current_color = ''
attempts = []
total_attempts = 5


def show_text():
    global current_color
    canvas.delete("all")
    current_color = random.choice(colors)
    canvas.create_text(300, 200, text=current_color.upper(), fill=current_color, font=('Helvetica', 32))
    global start_time
    start_time = time.time()


def record_response(selected_color):
    global attempts
    end_time = time.time()
    elapsed_time = end_time - start_time
    correct = selected_color == current_color
    attempts.append((correct, elapsed_time))

    print(f"{'Correct' if correct else 'Incorrect'}! Reaction time: {elapsed_time:.3f} seconds")

    if len(attempts) == total_attempts:
        correct_responses = sum(1 for attempt in attempts if attempt[0])
        average_time = sum(attempt[1] for attempt in attempts) / total_attempts
        feedback_label.config(
            text=f"Accuracy: {correct_responses / total_attempts:.0%}, Average Time: {average_time:.3f} seconds")
        attempts = []  # Reset for the next set
    else:
        feedback_label.config(text="")

    show_text()


def setup_buttons():
    for color in colors:
        button = tk.Button(button_frame, text=color.upper(), command=lambda c=color: record_response(c))
        button.pack(side=tk.LEFT)


def setup_keyboard():
    def on_key(event):
        key_to_color = {'r': 'red', 'b': 'blue', 'g': 'green', 'y': 'yellow', 'p': 'purple', 'o': 'orange', 'c': 'cyan'}
        selected_color = key_to_color.get(event.char, None)
        if selected_color:
            record_response(selected_color)

    root.bind("<Key>", on_key)


root = tk.Tk()
root.title("Level C - Matching Text and Color")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack()

feedback_label = tk.Label(root, text="", font=('Helvetica', 16))
feedback_label.pack()

if input_method == 'buttons':
    setup_buttons()
elif input_method == 'keyboard':
    setup_keyboard()

show_text()
root.mainloop()
