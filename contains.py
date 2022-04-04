class ContainsExample:
    def __init__(self, items):
        self.items = items
    def __contains__(self, item):
        return item in self.items
contains_instance = ContainsExample([1, 2, 3, 4, 5])
print(4 in contains_instance)