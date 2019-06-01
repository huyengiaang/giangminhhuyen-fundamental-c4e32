# name = input("What's your name? ")
# if name == "Huy small":
#     print("Handsome")
# elif name == "Huy big":
#     even_more_handsome = True
# else:
#     webbrowser.open("https://www.youtube.com/watch?v=04854XqcfCY")

mass = int(input("How much do you weigh in kg? ")) #in kg
height = int(input("How tall are you in cm? ")) #in cm
heightcv = (height/100) #in m

BMI = mass/(heightcv * heightcv)

if BMI < 16:
    print("You're severely underweight.")
elif 16 <= BMI < 18.5:
    print("You're underweight.")
elif 18.5 <= BMI < 25:
    print("You're normal.")
elif 25 <= BMI <= 30:
    print("You're overweight.")
elif BMI > 30:
    print("You're obese")
