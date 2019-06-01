m = int(input("Enter number of integers: "))

total_m = 0

ds_m = []

for i in range(m):
    integers = int(input("Enter the " + str(i+1) + " integer: "))
    ds_m.append(integers)
    
    total_m = total_m + integers
    
print(ds_m)
print("The sum of the integers is: ", total_m)
print("The average is: ", total_m/len(ds_m))




 
