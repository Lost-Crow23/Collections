<h1>Shopping list</h1>

This is the code for listings `Shopping list`.

This is a list including the following items.

    shopping_list = ["resort", "Nissan GTR", "pool", "theme park", "cinema"]

Prints out the zero index from the list.

    print(shopping_list[0])
    
    resort

Prints out the first index from the list.
    
    print(shopping_list[1])
    
    Nissan GTR

Prints out the last index from the list.
    
    print(shopping_list[-1])

    cinema

Replaces the 0 index with a new list name, then it is printed out.

    shopping_list[0] = "hotel"
    print(shopping_list[0])
    print(shopping_list)

    ['hotel', 'Nissan GTR', 'pool', 'theme park', 'cinema']

Replaces the first index with a new list name, then it is printed out.

    shopping_list[1] = "laptop"
    print(shopping_list[1])
    print(shopping_list)

    ['hotel', 'laptop', 'pool', 'theme park', 'cinema']

Adds the string at the end of the variable list -  shopping_list.

    shopping_list.append("olives")
    print(shopping_list)

    ['hotel', 'laptop', 'pool', 'theme park', 'cinema', 'olives']

Removes the specific string of the list variable

    shopping_list.remove("theme park")
    print(shopping_list)

    ['hotel', 'laptop', 'pool', 'cinema', 'olives']
Removes the last string from the list.

    shopping_list.pop()
    print(shopping_list)

    ['hotel', 'laptop', 'pool', 'cinema']

this is a readme file 