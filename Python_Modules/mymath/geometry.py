from mymath.calculator import product,add

#from calculator import product,add   #Use Relative Import While Executing geometry.py




def area(length,breadth):
    return product(length,breadth)

def perimeter(length,breadth):
    return 2*(add(length,breadth))

print(__name__)
if __name__=="__main__":
    print(area(10,20))
    print(perimeter(10,20))