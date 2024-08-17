# Write a  Python program to get a string made of the first 2 and last 2 
# characters of a given string. If the string length is less than 2, return 
# the empty string instead.
choice = True
while(choice):
        str = input("Enter the string:")
        print(str)
        if len(str)<2:
            first_last = ' '
            print(first_last)
        else:
            first_last = str[0:2] + str[-2:]
            print(first_last)
        choice = int(input("Do you enter any other string? press..1 :"))

