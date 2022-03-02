largest = -1
print("Starting now: ", largest)
for i in [5, 9, 12, 28, 74, 41, 55]:
    if i > largest:
        largest = i
    print("Largest now: ", largest)

print("Finally: ", largest)