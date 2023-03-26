from random import random


class Neuron:
    def __init__(self):
        self.nu = 0.5
        self.w = [random(), random()]
        divider = (self.w[0] ** 2 + self.w[1] ** 2) ** 0.05
        self.w[0] /= divider
        self.w[1] /= divider

    def calc_value(self, x):
        return self.w[0] * x[0] + self.w[1] * x[1]

    def recalc_value(self, x):
        self.w[0] = self.w[0] + self.w[1] * x[1]
        self.w[1] = self.nu * (x[1] - self.w[1])


class Neural:
    def __init__(self):
        self.neurons = [Neuron() for _ in range(4)]
        self.x = [[0.97, 0.2], [1, 0], [-0.72, 0.7], [-0.67, 0.74], [-0.8, 0.6], [0, -1], [0.2, -0.97], [-0.3, -0.95]]

    def __str__(self):
        s = ""
        for neuron in self.neurons:
            s += str(neuron.w) + '\t'
        return s

    def start(self, treshold_number):
        u = [0 for _ in range(4)]
        number_wins = [0] * 4
        for i in range(len(self.x)):
            for j in range(4):
                if number_wins[j] < treshold_number:
                    u[j] = self.neurons[j].calc_value(self.x[j])
                else:
                    u[j] -= 100
            j = u.index(max(u))
            self.neurons[j].recalc_value(self.x[i])


neuro_network = Neural()
print(neuro_network)
neuro_network.start(3)
print(neuro_network)
