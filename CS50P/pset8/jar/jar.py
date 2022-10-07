class Jar:
    def __init__(self, capacity=12):
        self.capacity = 12
        if self.capacity < 0:
            raise ValueError("Capacity must be a non-nagative int")

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
