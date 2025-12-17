class Carditem() :
    items_count = 0
    discount_rate = 0.8
    
    @classmethod
    def display_items_count(cls):
        return Carditem.items_count  

    @classmethod
    def create_item(cls,data_str):
        name,price,quantity = data_str.split(",")
        return cls(name,price,quantity)
        
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Carditem.items_count +=1
        """_summary_
        """        
        
    
    def calculate_total(self):
        return self.price * self.quantity
        
        
    def apply_discount(self):
        self.price = self.price * Carditem.discount_rate
        
        
# name = input("ismi nedir: ")
# price = int(input("fiyatı nedir: "))
# quantity = int(input("kaç adet aldınız: "))

name = "bilgisayar"
price = 50000
quantity = 2


item1 = Carditem(name,price,quantity)

item1.apply_discount()

item2 = Carditem("telefon",25000,2)
# item2 = Carditem.create_item("telefon,25000,3")#input("ismini fiyatını adedini giriniz: "))
item2.apply_discount()

item3 = Carditem("laptop",40000,1)
item3.apply_discount()

# print(item1.calculate_total())
# print(item1.display_items_count())
        
class Shoppingcard():
    
    def __init__(self,liste):
        self.liste=liste
        
        
    def add_item(self,item):
        self.liste.append(item)
        
    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
        
sc = Shoppingcard([item1,item2])
sc.add_item(item3)
sc.display_items()
    


        
        