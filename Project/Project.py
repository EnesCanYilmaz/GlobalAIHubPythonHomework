student_list = ["Enes Can Yılmaz","Emrah Arkcı","Murat Uçar","Kaan Özevren"]
courses = ["Matematik","Biyoloji","Fizik","Kimya","İngilizce"]

def letter_grade():
    
    courses_input = input("\nHangi dersleri almak istersiniz?: ")
    course_list = list(courses_input.split(","))
    
    if len(course_list) >= 3 and len(course_list) <= 5:
        
        for i in course_list:
            if i not in courses:
                return print("Sınıfınızda böyle bir ders",i,"bulunmamaktadır.")
        
        course = input("Notunuzu görmek için aldığınız kurslardan birini girin: ")
        
        if course in course_list:
            
            grades = {"vize":0,"final":0,"proje":0}
            
            vize = int(input("\nVize notunuzu giriniz: "))
            grades["vize"] = vize
            final = int(input("Final notunuzu giriniz: "))
            grades["final"] = final
            proje = int(input("Proje notunuzu giriniz: "))
            grades["proje"] = proje
            
            grade = (vize*30 + final*50 + proje*20)/100
            
            if grade >= 90:
                return print("\nDers Dereceniz AA.")
            if grade >= 70 and grade < 90:
                return print("\nDers Dereceniz BB.")
            if grade >= 50 and grade < 70:
                return print("\nDers Dereceniz CC.")
            if grade >= 30 and grade < 50:
                return print("\nDers Dereceniz DD.")
            else:
                return print("\nDers Dereceniz FF.")
        
        if course not in course_list and course in courses:
            return print("\nBu kursu alamazsın.")
        
        else:
            return print("\nSınıfınızda böyle bir ders",course,"bulunmamakta.")
        
    else:
        return print("\nEn az 3, en fazla 5 ders almalısınız. Sınıfta kaldın")


for i in range(4):
    
    name = input("Adınız: ")
    surname = input("Soyadınız: ")
    
    student_info = name + " " + surname
    
    if student_info in student_list:
        
        print("\n",student_info,",","Öğrenci bilgi sistemine hoşgeldin")
        letter_grade()
        break
    
    if i <= 2:
        
        print("Giriş sağlanamadı.\n")
    
    else:
        
        print("Tekrar deneyiniz")
