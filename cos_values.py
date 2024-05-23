import math
import matplotlib.pyplot as plt
import numpy as np

def calc_cos_values():
    cos_values = []
    # -0 because it will start +1 after the first arguement you pass
    for i in range(-0, 361):
        cos_value = math.cos(math.radians(i))
        cos_values.append(cos_value)
    return cos_values
def main():
    cosines = calc_cos_values()
    
    fig, ax = plt.subplots()
    thetas = []
    for i in range(-0, 361):
        thetas.append(i)
    # plot angles 0 - 360 on the x axis and their corresponding values on the y axis
    ax.plot(thetas, cosines)
    plt.show()
if __name__ == '__main__':
    main()
        
