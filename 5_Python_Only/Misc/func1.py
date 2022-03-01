def thing():
    print("Value - 1")
    print("Value - 2")
#thing()

def computepay(hours, rate):
    pay = 0
    if hours < 40:
        pay = hours * rate
    else:
        pay = 40 * rate + 1.5 * (hours - 40) * rate
    
    return pay

#print("Pay is: " + str(computepay(45, 10)))

def greet(lang):
    if lang == 'en':
        print("Hello boy")
    elif lang == 'sp':
        print("Holllaaa")
    else:
        print("Other lang")

greet('ur')

def func(x):
    print(x)
func(20)

def addTwo(a, b):
    added = a + b
    return a
x = addTwo(2, 7)
print(x)