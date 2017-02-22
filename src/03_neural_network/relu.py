'''
Rectified Linier Unit function
'''
import numpy as np
import matplotlib.pylab as plt

def relu(x):
    '''
    Rectified Linier Unit
    '''
    return np.maximum(0, x)

if __name__ == '__main__':
    # create array
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)

    # plot chart
    plt.plot(x, y)
    plt.ylim(-1., 5.0)
    plt.show()
