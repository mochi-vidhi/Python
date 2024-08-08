# Check if a list contains an element
l1 = [1,2,3,4,5]
print(l1)
value = int(input("Enter the value to be check:"))
if value in l1:
    print("yes!! Value is Available",value)
    print("Index of value is :",l1.index(value))
else:
    print("Value is not available:",value)
