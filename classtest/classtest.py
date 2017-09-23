class Screen(object):
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height = height
    @property
    def resolution(self):
        return self.__height * self.__width

# test:
s = Screen()
s.width = 2
s.height = 2
print(s.resolution)
assert s.resolution == 4, '2 * 2 = %d ?' % s.resolution



class Fab(object):
    def __init__(self):
        self.a ,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 1000000000:
            raise StopIteration()
        return self.a

i = 1cd
for n in Fab():
    print('i:',i,'fab:',n)
    i+=1