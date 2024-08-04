# Nummeric Data Type
x = 12 # int
print(x)
x = 34.5 # float
print(x)
x = 2j # complex num
print(x)
# =============================================
# Bool Data type
x = True # bool
print(x)
# =============================================
# Sequencial Data type
x = "Hello world!!" # string  -> mutable
print(x)
x = [2,3,"vidhi"] # list -> mutable
print(x)
x = (5,6,"xyz") # tupel -> immutable
print(x)
# =============================================
# Dictionary 
x = {"Name":"vidhi","age":20} # Dictionary -> mutable -> Key:value pair
print(x)
# =============================================
# set -> unorderd -> unique
x = {'geeks','for','geeks'}
print(x)
# =============================================
# byte data type
x = b"geeks"
print(type(x),x)
encode = 'vidhi'.encode('utf-8')
print("Encode: ",encode)
decode = encode.decode('utf-8')
print("decode: ",decode)
# =============================================
# range() data type
x = range(0,10,2)
print(x)
for x in range(0,10,2): # also be right 
    print(x)

