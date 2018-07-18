def add(a, b):
	return a + b

def divide(n, d):
    return n/d


class Calculator():
    
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b is 0:
          return None
        return a / b