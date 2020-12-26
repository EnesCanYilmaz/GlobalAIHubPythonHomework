name = input("Adınız :")
print("Merhaba {}".format(name),"Adam Asmaca'ya hoşgeldiniz :)")

print("*********")
print(f'Kullanıcı Adı : {name}')
print("10 denemeniz var.!!")
print("*********")
word = "Phyton"
guess = ""
lives = 10
while lives > 0:
    character_left = 0
    for i in word:
        if i in guess:
            print(i)
        else:
            print("_")
            character_left+=1    
    if character_left==0:
        print("Kazandın")
        break

    guess2 = input("Harf giriniz:")
    guess +=guess2
    if guess2 not in word:
        lives-=1
        print("Yanlış")
        print(" {} hakkınız kaldı.!".format(lives))

        if lives == 0:
            print("Oyun sona erdi...")