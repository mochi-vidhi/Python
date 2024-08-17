my_str = "Vidhi Mochi"
print(my_str)
for i in my_str:
    print(i,end=" ")

print("\n")
for i in range(0,len(my_str)):
    print(i,end=" ")

print("\n")
print(my_str[:8])
print(my_str[1:2])
print(my_str[2:2]) # empty 
print(my_str[:])
#my_str[2:3] = "v" # not modified
print(my_str[4:len(my_str)])
