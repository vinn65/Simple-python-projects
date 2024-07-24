#Classes
class Coder():
    def __init__(self, name): 
        self.Name = name
        """
        class variables
        Cname = "us" - can be accessed outside the class
        _cname  = "me" - private variable, should not be accessed outside  but is accessible
        __ccname = "mine" - strongly private variable, cannot be accessed outside the class function.

        """
    def info(self):
        print(self.Name)
    def is_PyDev(self):
        if "python" or "Python" in self.language:
            print(True)
        else:
            print(False)

cd = Coder("Vincent")
cd.Language = ['Python', 'Dart']
print(cd.Language)
cd.info()
cd.is_PyDev()


class Algebra():
   def __init__(self, r = 0.0, i = 0.0):
       self.real = r
       self.imag = i
   def __add__(self, y):
    #    self.imag = self.imag + y.imag
    #    self.real = self.real + y.real
        return Algebra(self.imag + y.imag,self.real + y.real) # same as above
        
   def show_values(self):
       return self.real, self.imag


num1 = Algebra(4.5, 8.9)
num2 = Algebra(4.5, 8.9)
print(num1.real)
# print(num1 + num2) wrong TypeError: unsupported operand type(s) for +: 'Algebra' and 'Algebra'
num3 = num1 + num2
print(num3.show_values())


"""
Iterate over a self defined class
""" 

class sumPair():
    #initialize
    def __init__(self,lst):
        self.list = lst
        self.list_len = len(lst)
        self.i1 = 0
        self.i2 = 1
    def sh0w(self):
        print(self.list)
    #iteration
    def __iter__(self):
        return self
    #control next
    def __next__(self):
        if self.i2 >= self.list_len:
            raise StopIteration
        else:
            self.sum_pair = self.list[self.i1] +  self.list[self.i2]
            self.i1 += 1
            self.i2 += 1
        
        return self.sum_pair
        

k  = [2,1,5,4,3,6,6] 
I = sumPair(k)
I.sh0w()
for ele in I:
    print(ele)

"""
Classes & Objects Exercise 1
Create a class LenVal which will store the length of any data passed and a sho_val() method or function inside the LenVal class to print the length.

Create three objects of the class with the following values and use the sho_val() method on them

'Head'
[ 1, 9, 4, 2, 6]
(1, )
"""

class LenVal():
    def __init__(self,ln):
        self.ln = ln
        self.leng = len(ln)
    
    def sho_val(self):
        print(self.leng)

v1 = LenVal('Head')
v2 = LenVal((1, ))
v3 = LenVal([ 1, 9, 4, 2, 6])

v1.sho_val()
v2.sho_val()
v3.sho_val()
