"""

Matplotlib - what are the libraries in here?

plt.plot(x, y)
plt.scatter(x, y)
plt.bar(x, y)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [-1, -4, -9, -16, -25, -36, -49, -64, -81, -100]
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style




def plotMe (x, y):
    plt.plot(x, y, color='b')
    plt.title("Tutorial01 Chart");
    plt.xlabel("x-axis");
    plt.ylabel("y-axis");
    plt.show();

def xSquared (x):
    return (x*np.pi - 3);

def xCubed (x):
    return (x*x);

def plotFunction():
    _domain = []
    _range  = []
    for x in range (0, 100):
        _domain.append(x)
        _range.append(xSquared(x))
    plotMe (_domain, _range)
    print("preProcessor() ------> Done!")

def main():
    plotFunction()
    print(np.pi)
    
    
if __name__ == "__main__": 
    # calling main function 
    main() 

