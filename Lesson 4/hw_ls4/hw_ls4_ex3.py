print("Answer the following algebra question: ")

# question 1 
print("If x = 8, then what is the value of 4(x + 3)? ")
choices1 = {
    '1.' : 35,
    '2.' : 36,
    '3.' : 40,
    '4.' : 44
}
for k, v in choices1.items():
    print(k,v)

correct_answer = 0  # correct answer counts. 

answer = int(input("Your choice: "))
if answer == 4:
    print("Bingo")
    correct_answer += 1
else:
    print(":(")

# question 2 
print("Estimate this answer (exact calculation not needed): ")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66, and 52. What is the mean? ")
choices2 = {
    '1.' : 'About 55',
    '2.' : 'About 65',
    '3.' : 'About 75',
    '4.' : 'About 85'
}
for k, v in choices2.items():
    print(k,v)
answer = int(input("Your choice: "))
if answer == 2:
    print("Bingo")
    correct_answer += 1
else:
    print(":(")

print("You correctly answer", correct_answer, 'out of 2 questions.')




