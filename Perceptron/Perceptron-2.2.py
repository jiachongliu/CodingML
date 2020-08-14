# -*- coding:utf-8 -*-
"""
title: 算法2.2 感知器学习算法的对偶形式
"""

class Perceptron(object):
    def __init__(self, t):
        self.t = t

    def run(self, learning_rate=1):
        alpha = []
        for i in range(len(self.t)):
            alpha.append(0)

        b = 0

        for (i, x) in zip(range(len(self.t)), self.t):
            for (j, x2) in zip(range(len(self.t)), self.t):
                fun = x[1] * (alpha[j]*x2[1] * x2[0] * x[0] + b)

            if fun <= 0:
                alpha.insert(i, alpha[i] + learning_rate)
                b        = b + learning_rate * x[1]

                print(b)

        return alpha, b


x = [[3 ,1], [3, 1], [4, 1], [3, 1], [1, -1], [1, -1]]
p = Perceptron(x)
a = []
a, b = p.run()
print(a, b)

