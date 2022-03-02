largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":            
            break
        else:
            num = int(num)
            if largest is None:
                largest = num
                smallest = num
            else:
                if num > largest:
                    largest = num
                if num < smallest:
                    smallest = num
    except:
        print("Invalid input")
        
print("Maximum is ", largest)
print("Minimum is ", smallest)