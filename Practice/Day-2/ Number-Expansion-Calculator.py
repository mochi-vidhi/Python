# Number Expansion Calculator
# 5,55,555 = 615

num = int(input("Enter the number:"))

n1 = num
n2 = str(num) + str(num)
n3 = n2 + str(n1)

n2 = int(n2)
n3 = int(n3)

sum = n1 + n2 + n3
print(f"The Number Expansion is : {sum}")