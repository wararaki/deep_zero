'''
softmax
'''

import sys
import numpy as np

def softmax(a):
    '''
    softmax function
    '''
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def main():
    '''
    main function
    '''
    a = np.array([0.3, 2.9, 4.0])
    print(softmax(a))
    return

if __name__ == '__main__':
    sys.exit(main())
