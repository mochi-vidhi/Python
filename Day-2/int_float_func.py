# int()
# Ex.1
marks = "93"
print(type(marks),marks)
marks = int(marks)
print(type(marks),marks)

# Ex.2
# per = int("23a") # Give the error 
# per = int(23.4)  # Give the error
per = int(True)
print("Per is :",type(per),per)

# float()
price = "50.6"
print(type(price),price)
price = float(price)
print(type(price),price)

# Ex.2

rupee = float("23.34")
# rupee = flaot("vidhi") # Give the error 
# rupee = flaot(23)  # Give the float value
rupee = float(True)
print(type(rupee),rupee)
