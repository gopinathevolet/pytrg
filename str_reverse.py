#Text Reverse using funtion and forloop
""" a is empty string variable name ,
	 For loop using for reverse string and store in a ,
	 len(text) is find the length of the string"""

def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print(reverse("Hello World!")) 
