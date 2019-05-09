# for i in [1, 2, 3, 'x']:
#     print("Hi", i)

# for i in [1,2,3,4,5,6,7,8,9,10]:
#     if i % 2 == 1:
#         print(i)

# for k in range(10):
#     for v in range(k):
#         print(v, end = " ")
# print()

# for k in range(10):
#     for v in range(10):
#         for x in range(10):
#             print(k,v,x)


# for i in range(n+1):
#     # print(i)
#     number = n+2
#     total = (n+1) / number * 2
# print("Total: ")

n = int(input("Insert number: "))
tong = 0
for v in range(n+1):
    tong = tong + v
print(tong)
