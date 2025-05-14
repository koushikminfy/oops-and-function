Easy oops
#1 .question
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
        
    def perimeter(self):
        return 2*(self.width+self.height)

# Example usage
rect = Rectangle(5, 10)
print(rect.area())
print(rect.perimeter())  


#2.question
class Counter:
    def __init__(self,value=0):
        self.value=value
    def increment(self):
        self.value +=1
        return self.value 
    def decrement(self):
        self.value -=1
        return self.value 
    def reset(self):
        self.value =0
        return self.value

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)  
counter.reset()
print(counter.value)  




