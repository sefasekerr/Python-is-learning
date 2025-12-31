import models.odev as odev

class productHelper(odev.product):
    # def __init__(self, name="Default", price=0, quantity=1):
    #     super().__init__(name, price, quantity)
        
    @staticmethod
    def create_item_from_text(file_name):
        items=[]
        with open(file_name,"r+",encoding="utf-8") as file:
            for i,satir in enumerate(file.readlines()):
                satir =satir.strip()
                name,price,quantity = satir.split(",")
                price =float(price)
                quantity = int(quantity)
                items.append(odev.product(name,price,quantity))
            return items
    @staticmethod
    def get_total_balance(products):
        total = 0
        for product in products:
            total +=(product.price *product.quantity)  
        total_with_vat = total *1.2
        return total_with_vat
            
            

            
            
        
        
        


items =productHelper.create_item_from_text("Products.txt")

print(items)
print(productHelper.get_total_balance(items))