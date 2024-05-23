import tkinter as tk
from tkinter import Canvas
from itertools import cycle
import random
import math
from sine_values import calc_sin_values
from tan_values import calc_tan_values
from cos_values import calc_cos_values

class Ball:
    def __init__(self, cos=None, sin=None, tan=None, parent=None, canvas=None, start_x=10, start_y=10):
        self.canvas = canvas
        self.parent = parent
        self.canvas.config(width=800, height=600)  # Set canvas dimensions
        self.id = canvas.create_oval(start_x, start_y, start_x + 100, start_y + 100, outline="black", fill="red", width=4)
        self.x = start_x
        self.y = start_y
        self.move_speed = random.randint(10, 20)
        self.direction = 1  # 1 for forward, -1 for backward
        
        if cos:
            self.trigs = cycle(calc_cos_values())
        elif sin:
            self.trigs = cycle(calc_sin_values())
        else:
            self.trigs = cycle(calc_tan_values())
        
        self.animate()

    def move(self, dx, dy):
        self.canvas.move(self.id, dx, dy)
        self.x += dx
        self.y += dy

    def animate(self):
        dy = next(self.trigs)  # Adjusted multiplier for smoother movement
        dx = (self.move_speed * self.direction)

        # Get the current position of the ball
        coords = self.canvas.coords(self.id)
        print(coords)
        ball_left, ball_top, ball_right, ball_bottom = coords

        # Check for collision with canvas boundaries
        if ball_bottom + dy >= self.canvas.winfo_height() or ball_top + dy <= 0:
            dy = -dy  # Reverse vertical direction

        if ball_right + dx >= self.canvas.winfo_width() or ball_left + dx <= 0:
            self.direction *= -1  # Reverse horizontal direction

        self.move(dx, dy)
        self.parent.after(20, self.animate)
