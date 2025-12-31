import datetime as dt
try:
    class product():
        def __init__(self,name="Default",price=0.0,quantity=1):
            if 3<=len(name)<=30 and 0<=price and 1<=quantity:
                self.__name= name
                self.__price= price
                self.__quantity= quantity        
                print(f"{dt.date.today()} bu tahite {self.__name} isimli ürün oluşturuldu")
            else:
                raise ValueError("Ürün oluşturulamadı: geçersiz parametreler")

            
        @property
        def name(self):
            return self.__name
        @property
        def price(self):

            return self.__price
        @property
        def quantity(self):

            return self.__quantity
                
        def get_total_price(self):
            totat_price = self.__price * self.__quantity
            return totat_price
        

        def __repr__(self):
            if ( product != "oluşturulamadı"):
                return f"{self.__name}-{self.__price}-{self.__quantity}"
                
    item=product("ela")
    
except Exception as e:
    print(e)




        