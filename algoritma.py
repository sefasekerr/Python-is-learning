

def order_total(order):
    subtotal = 0
    for i in order:
        a = float(i[1])
        subtotal +=a
    return subtotal    


def order_discount(subtotal):
    if subtotal>50:
        rate = 0.15
        discount = subtotal*rate
        return discount
    elif subtotal > 25:
        rate = 0.10
        discount = subtotal*rate
        return discount
    else :
        discount = subtotal
        return discount

def display_order(order):
    for x in order:
        print(f"{x[0]:<10}:{x[1]:>6}")

    
def menu_list():
    with open("menu.txt","r",encoding="utf-8")as file:
        menu = file.readlines()
        print(f"_____Şeker Pastanesine HOŞGELDİNİZ____")
        for item in menu:
            item = item.strip()
            
            index,urun,fiyat = item.split(":")
            print(f"{index}-{urun.strip():<10}:{fiyat.strip():>6}")


def take_order():
    menu_list()
    order = []
    my_dict = {}
    with open("menu.txt","r",encoding="utf-8") as file:
        for item in file.readlines():
            item = item.strip()
            index,urun,fiyat = item.split(":")
            my_dict[index.strip()]= (urun.strip(),fiyat.strip())
    for x in range(1,4):
        siparis = input(f"menüden numarayı seçin {x}.sipariş (1 ile {len(my_dict)} arasında): ")
        if siparis in my_dict:
            urun,fiyat = my_dict[siparis]
            order.append((urun,fiyat)) 

    return order
    
    
    
    
    pass

order = take_order()
display_order(order)
subtotal = order_total(order)
discount = order_discount(subtotal)

print(f"toplam tutarınız {subtotal-discount}")


