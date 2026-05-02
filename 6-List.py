list = ["Aditya",56,87,"Stya" , "Rajput"]
print(list)
print(list[0])
list.append("Aaaaa")
print(list)
list.extend("VBBBBBBB")
print(list)
list[5] = "Updated Value"

for i in list:
    print(i)

list.pop(3)
print(list)
list2 = [6,9827,92,678,38]
list2.sort()
print(list2)
list.append(list2)
print(list)
print(list[2:8])

print(list.count(56))
print(len(list))
# Praactice

write = input("Write Food 1:")
write1 = input("Write Food 2:")
write2 = input("Write Food 3:") 
writel = [write1,write1,write2]
print(writel)
print(len(writel))