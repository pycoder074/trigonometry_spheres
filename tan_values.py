import math
import matplotlib.pyplot as plt
import numpy as np

def calc_tan_values():
    tan_values = []
    # -0 because it will start +1 after the first arguement you pass
    for i in range(-0, 361):
        tan_value = math.tan(math.radians(i))
        tan_values.append(tan_value)
    return tan_values
def main():
    tans = calc_tan_values()
    
    fig, ax = plt.subplots()
    thetas = []
    for i in range(-0, 361):
        thetas.append(i)
    # plot angles 0 - 360 on the x axis and their corresponding values on the y axis
    ax.plot(thetas, tans)
    plt.show()
if __name__ == '__main__':
    main()
        
