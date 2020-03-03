import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.w = 2*np.random.random((3,1))-1

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoidDerivative(self, x):
        return x*(1-x)



    def train(self, train_inputs, train_outputs, iterations):
        for j in range(iterations):
            input_layer = train_inputs
            outputs = self.sigmoid(np.dot(input_layer, self.w))
            err = train_outputs-outputs
            adjust = err*self.sigmoidDerivative(outputs)
            self.w += np.dot(input_layer.T, adjust)

    def think(self, inputs):
        inputs = inputs.astype(float)
        return self.sigmoid(np.dot(inputs, self.w))


n = NeuralNetwork()
print("Random starting synaptic weights:\n",n.w)

train_inputs = np.array([[0,0,1],
                         [1,1,1],
                         [1,0,1],
                         [0,1,1]])

train_outputs = np.array([[0,1,1,0]]).T

n.train(train_inputs, train_outputs, 20000)
print("Synaptic weights after traingin:\n",n.w)

A = str(input("In 1: "))
B = str(input("In 2: "))
C = str(input("In 3: "))

print("New situation: input data = ",A,B,C)
print("Output:\n",n.think(np.array([A,B,C])))
