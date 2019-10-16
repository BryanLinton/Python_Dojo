class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self 

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self 


md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
y = md.add(15).add(2,5,10).subtract(11,2).result
z = md.add(15).add(2,5,10).subtract(11,2,50).result
print(x)
print(y)
print(z)	

