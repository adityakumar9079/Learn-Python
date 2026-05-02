# num = 1
# while num <= 25:
#     print("Aditya")
#     num = 1+num



#     Practice Questions

# 1. Write a Python program to print numbers from 1 to 10 using a while loop.
print("1. Write a Python program to print numbers from 1 to 10 using a while loop.")
a = 1
while a <= 10:
    print(a)
    a+=1





# 2. Write a program to print numbers from 10 down to 1 using a while loop.
# (Hint: start from 10 and decrease the counter each time.)

# Example Output: 10 9 8 ... 1


print(" 2. Write a program to print numbers from 10 down to 1 using a while loop.")
b = 10
while b >= 1:
    print(b)
    b-=1

# 3. Write a program to print all even numbers between 1 and 50 using a while
# loop.
# (Hint: Use the modulus operator % to check for even numbers.)

# Example Output: 2 4 6 8 ... 50

print("3. Write a program to print all even numbers between 1 and 50 using a while")

c = 1
while c <=50:
    if c % 2 == 0:
        print(c)
    c+= 1

   
  



# 4. Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
# (Hint: Keep a running total inside the loop.)

# 5. Write a program to print this pattern using a while loop:




# 8. Write a program using for and range() to print all even numbers between 1
# and 20.

for n in range(1,21):
    if n %2 == 0:
        print(n)
    




# 9. Write a program to print numbers from 1 to 50, but print "Saumya Singh"
# instead of numbers that are multiples of 5.
# Example Output: 1 2 3 4 Saumya Singh 6 7 8 9 Saumya Singh ...


for name in range(1,51):
    if name % 5==0:
        print("Somaya Singh")
    else:
        print(name)


# 10.Write a program to print the square of each number from 1 to 10 using a for
# loop.
# Example Output: 1 4 9 16 25 36 49 64 81 100
for s in range (1,11):
    print(s*s)

# 11.Write a program that prints the multiplication table of any number entered
# the user using a for loop.

# Example Output:

ent = int(input("Enter Any number:-"))

for m in range(1,11):
    print(f"{ent} X {m} = {ent*m}")