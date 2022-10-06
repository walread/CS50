class Jar:
    def __init__(self, size, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-nagative int")
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return "🍪"*self.n

    def deposit(self, n):
        self._size += n

    def withdraw(self, n):
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(10, 3)
    print(jar.size)

if __name__ == "__main__":
    main()
