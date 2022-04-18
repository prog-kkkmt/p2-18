import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math
import re

plt.style.use('seaborn-whitegrid')
fig = plt.figure(num='Билет №7')
ax = fig.add_subplot(1, 1, 1)
ax.grid(which='both')
ax.grid(which='minor', alpha=0.6)
ax.grid(which='major', alpha=1)


# with open('coef3.txt', 'r') as file:
#     line = file.readline().split()

class App:
    FUNCTION_TEMPLATE = '{0} * cos(x) + {1}'

    @staticmethod
    def average(arr):
        return max(arr) - min(arr)

    def __init__(self, filename):
        self.ox_points = []
        self.oy_points = []
        with open(filename, 'r') as file:
            line = file.readline().split()
            self.abc = line[0:2]
            self.function = self.FUNCTION_TEMPLATE.format(*self.abc)
            if len(line) > 2:
                self.ct_x_step = float(1 / eval(line[2].replace(',', '.')))  # 1 > x > 0
                self.ct_y_step = float(1 / eval(line[3].replace(',', '.')))  # 1 > y > 0

    def calc_point(self, x):
        res = eval(self.function.replace('cos(x)', f'({str(math.cos(x))})'))
        return res

    def create_points(self, start=-20, end=20, step=2.0):
        if start <= 0:
            raise AttributeError('Start must be greater than zero')

        if re.search(r'^[^}]+$', self.function):
            for X in np.arange(start, end, step):
                self.ox_points.append(X)
                self.oy_points.append(self.calc_point(X))
        else:
            raise AttributeError(f'Incorrect function: {self.function}')

    def create_plot(self, ct_x_steps=None, ct_y_steps=None, int_steps=False):
        print(self.ct_x_step, self.ct_y_step)
        if not self.ox_points:
            raise Exception('Не заданы точки!')
        ct_x_steps = ct_x_steps or self.ct_x_step
        ct_y_steps = ct_y_steps or self.ct_y_step
        ox_step = self.average(self.ox_points) / ct_x_steps
        oy_step = self.average(self.oy_points) / ct_y_steps

        if int_steps:
            ox_step = ox_step > 1 and int(ox_step) or ox_step
            oy_step = oy_step > 1 and int(oy_step) or oy_step
        print(f'Шаг по X: {ox_step}', f'Кол-во отрезков: {ct_x_steps}', min(self.ox_points), max(self.ox_points))
        print(f'Шаг по Y: {oy_step}', f'Кол-во отрезков: {ct_y_steps}', min(self.oy_points), max(self.oy_points))
        ax.set_xticks(np.arange(min(self.ox_points), max(self.ox_points), ox_step))
        ax.set_yticks(np.arange(min(self.oy_points), max(self.oy_points), oy_step))
        ax.xaxis.set_minor_locator(MultipleLocator(ox_step / 5))
        ax.yaxis.set_minor_locator(MultipleLocator(oy_step / 5))

        plt.plot(self.ox_points, self.oy_points)
        plt.show()


if __name__ == '__main__':
    app = App('coef2.txt')
    app.create_points(2, 20, step=0.05)
    app.create_plot(10, 10, int_steps=True)
