import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

class anime_polt():
    def __init__(self):

        self.x_vals = []
        self.y_vals = []

        self.index = count()
        # self.ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)


    def start_animation(self):
        self.ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        plt.tight_layout()
        plt.show()
        # return self.y_vals

    def animate(self,i):
        # self.x_vals.append(next(self.index))
        self.y_vals.append(i)
        plt.cla()
        plt.plot(self.x_vals, self.y_vals)

        print(i)

if __name__ == "__main__":
    anime_plot_instance = anime_polt()
    y_values = anime_plot_instance.start_animation()
