# #2.1
# sheep = [50, 51, 63, 78, 64, 91, 47]
# print("Hello, my name is Huyen and this is the weight of my sheep: ", sheep)

# #2.2
# biggest = max(sheep)
# print("Now my biggest sheep has size", biggest, "let's shear it.")

# #2.3
# sheep.remove(biggest)
# sheep.append(20)
# print("After shearing, here is my flock", sheep)

# #2.4
# new_sheep = [x+50 for x in sheep]
# print("One month has passed, now here is my flock ", new_sheep)

#2.5   
    #2.1
sheep = [50, 51, 63, 78, 64, 91, 47]
print("Hello, my name is Huyen and this is the weight of my sheep: ", sheep)

for i in range(3):
    #2.2
    biggest = max(sheep)
    print("Now my biggest sheep has size", biggest, "let's shear it.")

    #2.3
    sheep.remove(biggest)
    sheep.append(20)
    print("After shearing, here is my flock", sheep)

    print("MONTH ", i+1)

    #2.4
    sheep = [x+50 for x in sheep]
    print("One month has passed, now here is my flock ", sheep)

total = sum(sheep)
print("My flock has size in total: ", total)
money = total*2
print("I would get ",total, "* 2$ =",money,"$")


