# questions from book:
# What is nested list?
# A list within a list is called a nested list. 

# Can a list store both integers and strings in it?
# Yes. Elements in a list don’t have to be of the same type.



shop = ["t-shirt", "sweater", "jeans", "skirt", "cardigan", "socks"]

welcome = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if welcome == "R":
    R =  print("Our items: ", shop)
elif welcome == "C":
    C_item = input("Enter new item: ")
    C_add = shop.append(C_item)
    print("Our items: ", shop)
elif welcome == "U":
    U_pos = int(input("Update position? "))
    U_item = input("New item? ")
    shop[U_pos] = U_item
    print("Our items: ", shop)
elif welcome == "D":
    D_del = int(input("Delete position? "))
    shop.pop(D_del)
    print("Our items: ", shop)