import datetime as dt
# class User:
    
#     count = 0
#     @classmethod
#     def active_users(cls):
#         return f"aktif kullanıcı sayısı: {cls.count}"
    
    
#     @classmethod
#     def usersLog(cls,data_log):
#         name,surname,username,birthdate,password = data_log.split(" ")
#         birthdate = int(birthdate)
#         return cls(name,surname,username,birthdate,password)
#     def __init__(self,name,surname,username,birthdate,password):
#         self.name = name
#         self.surname = surname
#         self.username = username
#         self.birthdate = birthdate
#         self.password = password
#         self.age = User.calAge(self)
#         User.count +=1
#     def calAge(self):
#         return dt.datetime.now().year - self.birthdate
    
#     def info(self):
#         return f"{self.username} kullanıcı adıyla {self.name } {self.surname} isminde ve {self.age} yaşındaki kişi kaydolmuştur."
    
#     def logOut(self):
#         User.count -=1
#         return f"{self.username} çıkış yaptı."
    
# print(User.active_users())
# user1 = User("sefa","şeker","sefaseker",2004,"sefa123")
# user3 = User("sef","şek","sefasekerr",2003,"sefa1234")
# user2 = User("se","şeke","sefasekerrr",2002,"sefa12345")
# user4 = User.usersLog("eşşek köle hiranur 2013 eşşekhira")
# print(User.active_users())
# print(user1.info())
# print(user3.info())
# print(user2.info())
# print(user4.info())

# user3.logOut()
# user1.logOut()
# user2.logOut()



# print(User.active_users())

# x = "sefa"

# x.strip

class Kisi:
    @classmethod
    def kisi(cls,data_str):
        name,surname,birthdate,gender = data_str.split(" ")
        return cls(name,surname,birthdate,gender)
    
    def __init__(self,name,surname,birthdate,gender):
        self.name = name
        self.surname = surname
        birthdate = int(birthdate)
        self.birthdate = birthdate
        self.gender = gender
        self.age = Kisi.yasHesapla(self)
        

    
    def yasHesapla(self):
        return dt.datetime.now().year - self.birthdate
    
    def info(self):
        if hasattr(self,"number"):
            return f"{self.name} {self.surname} isimli öğrencinin yaşı {self.age} ve numarası {self.number} notları {self.notlar}, ortlaması ise {self.ort}"
        elif hasattr(self,"branch"):
            return f"{self.name} {self.surname} isimli öğrencinin yaşı {self.age} branşı {self.branch} "
        else:
            return f"{self.name} {self.surname} isimli öğrencinin yaşı {self.age} "
                
        

class ogrenci(Kisi):
    def __init__(self, name, surname, birthdate, gender,number):
        super().__init__(name, surname, birthdate,gender)
        self.number = number
        print("ogrenci çalıştı")
        
    def sinavNotlari(self):
        print(f"{self.number } numaralı öğrenci notlarını girin.")
        notlar = []
        for i in range(3):
            notlar.append(int(input(f"{i+1}. notunu giriniz")))
        self.notlar = notlar
        return notlar
    
    def ortAl(self):
        ort = sum(self.notlar) / len(self.notlar)
        ort= round(ort , 2)
        self.ort =ort
        return ort
    
    

class ogretmen(Kisi):
    def __init__(self, name, surname, birthdate, gender,branch):
        super().__init__(name, surname, birthdate, gender)
        self.branch =branch
        print("öğretmen oluştu")
    


user1 = Kisi("sefa","şeker",2004,"erkek")
user2 = Kisi.kisi("sefa şeker 2004 erkek")
user3 = ogrenci("mete","han",209,"errrkekk",1071)
user4 = ogretmen("cengiz","han",209,"errrkekk","komutan")
print(user3.sinavNotlari())
print(user3.ortAl())

print(user1.info())
print(user2.info())
print(user3.info())
print(user4.info())

























