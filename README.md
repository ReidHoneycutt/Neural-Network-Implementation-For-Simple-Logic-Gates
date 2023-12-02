# Neural-Network-Implementation-For-Simple-Logic-Gates

This is an implementation of a 2 node neural network which can learn the in/output mappings of an OR logic gate, or an AND logic gate. Depending on how you set the training labels. Set training_data  = [[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1] to have it converge to the mappings of an OR gate. Set training_data = [[0, 0], 0],  [[0, 1], 0], [[1, 0], 0], [[1, 1], 1] for an AND gate.
