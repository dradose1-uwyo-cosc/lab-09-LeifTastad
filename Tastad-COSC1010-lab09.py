# Leif Tastad
# UWYO COSC 1010
# Submission Date: 11/14/2024
# Lab 09
# Lab Section: 13

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

class Pizza:
    def __init__(self, size, sauce):
        self.sauce = sauce
        self.setSize(size)
        self.toppings = ['Cheese']
    
    def getSauce(self):
        return self.sauce
    

    def setSize(self, size):
        if size.isdigit():
            size = int(size)
            if size > 10:
                self.size = size
            else:
                self.size = 10
        else:
            self.size = 10
    def getSize(self):
        return self.size
    

    def addToppings(self, added_toppings):
        self.toppings.append(added_toppings)
    def getToppings(self):
        return self.toppings
    def getAmountOfToppings(self):
        return len(self.toppings) - 1


class Pizzeria:

    def __init__(self):
        self.orders = 0
        self.pizzas = []
    
    def placeOrder(self):
        size = input("The smallest pizza is 10 inches and the price is 60 cents an inch. Please enter a pizza size: ")

        sauce = input("Please enter the sauce you would like. Leave blank if you want red sauce: ").strip()
        if not sauce:
            sauce = 'red'
        pizza = Pizza(size, sauce)
        
        while True:
            topping = input("Toppings are 30 cents each. Please enter a topping and when done leave blank: ")
            if not topping:
                break
            pizza.addToppings(topping)
        
        self.pizzas.append(pizza)
        self.orders += 1
    
    topping_price = 0.30
    size_per_inch_price = 0.60
    
    def getReceipt(self):
        pizza = self.pizzas[-1]
        total_size_cost = pizza.getSize() * self.size_per_inch_price
        total_toppings_cost = pizza.getAmountOfToppings() * self.topping_price
        pizza_total = total_size_cost + total_toppings_cost

        print("Receipt:")
        print(f"Sauce: {pizza.getSauce()}")
        print(f"Size: {pizza.getSize()} inches")
        for top in pizza.getToppings():
            print(f"Toppings: {top}")
        print(f"Price for size: ${round(total_size_cost, 2)}0")
        print(f"Price for toppings: ${round(total_toppings_cost, 2)}0")
        print(f"Total price: ${round(pizza_total, 2)}0")
    def getNumberOfOrders(self):
        return self.orders

OrderForm = Pizzeria()
while True:
    pizzia_input = input("This is Leif's Fantastic Pizza, would you like to place an order? type exit to quit: ").strip()
    if pizzia_input.upper() == 'EXIT':
        break
    OrderForm.placeOrder()
    OrderForm.getReceipt()

if OrderForm.getNumberOfOrders() == 1:
    print(f"You've placed {OrderForm.getNumberOfOrders()} order please come again!")
elif OrderForm.getNumberOfOrders() > 1:
    print(f"You've placed {OrderForm.getNumberOfOrders()} orders please come again!")
else:
    print("You didn't order any pizzas, please come again!")