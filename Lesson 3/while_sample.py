# n_str = input("Enter a number: ")
# while not n_str.isdigit():
#     n_str = input("Not a number. Enter again: ")

# n = int(n_str)

# if n >= 0:
#     print("Absolute value is: ", n)
# else:
#     print("Absolute value is: ", -n)


# dem = 0
# while True:
#     print("hi", dem)
#     dem += 1 #dem = dem + 1
#     if dem >=3:
#         break
# print("end")

# # de print o tren thi print 5 lan
# for v in range(40):
#     print("hi", v)
#     if v >=4:
#         break
    

# # de print o duoi thi print 4 lan
# for v in range(40):
#     if v >=4:
#         break
#     print("hi", v)


# check the length of password. if < 8, enter new password.
# pass_str = input("Enter password: ")
# length = len(pass_str)
# while length < 8:
#     pass_str = input("Insufficient length. Enter again: ")
#     length = len(pass_str)
# print("Your password is: ", pass_str)

# another way to do it
while True:
    pw = input("Enter password: ")
    if len(pw) > 8:
        break
print("Your password is: ", pw)

