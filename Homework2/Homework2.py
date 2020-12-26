müsteri=[]
müsteri_firstname=input("Enter your  first name: ")
müsteri_lastname=input("Enter your last name: ")
müsteri_age=int(input("Enter your age: "))
müsteri_birthofyear=int(input("Enter your birth year: "))
müsteri.append(müsteri_firstname)
müsteri.append(müsteri_lastname)
müsteri.append(müsteri_age)
müsteri.append(müsteri_birthofyear)

for i in müsteri:
    print(i)

if müsteri_age<=18:
        print("You can't go out because it's too dangerous.")
else:
        print("You can go out to the street.")