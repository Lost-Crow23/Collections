# item = variable / anything / index / starting point
# index
print("Welcome to the restaurant")

starter_menu = ("corn on cob", "chicken fingers", "dumplings", "wings", "no starters")
main_menu = ("salmon fillets", "grilled chicken", "ribs", "pasta")
dessert_menu = ("cheesecake", "trifle", "milkshake", "pudding", "no desserts")
#
# # item = variable / anything / index / starting point
# # empty list variable  - customer_order
customers_order = []
print("Starter menu:")
for item in starter_menu:
    print("- " + item)
print("Main menu:")
for item in main_menu:
    print("- " + item)
print("Dessert menu:")
for item in dessert_menu:
    print("- " + item)
print("These are you orders: ")
#
# # i = range 0 (index) ,it initially loops over to what you choose, range (3) = function which starts from 0
# # and stops in a specified number which in this case 3(max list of orders that can be placed)
# # then +1 = another time, until the range finishes.
for item in range(3):
    print("Order", item+1)
    starter = input("what starter from the menu do you choose?: ")
    main = input("what main from the menu do you choose?: ")
    dessert = input("what dessert from the menu do you choose?: ")
    customers_order.append((starter, main, dessert))
#
# prints the customers orders back to them, the list of 3 orders they have ordered.
# the f function is used to add the variables with the index's which comes out in order in a row.
print("Your order:")
for item in range(len(customers_order)):
    print(f"Order {item+1}: {customers_order[item][0]}, {customers_order[item][1]}, {customers_order[item][2]}")




