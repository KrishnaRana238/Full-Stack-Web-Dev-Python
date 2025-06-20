# method overloading

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
d = MathOperations()
print(d.add(2, 3))  # This will call the first add method
print(d.add(2, 3, 5))  # This will call the second