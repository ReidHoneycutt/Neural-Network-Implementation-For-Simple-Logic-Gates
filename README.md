# Neural Network Implementation For Simple Logic Gates

Contained in this repo are implementations of a 3-layer, feed-forward neural network (NN), with one hidden layer containing a single neuron, which can solve OR and AND logic gates, and an implementation of a NN with 2 neurons in the hidden layer, which can solve XOR gates. A NN with one neuron in the hidden layer can learn the in/output mappings of an OR gate, or an AND gate, but cannot solve the XOR because it is not linearly seperable, and thus requires 2 neurons in the hidden layer to approximate the correct hyperplane. 
  
  For the single neuron NN, depending on how you set the training labels, have it solve for an OR gate by setting the training_data  = [[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]. To have it solve for an AND gate, set training_data = [[0, 0], 0],  [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]. After a suffiecient number of epochs, the predictions will converge to 0 for the inputs where the output target is 0, and converge to 1 for the inputs where the output target is 1.

  Here is what the output of the 2-hidden neuron NN with training data for an XOR looks like after 100,000 epochs of learning, where each epoch consists of a prediction for each of the 4 possible inputs: 

![Alt text](XOR_NN_output.png)

# Neural Network Partial Derivatives Computation

This document explains the computation of partial derivatives of the loss function `L` in a simple neural network model.

## Model Description

In this neural network model, we define:

- `L` as the loss function: \( L = (\text{label} - \text{pred})^2 \)
- `pred` as the prediction: \( \text{pred} = \text{sigmoid}(z_1) \)
- `z_1` as the output of the first neuron: \( z_1 = \text{sigmoid}(z_0) \cdot w_1 + b_1 \)
- `z_0` as the input to the first neuron: \( z_0 = x \cdot w_{00} + y \cdot w_{01} + b_0 \)

Where:
- `x`, `y` are inputs
- `w_{00}`, `w_{01}`, `b_0`, `w_1`, `b_1` are parameters of the model
- `sigmoid(z)` is the sigmoid activation function

## Partial Derivatives Computation

The partial derivatives of the loss function `L` with respect to the parameters are computed as follows:

### 1. Partial Derivative with respect to `w_{00}`

\[ \frac{\partial L}{\partial w_{00}} = 2 \cdot (\text{label} - \text{pred}) \cdot (-1) \cdot \text{sigmoid}'(z_1) \cdot w_1 \cdot \text{sigmoid}'(z_0) \cdot x \]

### 2. Partial Derivative with respect to `w_{01}`

\[ \frac{\partial L}{\partial w_{01}} = 2 \cdot (\text{label} - \text{pred}) \cdot (-1) \cdot \text{sigmoid}'(z_1) \cdot w_1 \cdot \text{sigmoid}'(z_0) \cdot y \]

### 3. Partial Derivative with respect to `b_0`

\[ \frac{\partial L}{\partial b_0} = 2 \cdot (\text{label} - \text{pred}) \cdot (-1) \cdot \text{sigmoid}'(z_1) \cdot w_1 \cdot \text{sigmoid}'(z_0) \]

### 4. Partial Derivative with respect to `w_1`

\[ \frac{\partial L}{\partial w_1} = 2 \cdot (\text{label} - \text{pred}) \cdot (-1) \cdot \text{sigmoid}'(z_1) \cdot \text{sigmoid}(z_0) \]

### 5. Partial Derivative with respect to `b_1`

\[ \frac{\partial L}{\partial b_1} = 2 \cdot (\text{label} - \text{pred}) \cdot (-1) \cdot \text{sigmoid}'(z_1) \]

## Conclusion

These partial derivatives are crucial for the backpropagation algorithm in the neural network, which adjusts the parameters `w_{00}`, `w_{01}`, `b_0`, `w_1`, and `b_1` to minimize the loss function `L`.


  Included are implementations of the 1-hidden-neuron NN in python, javascript and processing/Java, and a 2-hidden-neuron XOR solution in python(two neurons in the hidden layer).

  
