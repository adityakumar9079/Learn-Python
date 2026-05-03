# file = open("6-List.py")
# files = file.read()
# print(files)

# file = open("text.txt","a")
# file.write("yhuqihiowi")


# with open("mu.txt","w") as a:
#     a.write("Aditay is DevOps Enginear")
    

# with open("11-Function.py") as r:
#     l1 = r.readline()
#     l2 = r.readline()
#     l3 = r.readline()
#     l4= r.readline()
#     l5 = r.readline()
    
#     print(l1)
#     print(l2)
#     print(l3)
#     print(l4)
#     print(l5)



# Practice Questions - Reading Files

# 1. Read a file named story. txt and print the full content.

with open("story.txt","r") as s:
    data = s.read()
    print(data)

# 2. Read only the first line of bio.txt.
with open("bio.txt","w") as wr:
    wr.write("Aditya is Best")


with open("bio.txt") as l:
    list = l.readline()
    print(list)


# 3. Print how many lines are present in notes. txt.

with open("story.txt") as n:
    l = n.readlines()
    print(len(l))