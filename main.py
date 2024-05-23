win = tk.Tk()
canvas = Canvas(win, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)
# you can change the trig ratios for different movements
ball_sin = Ball(sin=True, parent=win, canvas=canvas)
win.mainloop()

