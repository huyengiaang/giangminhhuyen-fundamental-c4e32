# def say_hi():
#     print('hi')
#     print('bye')
# say_hi()
# say_hi()

# def add_two_number(a,b):
#     # a = int(input("Enter the first number: "))
#     # b = int(input("Enter the second number: "))
#     # print(a,b)
#     # print("Sum is: ", a+b)
#     if a>0:
#         return a+b 
#     if a<0:
#         return a-b #nhung lenh sau return khong co y nghia gi nua 
# a = 50
# b = 7
# c = 10
# tong1 = add_two_number(b,a)
# tong2 = add_two_number(tong1,c)
# print('tong 3 so: ', tong2)





# find sum of a number with its absolute value
# def abs_of_number(a):
#     if a>0:
#         return a 
#         print('tri tuyet doi la: ', a)
#     else:
#         return -a
#         print('tri tuyet doi la: ', -a)
#     print('tri tuyet doi la: ', a)
# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print(tong)


# evaluate(1,3,'+')

def evaluate(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
print(evaluate(1,3,'+'))

def eval_expression(s):
    a = int(s[0])
    b = int(s[2])
    c = s[1]
    return evaluate(a,b,c)
print(eval_expression('3+5'))

while True:
    s = input('nhap bieu thuc: ')
    print(eval_expression(s))


