import matplotlib.pyplot as plt
import numpy as np
from sine_values import calc_sin_values
class sinegraph:
    def __init__(self, fig):
        self.fig = fig

        self.sin_values = calc_sin_values()
        print(self.sin_values)
        thetas = []

        for i in range(-0, 361):
            thetas.append(i)
        self.plot(thetas, self.sin_values)

    def plot(self, thetas, sines):
        ax = self.fig.add_subplot(111)
        ax.plot(thetas, sines)
        ax.set_title('Sine Wave')
        ax.set_xlabel('Angle (degrees)')
        ax.set_ylabel('Sine value')
            
if __name__ == '__main__':
    # Create a new figure
    fig = plt.figure()

    # Create a Grid instance
    grid = sinegraph(fig)


    # Plot some data (example)
    x = np.linspace(0, 10, 100)
    y = np.sin(x)


    # Display the plot
    plt.show()
