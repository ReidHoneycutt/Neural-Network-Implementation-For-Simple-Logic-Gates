# Neural Network Implementation For Simple Logic Gates

  These are implementations of a 3-layer, feed-forward neural network, with one hidden layer containing a single neuron. The network can learn the in/output mappings of an OR logic gate, or an AND gate. Depending on how you set the training labels. To have it solve for an OR gate, set training_data  = [[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]. To have it solve for an AND gate, set training_data = [[0, 0], 0],  [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]. After a suffiecient number of epochs, the predictions will converge to 0 for the inputs where the output label is 0, and converge to 1 for the inputs where the output label is 1.

![Alt text](/output_screenshot.png)
  Included are implementations of this in python, and processing/Java, and an XOR solution in python(two neurons in the hidden layer)
