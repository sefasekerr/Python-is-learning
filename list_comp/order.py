menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99},
    6: {"name": 'kavun', "price": 1.99},
    7: {"name": 'karpuz', "price": 0.99},
    
}

def calculate_subtotal(order):
    total = 0
    for item in order:
        total += item['price']
    subtotal = round(total,2)
    return subtotal
    ### WRITE SOLUTION HERE

def calculate_discount(subtotal):
    if subtotal > 6:
        discount_rate= 0.15
        discount_total = round(subtotal*discount_rate,2)
        rate_total = discount_rate,discount_total
        return rate_total
    elif subtotal>3:
        discount_rate= 0.10
        discount_total = round(subtotal*discount_rate,2)
        rate_total = discount_rate,discount_total
        return rate_total
    else:
        rate_total = None
        return rate_total
          

def calculate_tax(subtotal):
    tax = subtotal * 0.15
    
    return round(tax,2)


def summarize_order(order):
    
    subtotal = calculate_subtotal(order) 
    tax = calculate_tax(subtotal)
    discount_total = calculate_discount(subtotal)
    if discount_total != None:
        total = round(subtotal + tax - discount_total[1],2)
    else:
        total= round(subtotal+tax,2)
    names = [item["name"] for item in order]
    liste = names,total
    return liste

    ### WRITE SOLUTION HERE


# This function is provided for you and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 7): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))
    
    
    discount = calculate_discount(subtotal)
    if discount !=None:
        print(f"You received a discount because your order is over $6. Discount rate:{discount[0]}\n"
              f"discount amount: {discount[1]}")

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    names, total = summarize_order(order)
    print(f"Order summary: Items: {names}, Total: {total}")

if __name__ == "__main__":
    main()
