# Neural Network Implementation For Learning Logic Gates

- A neural network(NN) with one hidden layer containing one neuron is capable of learning the in/output mappings of an OR gate, AND gate, NAND gatebut is not capable of learning an XOR because it is not linearly seperable.
- Contained in this repo is an implementation of a feed-forward neural network (NN) with one hidden layer. Note below in the truth table what is different about the logic gates that are learnable with 1 neuron in the hidden layer, and the gates that require two neurons in the hidden layer to get learned.
  
![Screenshot 2023-12-08 150546](https://github.com/ReidHoneycutt/Neural-Network-Implementation-For-Simple-Logic-Gates/assets/30945205/ebd2790a-54df-45d1-a808-8559fd86217c)
  
-A neural network(NN) with one hidden layer containing one neuron is capable of learning the in/output mappings of an OR, NOR, AND, and NAND but is not capable of learning an XOR or XNOR because their solution spaces are not linearly seperable. 
-To approximate the correct hyperplaneTo learn XOR or XNOR requires 2 neurons in the hidden layer. Note how in the truth table
  
- For the single neuron NN, have it solve for an OR gate by setting the training_data  = [[0, 0], 0],  [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]. To have it solve for an AND gate, set training_data = [[0, 0], 0],  [[0, 1], 0], [[1, 0], 0], [[1, 1], 1].
- After a suffiecient number of epochs, the predictions will converge to 0 for the inputs where the output target(correct answer) is 0, and converge to 1 for the inputs where the output target is 1.

  ![Alt text](model_definitions.png)

 

<img width="472" alt="Screenshot 2023-12-06 at 8 17 29 PM" src="https://github.com/ReidHoneycutt/Neural-Network-Implementation-For-Simple-Logic-Gates/assets/30945205/6dc539f8-9066-4f6a-9216-a4ad8dba1d4f">

 Note that the partials with respect to weight 00, weight 01, and bias 0 and weight 1 are identical except for their last term(last term being 1 in the case of weight 1), and the partials w.r.t weight and bias 1 are identical except for their last terms also.
 
<img width="343" alt="Screenshot 2023-12-06 at 8 16 49 PM" src="https://github.com/ReidHoneycutt/Neural-Network-Implementation-For-Simple-Logic-Gates/assets/30945205/6d964d67-676b-44b0-9372-03d2596e8a99">

![Alt text](partial_derivatives.png)

  Included are implementations of the 1-hidden-neuron NN in python, javascript and processing/Java, and a 2-hidden-neuron XOR solution in python(two neurons in the hidden layer).

  
 Here is what the output of the 2-hidden neuron NN with training data for an XOR looks like after 100,000 epochs of learning, where each epoch consists of a prediction for each of the 4 possible inputs: 
  The partial derivatives of the loss function L are as follows:
  
![Screenshot 2023-12-04 112223](https://github.com/ReidHoneycutt/Neural-Network-Implementation-For-Simple-Logic-Gates/assets/30945205/3743b458-488a-4038-b2e2-da4a8849f049)
