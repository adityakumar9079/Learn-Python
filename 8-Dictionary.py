dist = {
    "name":"Aditya Rajput",
    "Age":20,
    "Uni":"Ignou",
    "Sub":"BCAOL",
    "Roll":2401635869
}
print(dist)
print(type(dist))
print(dist["Uni"])
dist["sub"]="NEW"
print(dist)
print(dist.values())
print(dist.keys())
print(dist.items())
dist.pop("sub")
print(dist)
print(dist.pop("Uni"))
print(dist)



# Practice..........................................................................................................


# Create a dictionary named marks to store marks of 3 subjects.
# Add the subjects one by one and print the final dictionary.

ent1 = int(input("Enter Hindi marks: "))
ent2 = int(input("Enter English marks: "))
ent3 = int(input("Enter Maths marks: "))

marks = {
    "Hindi": ent1,
    "English": ent2,
    "Maths": ent3
}

print(marks)