#ignore this for hw2
class Calculation:
    def __init__(self, a, b, operation):
        """initializing object/instance"""
        self.a = a
        self.b = b
        self.operation = operation
    
    def get_result(self):
        """Call the stored operation with a and b"""
        return self.operation(self.a,self.b)