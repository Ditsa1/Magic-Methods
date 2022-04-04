class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
i = iter(Squares(1, 3))
print(next(i))
print(next(i))
print(next(i))
# Output: 1 4 9