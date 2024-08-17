tr = "google.com"
print("The orignal string: ",str)
l = []
for word in str:
    if word not in l:
          l.append(word)
    
print("Unique list:",l)
x = []
for word in l:
       y = str.count(word)
       x.append(y)
print("Counted word in list: ",x)