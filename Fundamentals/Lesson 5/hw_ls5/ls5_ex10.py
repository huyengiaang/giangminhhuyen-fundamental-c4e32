# check the function in exercise 9. 
def get_even_list(l):
    list_even = []
    for i in l:
        if i % 2 == 0:
            list_even.append(i)
    return list_even

even_list = get_even_list([1,2,5,9,-10,6])
print("List of even numbers: ", even_list)

if set(even_list) == set([2,-10,6]):
    print("Your function is correct")
else: 
    print("Ooops, bugs detected")