import numpy as np

# Load the .npz file
data = np.load("w" + "_parameters.npz")

# Extract the arrays from the loaded data
weights_input_hidden = data['weights_input_hidden']
biases_input_hidden = data['biases_input_hidden']
weights_hidden_output = data['weights_hidden_output']
biases_hidden_output = data['biases_hidden_output']

# Print the arrays
print("Weights Input Hidden:")
print(weights_input_hidden)
print("\nBiases Input Hidden:")
print(biases_input_hidden)
print("\nWeights Hidden Output:")
print(weights_hidden_output)
print("\nBiases Hidden Output:")
print(biases_hidden_output)