# String
- String is a Data type that stores the squence of Characters.
## Different way to writing string.
- 1. Using single qouet - ' '
- Ex.
```
str = 'vidhi'
```
- 2. Using double qouet - " "
- Ex.
```
str = "vidhi"
```
- 3. Using Triple qouet - """ """
- Ex.
```
str = """ Vidhi """
```
### why we need three different way:
- Because if we write sentence and inside the sentence we need 's.
- so we required both double qoutes and single qouets string.
- otherwise python interpreter confues.
Ex.
```
str = "The cat's master loves his cat."

Apostrophes - 's 
```
### print sentence in new line.
- Using '\n'
- Ex.
```
str = "Hello World!!\nHow are You?"
```
### print sentence with space.
- Using '\t'
- Ex.
```
str = "Hello World!!\tHow are You?"
```
<hr>

## Basic Operations.
- <b>Concating two strings (Concatenation)</b>
- Addition of two string 
- Ex.
```
"hello" + "world" -> "helloworld"
```
- <b> length of string </b>
- Using len() 
- Ex.
```
str = "vidhi"
print(len(str))
```
- len() also count the space between two strings.
```
str = "apna"
str2 = "clg"
str3 = str +" "+str2
print(len(str3))
```
<hr>

## Indexing in String.
- index means to give position number for character
- Ex.
```
A P N A   C O L L E G
0 1 2 3 4 5 6 7 8 9 10
```
- index is also given to space.
- We can not modify the string using index.
Ex.
```
str = "apna"
str[0] = 'b' # not allowed in python
```
## Slicing in string:

- Accessing parts of the string.
- small parts / divide the string.
- Ex.
```
str[starting_idx : ending_idx] # ending index not included
```
```
 str = "A p n a C o l l e g e"
        0 1 2 3 4 5 6 7 8 9 10
```
```
str[0:4] is Apna
```
```
str[1:6] is pnaCo
```
```
str[:] is ApnaCollege # starting from zero and ending till string compeleted
```
```
str[4:] is College # ending str(len) is same as [4:str(len)]
```
```
str[:7] is ApnaCol # starting from zero end with 6+1. 
# same as [0:7]
```
<hr>

###  Use case of Slicing:
-  Image Processing:
- Cropping or Resizing: In image processing, slicing is used to crop images, remove unwanted borders, or focus on a specific section of the image.
```
image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cropped_image = image[1:3]  # Crop rows 1 and 2
```
- Data Analysis and Manipulation
- Pandas and NumPy: In data analysis using Pandas and NumPy, slicing is commonly used to select subsets of data, rows, columns, or specific portions of an array.
```
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
sub_arr = arr[1:4]  # Slicing the array to get elements 2, 3, and 4
```
- Web Scraping
- Extracting Parts of HTML: When scraping web pages, slicing helps extract specific parts of a webpage, such as text between certain tags or specific elements.
```
html = "<html><body><p>Hello World</p></body></html>"
content = html[12:-14]  # Extracting "Hello World"
```
- Security & Cryptography
- Machine Learning & AI

<hr>

### Negative Indexing:
```
A   p   p   l  e 
-5 -4  -3  -2 -1
```
```
str = "Apple"
print(str[-3:-1])
```
