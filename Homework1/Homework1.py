value1=input("Adınızı yazınız:")
value2=int(input("Bir tam sayı giriniz:"))
value3=float(input("Bir ondalıklı sayı giriniz:"))
value4=bool(input("Bir boolean ifade giriniz:"))
value5=complex(input("Bir karmaşık sayı giriniz:"))
##
type1=type(value1)
type2=type(value2)
type3=type(value3)
type4=type(value4)
type5=type(value5)
##
print(f"1. ifade: {value1} ve türü:{type1}")
print(f"2. ifade: {value2} ve türü:{type2}")
print(f"3. ifade: {value3} ve türü:{type3}")
print(f"4. ifade: {value4} ve türü:{type4}")
print(f"5. ifade: {value5} ve türü:{type5}")