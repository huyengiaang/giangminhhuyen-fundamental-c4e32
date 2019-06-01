# phan tich mot so ra so nguyen to

n = int(input("Enter a number: "))

so_chia = 2
ls = []
if n == 1:
    print("1")
while n > 1:
    if n % so_chia == 0:
        kq = n / so_chia
        print(so_chia)
        ls.append(so_chia)
        n = kq
    else:
        so_chia += 1  
