import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.animation as animation

field_size = 100
field = np.random.choice([0, 1], size=(field_size, field_size), p=[0.6, 0.4])

def number_of_live_fields(field, x, y):
    return np.sum(field[x - 1:x + 2, y - 1:y + 2]) - field[x, y]

def evolve(frame, field):
    new_field = field.copy()
    for i in range(field_size):
        for j in range(field_size):
            live_fields = number_of_live_fields(field, i, j)
            if field[i, j] == 1:
                if live_fields < 2 or live_fields > 3:
                    new_field[i, j] = 0
            else:
                if live_fields == 3:
                    new_field[i, j] = 1
    mat.set_data(new_field)
    field[:] = new_field[:]
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(field, cmap=ListedColormap(['#2E3192', '#1BFFFF']))
ax.axis('off')
ax.set_title("Conway's Game of Life")
ani = animation.FuncAnimation(fig, evolve, fargs=(field,), frames=500, interval=100)

plt.show()
