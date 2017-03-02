'''
neuron
'''
# import libraries
import sys
import numpy as np


def identity_function(x):
    '''
    identity function
    '''
    return x


def sigmoid(x):
    '''
    sigmoid function
    '''
    return 1 / (1 + np.exp(-x))


def neuron_calc():
    '''
    calculate network
    '''
    # first layer
    print('first layer info[input->hidden]]:')

    X = np.array([1.0, 0.5])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])
    print('  weight: {0}'.format(W1.shape))
    print('  feature vector: {0}'.format(X.shape))
    print('  bias: {0}'.format(B1.shape))

    A1 = np.dot(X, W1) + B1
    print('  signal: {0}'.format(A1))

    Z1 = sigmoid(A1)
    print('  output: {0}'.format(Z1))

    # second layer
    print('second layer info[hidden->output]:')

    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    B2 = np.array([0.1, 0.2])
    print('  weight: {0}'.format(W2.shape))
    print('  feature vector: {0}'.format(Z1.shape))
    print('  bias: {0}'.format(B2.shape))

    A2 = np.dot(Z1, W2) + B2
    print('  signal: {0}'.format(A2))

    Z2 = sigmoid(A2)
    print('  output: {0}'.format(Z2))

    # final layer
    print('final layer info[output]:')

    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    B3 = np.array([0.1, 0.2])
    print('  weight: {0}'.format(W3.shape))
    print('  feature vector: {0}'.format(Z2.shape))
    print('  bias: {0}'.format(B3.shape))

    A3 = np.dot(Z2, W3) + B2
    print('  signal: {0}'.format(A3))

    Y = identity_function(A3)
    print('final output: {0}'.format(Y))

    return


def main():
    '''
    main function
    '''
    neuron_calc()

    return

if __name__ == '__main__':
    sys.exit(main())
