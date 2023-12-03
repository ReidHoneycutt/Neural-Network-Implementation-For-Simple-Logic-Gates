// JavaScript implementation of a 3-layer feed-forward neural network with one hidden layer

function sigmoid(x) {
	return 1 / (1 + Math.exp(-x));
}

function sigmoidDerivative(x) {
	return sigmoid(x) * (1 - sigmoid(x));
}

function train(trainingData, param1, param2, epochs, alpha) {
	let w00 = param1[0];
	let w01 = param1[1];
	let b0 = param1[2];
	let w1 = param2[0];
	let b1 = param2[1];

	for (let i = 0; i < epochs; i++) {
		for (let j = 0; j < trainingData.length; j++) {
			let x = trainingData[j][0][0];
			let y = trainingData[j][0][1];

			// Activated output
			let z0 = x * w00 + y * w01 + b0;
			let z1 = sigmoid(z0) * w1 + b1;

			// Prediction
			let pred = sigmoid(z1);
			let label = trainingData[j][1];
			console.log(x, y, pred);

			let dL_dw00 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0) * x;
			let dL_dw01 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0) * y;
			let dL_db0 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * w1 * sigmoidDerivative(z0);
			let dL_dw1 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1) * sigmoid(z0);
			let dL_db1 = 2 * (label - pred) * (-1) * sigmoidDerivative(z1);

			w00 = w00 - alpha * dL_dw00;
			w01 = w01 - alpha * dL_dw01;
			w1 = w1 - alpha * dL_dw1;
			b0 = b0 - alpha * dL_db0;
			b1 = b1 - alpha * dL_db1;
		}
	}
}

// Main function
function main() {
	const param1 = [0.5, 0.5, 0.5];
	const param2 = [0.5, 0.5];
	const epochs = 100000;
	const alpha = 0.01;
	// Training data for OR gate: [[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]
	// Training data for AND gate: [[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]
	const trainingData = [[[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]];
	train(trainingData, param1, param2, epochs, alpha);
}

main();

