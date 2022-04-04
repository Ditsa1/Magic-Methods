class CallExample:
    def __init__(self, val):
        self.val = val
    def __call__(self, b):
        return self.val * b
call_example = CallExample(5)
print(call_example(6))
# Output: 30