class Shape:
    def __init__(self,length):
        self.length=length
    
    def area(self,length):
        area=self.length**2
        return 0

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self,length)
    
    def area(self, length):
        area=self.length**2
        print("정사각형의 면적: {}".format(area))
        return area
       
side=int(input("정사각형의 한 변의 길이를 입력하세요: "))
result=Square(side)
result.area(side)