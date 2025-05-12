# Task no 1 (Integer)

age = 26
#print("In 5 years,you will be,",age+5)

# Task no 2 (String)

name = "Fiza"
#print("Hello,",name)

# Task no 3 ( Float)

height = 1.64
#print("Your height is",height,"meters")

# Task no 4 (Combined use)

item = "Book"
quantity = 4
price_per_item = 12.99
total_cast = quantity*price_per_item
#print("You bought 4 Books for a total of",total_cast,"dollars")

# Task no 5 (Challenge Yourself)

name =input("What is your name?")
item =input("What item do you want to buy?")
price =float(input("What is the price of one{item}?"))
quantity =int(input("How many{item}do you want to buy?"))
total_cast =price*quantity
print(f"Hello {name}!")
print(f"You bought {quantity}{item}(s)")
print(f"Total {total_cast}(dollars)")