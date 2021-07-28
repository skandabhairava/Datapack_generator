def calcul_time(fonction):
    def wrapper():
        fonction()
        fonction.h = "abccc"    
    return wrapper

@calcul_time
def test():
    print("hallo!")

test()
print(test.h)