#Base layer class
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input):
        # TODO : Return output
        pass

    def backward(self, output_gradient, learning_rate):
        # TODO : update parameters and return the input gradient
        pass

#print("Class is fine")