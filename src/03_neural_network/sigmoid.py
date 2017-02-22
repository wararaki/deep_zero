'''
this is step function test program
'''

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    '''
    sigmoid function
    '''
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    # create array
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)

    # plot chart
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
    