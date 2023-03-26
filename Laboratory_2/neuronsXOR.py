import random


def activate_function(value):
    # Relu
    if value < 0:
        return 0
    else:
        return value


class LayerInput:
    def __init__(self, neurons_count):
        self.neurons_count = neurons_count

    def calculate(self, input_vector):
        return input_vector

    def __str__(self):
        pass


class LayerOutput:
    def __init__(self):
        pass

    def calculate(self):
        pass

    def weights_change(self):
        pass

    def __str__(self):
        pass


class LayerHidden:

    def __init__(self, prev_neuron_count, cur_neuron_count, step_learn):
        self.out = []
        self.step_learn = step_learn
        self.step_y = step_learn / 3
        self.input_vector = []
        self.prev_neuron_count = prev_neuron_count
        self.cur_neuron_count = cur_neuron_count
        self.weights = []
        for _ in range(cur_neuron_count):
            weight = []
            for i in range(prev_neuron_count):
                weight.append(random.random())
            self.weights.append(weight)

    def weight_change(self):
        for i in range(self.cur_neuron_count):
            for j in range(self.prev_neuron_count):
                self.weights[i][j] = self.step_learn * self.input_vector[j][0] * self.out[i] * \
                                     self.input_vector[j][1] + self.weights[i][j] * (1 - self.step_y)

    def calculate(self, input_vector):
        self.input_vector = input_vector
        self.out = []
        for i in range(self.cur_neuron_count):
            summary = 0
            for j in range(self.prev_neuron_count):
                summary += self.input_vector[j][0] * self.weights[i][j] + self.input_vector[j][1] * self.weights[i][j]
            self.out.append(activate_function(summary))

    def __str__(self):
        s = ""
        for ww in self.weights:
            s += f'{ww}\n'
        return s


if __name__ == "__main__":
    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    d = [1, 0, 0, 1]
    layer = LayerHidden(4, 4, 0.5)
    print(layer, "\n")
    layer.calculate(x)
    layer.weight_change()
    print(layer)
