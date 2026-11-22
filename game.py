num=17
print("Guess the number between 1 to 50")

count=0
attempts=5

while count < attempts : 
    user_input=int(input("write ur guess\n u only have 5 attempts "))
 
    count += 1 
    if user_input == 17 :
        print("ur guess is right")
    elif user_input < num :
        print("ur guess is cold")
    elif user_input > num :
        print("ur guess is  ice cold")
    elif user_input > 10 :
        print("ur guess is hot")
    elif user_input >15 and user_input <19 :
        print("ur guess is very hot")

    print("remaining attempts : ", attempts-count)

if user_input != 17 : 
    print("wrong guess the number is 17")



