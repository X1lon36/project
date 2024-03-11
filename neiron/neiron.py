import numpy as np # модуль

import data     # второй файл питона с переменными

def sigmoid(x):
    return 1/ (1+np.exp(-x)) # формула сигмоиды

inputs = np.array(data.y) #входные нейроны с информацией
weights = np.array([10,0,-5]) #веса

outputs = sigmoid(np.dot(inputs,weights)) # расчёт по сигмоиде

print(outputs) # вывод данных

print(input())
