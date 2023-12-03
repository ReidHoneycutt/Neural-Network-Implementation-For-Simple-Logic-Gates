NeuralNetwork NN;

void setup() {
  size(900, 900);
  double[] param1 = {0.5, 0.5, 0.5};
  double[] param2 = {0.5, 0.5};
  int epochs = 1000000;
  // Set the training data set, and the learning rate alpha in the NN class
  double[][][] trainingData = {{{0, 0}, {0}}, {{0, 1}, {1}}, {{1, 0}, {1}}, {{1, 1}, {0}}};
  // 
  NN = new NeuralNetwork(param1, param2, epochs);
  
}


  
