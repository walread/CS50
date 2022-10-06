class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-nagative int")
        self.capacity = capacity

    def __str__(self):
        for _ in self.size:
            return "🍪"*3

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        

    @property
    def size(self):
        self.size = 3


def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
