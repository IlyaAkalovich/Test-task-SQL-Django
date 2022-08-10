# 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

# Python
# example:
    #def isEven(value): return value % 2 == 0

#Decision:
    def isEven(value): return value & 1 == 0

# Плюсы реализации в примерах - простота понимания, можно адаптировать для функции вычисления остатка от деления одного числа на другое.
# Минусы реализации в примерах - работает медленнее, чем низкоуровневые операции.


# 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

# First
# implementation:

class RingBuffer:
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.max

        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data

# Second
# implementation:

class CircularBuffer(object):
    def __init__(self, size):
        self.index = 0
        self.size = size
        self._data = []

    def record(self, value):
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size

    def __getitem__(self, key):
        return (self._data[key])

    def __repr__(self):
        return self._data.__repr__() + ' (' + str(len(self._data)) + ' items)'

    def get_all(self):
        return (self._data)


# 3. На языке Python реализовать функцию,
# которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
# Объяснить почему вы считаете, что функция соответствует заданным критериям.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

         while j < len(R):
             arr[k] = R[j]
             j += 1
             k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Сортировка слиянием работает быстрее quicksort в худшем случае, и имеет сложность O(nlogn).