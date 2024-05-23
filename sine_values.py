import math
import matplotlib.pyplot as plt
import numpy as np
def calc_sin_values():
    sin_values = []
    # -0 because it will start +1 after the first arguement you pass
    for i in range(-720, 720):
        sin_value = math.sin(math.radians(i))
        sin_values.append(sin_value)
    return sin_values

def main():
    sines = calc_sin_values()
    
    fig, ax = plt.subplots()
    thetas = []
    for i in range(-720, 720):
        thetas.append(i)
    # plot angles 0 - 360 on the x axis and their corresponding values on the y axis
    ax.plot(thetas, sines)
    ax.set_xlabel('thetas')
    ax.set_ylabel('sines')
    plt.show()
if __name__ == '__main__':
    main()
    
        
