class Str:
    def __init__(self, string1):
        self.string1 = string1
    def __add__(self, string2):
        return self.string1 + string2
instance1 = Str("Hello")
print(instance1 + " Folks")
# Output: Hello Folks