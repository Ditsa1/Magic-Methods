class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([1, 2, 3])
print("First item:",a[0])
print("Second item:",a[1])
print("Third item:",a[2])
# Output: 
# First item: 1
# Second item: 2
# Third item: 3