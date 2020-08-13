# -*- coding:utf-8 -*-

"""
title: 算法2.1 感知器学习算法的原始形式
"""
class Perceptron(object):
    
    def __init__(self, x):
        self.x = x

    def run(self, w_0, b_0, alpha=0.1):
        w = w_0
        b = b_0

        for x in self.x:
            f = x[1] * (w * x[0] + b)

            if f <= 0:
                w = w + alpha * x[1] * x[0]
                b = b + alpha * x[1]

        return w, b


# an example
x = [[1, -1], [2, -1], [3, 1,], [4, -1]]
p = Perceptron(x)
w, b = p.run(1, 2)

print(w, b)
