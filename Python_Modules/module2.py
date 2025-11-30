import module1

def function2():
    print("This is the function from module2")


print("__name__ of module 2 : ",__name__)
if __name__=="__main__":                               
    function2()
    module1.function1()