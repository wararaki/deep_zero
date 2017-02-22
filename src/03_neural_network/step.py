'''
this is step function test program
'''

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    '''
    step function
    '''
    return np.array(x > 0, dtype=np.int)


if __name__ == "__main__":
    # create array
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)

    # plot chart
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
