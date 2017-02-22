'''
perceptron
'''

import numpy as np

def AND_old(x1, x2):
    '''
    AND perceptron
    '''
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2

    # validator
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def AND(x1, x2):
    '''
    AND function
    '''
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b

    # validator
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w*x) + b

    # validator
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    '''
    OR function
    '''
    x = np.array([x1, x2])
    y = np.array


if __name__ == "__main__":
    '''
    Main function
    '''

    # test
    print(NAND(0, 0))
    print(NAND(1, 0))
    print(NAND(0, 1))
    print(NAND(1, 1))
