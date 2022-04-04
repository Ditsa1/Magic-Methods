class LenExample:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
len_instance = LenExample([1, 2, 3])
print(len(len_instance))
# Output: 3