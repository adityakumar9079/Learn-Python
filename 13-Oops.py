class food:
    apple="max-sweet"
    orange="sweet, sour"
    papaya="sweet"
    banana="very-sweet"
    quantity=4

taste=food()
print(taste.apple)
print(taste)
print(type(taste.banana))
print(type(taste.quantity))

# Practice Questions - Class & Object///////////////////////////////////////////////////////

# 1. Create a glass Car with attribute brand = "Scorpio".
class car:
    brand="scorpio"

company = car()
print(company.brand)


# 2. Create a class Laptop with attributes: brand, RAM, price. Create 2 objects
# with different values.

class Laptop:
    brand = "Asus"
    RAM = "16 GB"
    price = 67000

domain = Laptop()
domain.brand = "Acer"
cost = Laptop()

print(domain.brand)
print(cost.brand)
print(cost.price)