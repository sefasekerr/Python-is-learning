import  datetime as dt
import time
import sys
import os



# def main():
#     def gunaydin(isim):
#         return f"günaydın {isim}"

#     def oglen(isim):
#         return f"tünaydın {isim}"

#     def aksam(isim):
#         return f"iyi akşamlar {isim}"

#     def gece(isim):
#         return f"iyi geceler {isim}"
#     #isim = input("isimiz nedir: ")
#     if 0<= dt.datetime.now().hour <5 :
#         return gece
#     if 5<= dt.datetime.now().hour < 12:
#         return gunaydin
#     if 12<= dt.datetime.now().hour < 18:
#         return oglen
    
#     if 18<= dt.datetime.now().hour < 24:
#         return aksam



# print(main()(input("isimiz nedir: ")))


# def selamlam(fn):
#     def inner():
#         fn()
#         fn()
#     return inner

# @selamlam
# def gunaydin():
#     print(f"merhaba")
    
    
# @selamlam
# def iyi_gunler():
#     print(f"iyi günler")
    

# iyi_gunler()
# def speed_test(fn):
#     def inner(*args, **kwargs):
#         start_time= time.perf_counter()
#         fn(*args, **kwargs)
#         stop_time =time.perf_counter()
#         return f"geçen süre: {stop_time-start_time:.6f}"
#     return inner

# def speed_test1(fn,*args, **kwargs):
#     start=time.perf_counter()
#     fn(*args, **kwargs)
#     stop=time.perf_counter()
#     return f"geçen süre {stop-start:.6f}"
# @speed_test
# def sum_gen():
#     return sum((x for x in range(200000000)))

# # @speed_test
# def sum_list():
#     return sum([x for x in range(200000000)])

# # print(sum_list())

# print(speed_test1(sum_gen))
def de_speed_test(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            print(f"{fn.__name__} metodu çalışıyor...")
            for _ in range(count):
                start_time= time.perf_counter()
                fn(*args, **kwargs)
                stop_time =time.perf_counter()
                print(f"geçen süre {stop_time-start_time:.6f}")
            return fn(*args, **kwargs)
        return inner
    return speed_test


@de_speed_test(count=3)
def sum_gen():
    return sum((x for x in range(2000000)))

@de_speed_test(count=2)
def sum_list():
    return sum([x for x in range(2000000)])

sum_list()
print(sum_gen)










