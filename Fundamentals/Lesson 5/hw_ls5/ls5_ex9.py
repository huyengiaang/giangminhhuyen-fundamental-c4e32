# write a function that extracts the even items in a given integer list.
# return a new list contains only even numbers. 
def get_even_list(l):
    list_even = []
    for i in l:
        if i % 2 == 0:
            list_even.append(i)
    return list_even

even_list = get_even_list([1, 6, 5, -1, 4])
print("List of even numbers: ", even_list)

