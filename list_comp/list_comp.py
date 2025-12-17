# #sonuc =[sayi for sayi in range(1,100) if sayi %12 ==0]
# text = "Hello 12345 World"
# sonuc =[i for i in text if (i.isdigit())]
# print(sonuc)
# # sonuc = [harf for harf in text if (int(harf)) ]
# # print(sonuc)    
  
# sicakliklar = [20,15,0,-5,-2]

# sicaklik = [derece  if (derece>4) else f"buzlanma tehlikesi {derece}"for derece in sicakliklar]

# print(sicaklik)

# ogrenciler = ["ali","ahmet","ömer"]
# notlar = [50,60,80]

# nots=dict(zip(ogrenciler,notlar))

# print(nots)

# result = [v for v in nots.items() if v[1]>50]
# print(result)

# notlar = [45, 67, 89, 32, 76, 90, 55]

# # 50 ve üzeri notları list comprehension ile filtrele
# gecenler = [n for n in notlar if n >= 50]

# # Ortalama (sum built-in fonksiyonu)
# ortalama = sum(gecenler) / len(gecenler)

# # En yüksek not (max built-in fonksiyonu)
# en_yuksek = max(gecenler)

# print("Geçenler:", gecenler)
# print("Ortalama:", ortalama)
# print("En yüksek:", en_yuksek)

# """
# - 1’den 10’a kadar sayılar üret.
# - Çift sayıların karelerini al.
# - Lambda ile küpünü hesapla.
# - map ve filter built-in fonksiyonlarını kullan.
# """

# sayi = list(range(1,11))
# cift_sayi = [x**2 for x in sayi if x % 2==0]
# cift_say = list(filter(lambda i: i%2==0,sayi))
# kup_sayi = list(map(lambda a : a**3,sayi))
# print(sayi)
# print(kup_sayi)
# print(cift_say)



"""r paragraf içindeki kelimeleri analiz et:
- Kelimeleri listele.
- Uzunluğu 5’ten büyük olanları filtrele.
- Lambda ile alfabetik sıralama yap.
- len() ve set() built-in fonksiyonlarını kullan

"""
# metin = "Python programlama dili güçlü ve esnek bir dildir"

# kelimeler = metin.split()

# sonuc = list(filter(lambda a : len(a)>5,kelimeler))

# result = list(sorted(kelimeler,key=lambda x:x.lower()))

# uniq= set(result)
# print(uniq)

# print(result)
# print(sonuc)

"""
metin = "Python programlama dili güçlü ve esnek bir dildir"

Bir şirkette çalışanların maaşlarını analiz et:
- Maaşları liste comprehension ile vergiden sonra hesapla (%20 kesinti).
- Lambda ile en yüksek maaşı bul.
- min(), max(), sum() built-in fonksiyonlarını kullan.

"""
# maaslar = [5000, 7000, 8000, 4500, 10000]

# net_maaslar = [maas*0.80 for maas in maaslar]

# max_maas = max(net_maaslar,key=lambda a:a)

# zamli_maas = [maas*1.2 for maas in net_maaslar if maas <6000]

# print(f"zam yapılan maaslar {zamli_maas}")
# print(net_maaslar)
# print(max_maas)
# """
# Bir sosyal medya uygulamasında kullanıcı yaşlarını analiz et:
# - 18 yaşından küçükleri filtrele.
# - Lambda ile yaşları küçükten büyüğe sırala.
# - any() ve all() built-in fonksiyonlarıyla kontrol yap.

# """


# yaslar = [15, 22, 30, 17, 40, 19]

# resit_yaslar = [yas for yas in yaslar if yas>=18]

# sirali_yaslar = sorted(resit_yaslar,key=lambda a:a)


# is_age = any(y<=18 for y in yaslar)
# is_long_age =  all(y>=18 for y in yaslar)


# print(resit_yaslar)
# print(sirali_yaslar)
# print(is_age)
# print(is_long_age)
# sayi = int(input("sayı girin: "))

# match sayi:
#     case 1:
#         print("sayı 1")
        
    # case 2:
    #     print("sayi 2")

# with open("text.txt","r+",encoding="utf-8") as f:
#     for i in range(10):
#         for j in range(10):
            
#             print(j,end=" ")
            
#         print(" ")
        
# import time

# for i in range(5):
#     print(i, end=" ", flush=True)  # çıktılar hemen yazılır
#     time.sleep(1)

# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]


# for i,num in enumerate(num_list):
#     print(num)
#     if num ==36:
#         print(f"konumda bulundu { i }")
#     elif num>45:
#         print(f"45 in üzerinde: {num}")
#     elif num<=45:
#         print(f"45 in altında {num}")
# def count_up_to(n):
#     for number in range(1, n + 1):
#         yield print(number)
# print(count_up_to(5))

# fiyatlar = [215.10,250.85,650,985.41]

# indirimli_fiyat  = list(map(lambda x : x * 0.9 , fiyatlar))
# print(indirimli_fiyat)


# notlar = [ 90 , 80, 70 ,60 , 50 ,80 ,95 ]

# str_notlar = list(map(lambda x : str(x),notlar ))

# print(str_notlar)

# gecen_notlar = list(filter(lambda x : x>50,notlar))

# print(gecen_notlar)


# yuz_varmi =[10,50,90,99,88,66,55,40,80,33,20,15]

# q = all(a for a in yuz_varmi if yuz_varmi ==100)
# print(q)


# alpha = "q w e r t y u ı o p ğ ü a s d f g h j k l ş i z x c v b n m ö ç"
# char_alpha = alpha.split(" ")
# sirali_alpha = sorted(char_alpha)
# print(sirali_alpha)

total = 12.1684
print(f"{total,2}")

