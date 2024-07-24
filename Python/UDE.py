class ZeroCubeError(Exception):
    "0 Can`t be passed as a cube"

class Cube():
    def __init__(self, num):
        num = int(num)
        if num != 0:
            self.qub = num ** 3
        else:
            raise ZeroCubeError

try:
    num = Cube(input("Number >"))
 

except:
    print(ZeroCubeError.__doc__)

else:
    print(f"Cube : {str(num.qub)}")
finally:
    print("All done")

