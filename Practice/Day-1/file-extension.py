# File Extension Extractor
filename = input("Enter file name with extension: ")
f_extns = filename.split(".")
print("The file extension is: ",repr(f_extns[-1]))