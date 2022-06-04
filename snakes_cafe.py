welcome_msg = """ **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
*********************************** """

print(welcome_msg)

menu = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
}
order = {}

while True:
    ord = input("> ")
    if ord == 'quit':
        break
    elif ord not in menu:
        print("Sorry, your choice isn't available in our menu \n"
              "** What would you like to order? **")
    elif ord not in order and ord in menu:
        order[ord] = 1
        print(f'** {order[ord]} order of {ord} have been added to your meal **')
    elif ord in order:
        order[ord] += 1
        print(f'** {order[ord]} order of {ord} have been added to your meal **')

if len(order) != 0:
    print(f"Your order is: {order}, Thank you for your patronage")
else:
    print("You didn't order, please visit us again")
