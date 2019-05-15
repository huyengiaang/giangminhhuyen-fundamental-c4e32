# nhap n so nguyen tu ban phim. 
# -in ra day vua nhap 
# -in ra trung binh cong cac so chan 

n = int(input("Enter an integer number: "))
ds = []

for i in range(n):
    so = int(input("Enter the " + str(i+1) +  " integer: "))
    ds.append(so)
    # so = int(so)

print("List just entered: ", ds)
# print(ds)

# tong_so_chan = 0
# so_phan_tu_chan = 0
list_even = []

for v in ds:
    if v % 2 == 0:
        list_even.append(v)
print("Even numbers: ", list_even)
print("tbc la: ", sum(list_even)/len(list_even))
        # print(v)
        # tong_so_chan = tong_so_chan + v
        # so_phan_tu_chan += 1

# print("average of even numbers: ", tong_so_chan / 2 )
