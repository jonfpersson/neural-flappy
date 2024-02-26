import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Network:
    def __init__(self, input_size, hidden_size, output_size):
        self.fitness = 0

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.failCounter = 0
        
        # Initialize weights and biases with random values
        self.weights_input_hidden = np.random.randn(hidden_size, input_size)
        self.biases_input_hidden = np.random.randn(hidden_size, 1)
        self.weights_hidden_output = np.random.randn(output_size, hidden_size)
        self.biases_hidden_output = np.random.randn(output_size, 1)
           # Set initial mutation rate
        self.initial_mutation_rate = 0.1
        self.current_mutation_rate = self.initial_mutation_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def update(self, mutation_rate=0.1):

        # Add small mutations to the new values
        self.weights_input_hidden += np.random.randn(*self.weights_input_hidden.shape) * mutation_rate
        self.biases_input_hidden += np.random.randn(*self.biases_input_hidden.shape) * mutation_rate
        self.weights_hidden_output += np.random.randn(*self.weights_hidden_output.shape) * mutation_rate
        self.biases_hidden_output += np.random.randn(*self.biases_hidden_output.shape) * mutation_rate

    def calc_fitness(self, local_fitness):
        # this run was better, let's update the current fitness and weights & biases (and adjust mutation rate)
        if local_fitness > self.fitness:
            self.fitness = local_fitness
            self.save_weights_biases("w")

            self.current_mutation_rate *= 0.05  # You can tune the decay rate as needed
            self.update(self.current_mutation_rate)

        else:
            # Increase mutation rate to encourage exploration
            self.current_mutation_rate *= 1.1  # You can tune the increment rate as needed
            # Apply a cap to the mutation rate to prevent it from growing indefinitely
            self.current_mutation_rate = min(self.current_mutation_rate, 0.8)
            # Perform mutation with the increased rate
            self.update(self.current_mutation_rate)
            self.failCounter += 1
            if(self.failCounter > 4):
                self.load_weights()
                self.failCounter =0


    def forward(self, inputs):
        inputs = np.array(inputs).reshape(-1, 1)
        hidden_inputs = np.dot(self.weights_input_hidden, inputs) + self.biases_input_hidden
        hidden_outputs = self.sigmoid(hidden_inputs)

        final_inputs = np.dot(self.weights_hidden_output, hidden_outputs) + self.biases_hidden_output
        final_outputs = self.sigmoid(final_inputs)

        print(self.fitness)

        return final_outputs
    def save_weights_biases(self, filename):
        np.savez(filename + "_parameters.npz",
                 weights_input_hidden=self.weights_input_hidden,
                 biases_input_hidden=self.biases_input_hidden,
                 weights_hidden_output=self.weights_hidden_output,
                 biases_hidden_output=self.biases_hidden_output,
                 fitness=self.fitness)

    def load_weights(self):
        # Load the .npz file
        try:
            data = np.load("w" + "_parameters.npz")
        except FileNotFoundError:
            print("File not found. Using default values.")
            return

        # Extract the arrays from the loaded data
        self.weights_input_hidden = data['weights_input_hidden']
        self.biases_input_hidden = data['biases_input_hidden']
        self.weights_hidden_output = data['weights_hidden_output']
        self.biases_hidden_output = data['biases_hidden_output']
        self.fitness = data['fitness']
