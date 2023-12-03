# A 3 layer, feed-forward neural network, with one hidden layer containing a single neuron
# that solves for the correct in/output mappings for OR gates or AND gates

import math
alpha = .01


def main():

    param1 = [.5, .5, .5]
    param2 = [.5, .5]
    epochs = 1000000
    # training_data, SET THESE LABELS TO [[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]
    # for an OR GATE OR [[0, 0], 0],  [[0, 1], 0], [[1, 0], 0], [[1, 1], 1] for an AND gate
    training_data = [[[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]]
    computing(training_data, param1, param2, epochs, alpha)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def computing(training_data, param1, param2, epochs, alpha):
    # 
    w00 = param1[0]
    w01 = param1[1]
    b0 = param1[2]
    w1 = param2[0]
    b1 = param2[1]
    for i in range(epochs):
        for j in range(len(training_data)):
            x = training_data[j][0][0]
            y = training_data[j][0][1]
            # activated output
            z0 = x * w00 + y * w01 + b0
            z1 = sigmoid(z0) * w1 + b1

            # prediction
            pred = sigmoid(z1)
            label = training_data[j][1]
            print(x, y, pred)

            dL_dw00 = 2 * (label - pred) * (-1) * sigmoid_derivative(z1) * w1 * sigmoid_derivative(z0) * x
            dL_dw01 = 2 * (label - pred) * (-1) * sigmoid_derivative(z1) * w1 * sigmoid_derivative(z0) * y
            dL_db0 = 2 * (label - pred) * (-1) * sigmoid_derivative(z1) * w1 * sigmoid_derivative(z0) * 1
            dL_dw1 = 2 * (label - pred) * (-1) * sigmoid_derivative(z1) * sigmoid(z0)
            dL_db1 = 2 * (label - pred) * (-1) * sigmoid_derivative(z1) * 1
            w00 = w00 - alpha * dL_dw00
            w01 = w01 - alpha * dL_dw01
            w1 = w1 - alpha * dL_dw1
            b0 = b0 - alpha * dL_db0
            b1 = b1 - alpha * dL_db1


main()
