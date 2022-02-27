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

print("Pay is: " + str(computepay(45, 10)))