class ArrayQueue:
    DEFAULT_CAPACITY = 30 

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._first = 0  # Inicializa com 0
        self._last = 0  # Inicializa com 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     
        self._data[self._last] = e 
        self._last = (self._last + 1) % len(self._data)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print('fila vazia')
            return None 
        answer = self._data[self._first]
        self._data[self._first] = None     
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        return answer

    def first(self):
        if self.is_empty():
            print('fila vazia')
            return None
        return self._data[self._first]

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._first
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._first = 0
        self._last = self._size

    def print_queue(self):
        if self.is_empty():
            print('fila vazia')
        else:
            print('Fila:', end=' ')
            for i in range(self._first, self._last):
                print(self._data[i], end=' ')
            print()
