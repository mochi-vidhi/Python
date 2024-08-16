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






