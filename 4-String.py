# String
a = "Aditya Rajput"
b = "Hacker"

#  Combining two strings
print (a + " " + b) 

#length 
print(len(a))

# Slicing
print(a[1:9])
print(a[1:-10])

#Case

print(a.isupper())
print(a.upper())
print(b.lower())
print(a.find("Ai"))
print(a.replace("Rajput","Kumar"))

# Practice 

Given = input("")
Given = Given.replace(" ","_")
Given = Given.lower()
Given = Given + "\n"
print(Given*10)