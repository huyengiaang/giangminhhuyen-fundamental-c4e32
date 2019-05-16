# persons = [
#     {"name": "nguyen van a", "age": 21,"address": "hanoi"}, 
#     {"name": "nguyen van b", "age": 20,"address": "hcm"},
#     {"name": "nguyen van c", "age": 31,"address": "nam dinh"}
# ]
# print(persons[2],["age"])

# d = {'name': 'nguyen van a'}
# print(d.get('name', 'khong co trong tu dien'))

# if 'a' in d:
#     print(d['a'])


dic = {'mouse':'con chuot', 'keyboard':'ban phim', 'monitor':'man hinh'}

# while True: 
#     word = input("Enter a word: ")
#     if len(word) == 0:
#         break
#     if word in dic:
#         print("Meaning: ", dic[word])
#     else:
#         print("This word is not in the dictionary.")
    

for v in dic:                   # theo key
    print(v)
for v in dic.values():          # theo value
    print(v)
for v,k in dic.items():         # theo both key: value
    print(v, ":", k)









persons = [
    {'sdt':['9039920', '8399202'],
    'name': 'nguyen van A',
    'age': 21},
    {'sdt':[],
    'name': 'nguyen van B',
    'age': 23}
]

sdt = '9039920'     # find the name of the person whose number is this
for p in persons: 
    if sdt in p['sdt']:
        print(p['name'].split(' ')[-1])     # print the first name only

print(len(persons))     # number of items in list persons
first_person = persons[0]   # the first person's data
sdt = first_person['sdt']   # sdt of first person
first_sdt = sdt[1]  # find the second sdt of the first person
print(first_sdt)



