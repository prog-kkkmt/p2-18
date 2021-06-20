import matplotlib.pyplot as plt
import math
def main():
    # Координаты точек по x
    x = []
    # Координаты точек графика first по оси y
    y1 = []


    print("Сколько будет чисел в массиве")
    n = int(input())
    numbers1 = [] #тесовые данные 98.0, 105.0, 100.0, 100.0, 106.0, 95.0, 116.0, 112.0
    numbers2 = [] #тестовые данные 2.1, 2.4, 3.2, 2.7, 2.2, 2.3, 3.8, 3.4
    
    for i in range(n):
        print("число первого массива")
        numbers1.append(float(input()))
    for i in range(n):
        print("число второго массива")
        numbers2.append(float(input()))
    
    a = getA(numbers1, numbers2)
    b = getB(numbers1, numbers2)
    print(a)
    print(b)

    graphListY = []

    for i in range(n):
        graphListY.append(a * numbers1[i] + b)
        
    plt.figure(figsize=(7, 4)) # Размер рисунка
    # Построение графика first
    plt.plot(numbers1, graphListY, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
    plt.legend() # Отображение легенды
    plt.grid(True) # Отображение сетки
    plt.show() # Отображение графика


def getAverage(list):#+
    result = 0
    for i in list:
        result += i
    return result / len(list)
        
def getTop(list1,list2):
    result = 0
    for i in range(len(list1)):
        result += (list1[i] - getAverage(list1)) *(list2[i] - getAverage(list2))
    return result
    
def getBot(list1):#+
    result = 0
    for i in range(len(list1)):
        result += math.pow((list1[i] - getAverage(list1)),2)
    return result

def getA(list1, list2):
    return getTop(list1,list2) / getBot(list1)

def getB(list1,list2):
    return getAverage(list2) - (getA(list1,list2) * getAverage(list1))

    
main()
