def sum():
    a = 33
    b = 23
    print(a+b)

sum()
print(type(sum))


# Practice Questions

# 1. Write a function named welcome_message() that prints "Welcome to
# Python Programming!" three times.

def welcome_message() :
    print("Welcome to Python Programming!")

welcome_message()
welcome_message()
welcome_message()

# 2. Define a function inspire() that prints a motivational quote with your
# name.

def inspire() :
    print("Aditya is a good Boy he does't throw anyone of his life")

inspire()

# 3. Create a function good_morning() that prints "Good Morning, Saumya!".
# Call it twice.
def good_morning():
    print("Good Morning, Saumya!")

good_morning()


# 4. Why are functions used in programming? Write two advantages.

# Function is use programing to reduse the code readabiliuty
# it is make one time and use many times





# Practice Questions

# 1. Write a function show_age(name, age) that prints: "Saumya Singh is 21
# years old.
# 11

def show_age(name,age):
    print(name,age)

show_age("Saumya Singh",21)
 


# 2. Create a function add_numbers(a, b) that prints both the sum and
# difference.

def add_numbers(a,b):
    print(a+b)
    print(a-b)

add_numbers(34,20)

def save(a,b):
    return a*b
  

c = save(20,56)
print(c)

# 1. Write a function square(num) that returns the square of a number.
num = int(input("Enter Any Number For Square :-"))
def square(num):
    return num*num
c = square(num)
print(c)
# 2. Write a function that takes a string and returns the count of vowels and
# consonants separately.