class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-nagative int")
        self.capacity = capacity

    def __str__(self):
        return "🍪"*self.n

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size


def main():
    jar = Jar(10, 3)
    print(jar.size)

if __name__ == "__main__":
    main()
