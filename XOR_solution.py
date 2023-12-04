# The neural network is structured with two neurons in the hidden layer and one neuron in the output layer.
import math

alpha = 0.1  # Learning rate


def main():
    # Initial parameters for the neural network
    # Two neurons in the hidden layer, each with two weights and one bias
    weights_hidden = [[0.15, 0.25], [0.35, 0.45]]
    bias_hidden = [0.6, 0.7]

    # One neuron in the output layer with two weights and one bias
    weights_output = [0.55, 0.65]
    bias_output = 0.8

    epochs = 100000  # Number of training iterations
    training_data = [[[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 0]]  # XOR training data

    # Training process
    for _ in range(epochs):
        for input_data, target in training_data:
            # Forward pass
            hidden_layer_output = [sigmoid(dot_product(input_data, weights_hidden[i]) + bias_hidden[i]) for i in range(2)]
            output = sigmoid(dot_product(hidden_layer_output, weights_output) + bias_output)

            # Compute error
            error = target - output

            # Backward pass (Backpropagation)
            # Update weights and biases for the output layer
            weights_output = [weights_output[i] + alpha * error * sigmoid_derivative(output) * hidden_layer_output[i] for i in range(2)]
            bias_output += alpha * error * sigmoid_derivative(output)

            # Update weights and biases for the hidden layer
            for i in range(2):
                for j in range(2):
                    weights_hidden[i][j] += alpha * error * sigmoid_derivative(output) * weights_output[i] * sigmoid_derivative(hidden_layer_output[i]) * input_data[j]
                bias_hidden[i] += alpha * error * sigmoid_derivative(output) * weights_output[i] * sigmoid_derivative(hidden_layer_output[i])
            print("input: " + str(input_data) + "     " + "prediction: " + str(output) + "    " + "target: " + str(target))


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


main()
