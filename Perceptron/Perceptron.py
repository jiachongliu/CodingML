# -*- coding:utf-8 -*-

"""
from: https://github.com/fengdu78/lihang-code/blob/master/%E7%AC%AC02%E7%AB%A0%20%E6%84%9F%E7%9F%A5%E6%9C%BA/2.Perceptron.ipynb

"""
import numpy as np

class Perceptron:
    def __init__(self, data, b, l_rate):
        self.w = np.ones(len(data[0]) - 1, dtype=np.float32)
        self.b = b
        self.l_rate = l_rate

    def sign(self, x, w, b):
        y = np.dot(x, w) + b
        return y

    # Stochastic Gradient Descent
    def SGD(self, X_train, y_train):
        is_wrong = False
        while not is_wrong:
            wrong_count = 0
            for d in range(len(X_train)):
                X = X_train[d]
                y = y_train[d]

                if y * self.sign(X, self.w, self.b) <= 0:
                    self.w = self.w + self.l_rate * np.dot(y, X)
                    self.b = self.b + self.l_rate * y
                    wrong_count += 1

            if wrong_count = 0:
                is_wrong = True

        return 'complete!'
