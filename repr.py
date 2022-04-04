class ReprExample:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return f"ReprExample(a={self.a}, b={self.b}, c={self.c})"
repr_instance = ReprExample(1, 2, 3)
print(repr_instance)
# Output
# ReprExample(a=1, b=2, c=3)