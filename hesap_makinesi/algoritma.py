def order_list(order):
    pass

def order_total(order):
    pass

def order_tax(subtotal):
    pass
def display_order(order):
    items = []
    with open("menu.txt","r",encoding="utf-8")as file:
        menu = file.readlines()
        for item in menu:
            item = item.strip()
            if ":" in item:
                index,urun,fiyat =item.split(":")
                index = index.strip()
                if index in order:
                    items.append(f"{urun}-{fiyat}")
                
        return items
    
    pass
    
def menu_list():
    liste = []
    with open("menu.txt","r",encoding="utf-8")as file:
        menu = file.readlines()
        print(f"_____Şeker Pastanesine HOŞGELDİNİZ____")
        for item in menu:
            item = item.strip()
            
            if ":"in item:
                index,urun,fiyat = item.split(":")
                print(f"{index}-{urun.strip():<10}:{fiyat.strip():>6}")
            
        
    pass

def take_order():
    menu_list()
    order = []
    count=1
    with open("menu.txt","r",encoding="utf-8") as file:
        for item in file.readlines():
            item = item.strip()
            index,urun,fiyat = item.split(":")
        for x in range(3):
            siparis = int(input(f"menüden numarayı seçin {count}.sipariş (1 ile 6 arasında): "))
            count += 1
            order.append(siparis)
        return order
    
    
    
    
    pass

order = take_order()
print(display_order(order))



