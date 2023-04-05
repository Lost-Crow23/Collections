# # using the range method to print out 10 times, items is variable
# # Hello, is printed out 10 times, to test if the loops are functional.
for item in range(10):
    print("hello")
#
# # Create another loop with a range that asks for names and appends to list_names
# initialise a list
list_data = []

# asks user input (names) , adds all names and type "finished" to end the process
the_names = (input("what names are you looking to enter: "))
while the_names.strip().lower() != "finished":
    list_data.append(the_names.strip())
    the_names = (input("Enter a name or type finished: "))
print("the names you entered are: ", list_data)
#
# '''
# # This loop iterates over each name in list_data and
# # formats it into lowercase in a new variable called list_names_lower
# '''
counter = 0
list_names_lower = []
for name in list_data:
    list_names_lower.append(list_data[counter].lower())
    counter += 1
print(list_names_lower)
# lastly, amount of names in the list is thus counted, and tells the user, if it's either odd or even
if counter % 2 == 0:
    print("There are an even amount of numbers in the list data")
else:
    print("There are an odd amount of names in the list data")

# 10 integers are to be taken from the list and the average value is to be solved
# print("we are going to work out the average of this numbers, please enter 10 numbers: ")
#
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# num_4 = int(input())
# num_5 = int(input())
# num_6 = int(input())
# num_7 = int(input())
# num_8 = int(input())
# num_9 = int(input())
# num_10 = int(input())
#
# num_list = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]
# print(num_list)
# average = sum(num_list) / len(num_list)
# print(f"your average is", {average})

