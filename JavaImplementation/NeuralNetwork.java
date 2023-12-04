public class NeuralNetwork {

    static final double alpha = 0.01;
    double[] param1 = {0.5, 0.5, 0.5};
    double[] param2 = {0.5, 0.5};
    int epochs = 1000000;
    // static is needed so that you don't have to send trainingData as a parameter
    static double[][][] trainingData = {{{0, 0}, {0}}, {{0, 1}, {1}}, {{1, 0}, {1}}, {{1, 1}, {1}}};
    
    NeuralNetwork(double[] param1_, double[] param2_, int epochs_) {
      param1 = param1_;
      param2 = param2_;
      epochs = epochs_;
      computing(trainingData, param1, param2, epochs, alpha);
    }

    public static double sigmoid(double x) {
        return 1 / (1 + Math.exp(-x));
    }

    public static double sigmoidDerivative(double x) {
        return sigmoid(x) * (1 - sigmoid(x));
    }

    public static void computing(double[][][] trainingData, double[] param1, double[] param2, int epochs, double alpha) {
        double w00 = param1[0];
        double w01 = param1[1];
        double b0 = param1[2];
        double w1 = param2[0];
        double b1 = param2[1];

        for (int i = 0; i < epochs; i++) {
            for (int j = 0; j < trainingData.length; j++) {
                double x = trainingData[j][0][0];
                double y = trainingData[j][0][1];
                // Activated output
                double z0 = x * w00 + y * w01 + b0;
                double z1 = sigmoid(z0) * w1 + b1;

                // Prediction
                double pred = sigmoid(z1);
                double label = trainingData[j][1][0];
                System.out.println(x + " " + y + " " + pred);

                double dL_dw00 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0) * x;
                double dL_dw01 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0) * y;
                double dL_db0 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0);
                double dL_dw1 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * sigmoid(z0);
                double dL_db1 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1);
                
                w00 -= alpha * dL_dw00;
                w01 -= alpha * dL_dw01;
                w1 -= alpha * dL_dw1;
                b0 -= alpha * dL_db0;
                b1 -= alpha * dL_db1;
            }
        }
    }
}
