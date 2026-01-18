from colorama import init, Back, Style
init()

items = []

def get_name():
    while True:
        name = input('enter the product name here: ').strip()
        if name.replace(' ', '').isalpha():
            return name
        else:
            print('enter a valid product name')
        
def get_price():
    while True:
        try:
            price = float(input('enter the price of the respective product: R$'))
            if price < 0:
                print('enter a valid value (+0)')
                continue
            else:
                return price
        except ValueError:
            print('enter a valid value')

print(f'{Back.BLUE}============= PEOPLE STORE ============={Style.RESET_ALL}')
         
while True:
    
    name = get_name()
    price = get_price()
    
    items.append({'name': name , 'price': price}) #'name' and 'price' is key.   name and price is value.
    
    repeat = input('do you want continue? (yes/no): ')
    if repeat.lower() == 'yes':
        continue
    elif repeat.lower() == 'no':
        print(f'your list: {items}')
        print(f'your total cost was: R${sum(p['price']for p in items)}') #sum the value associated with the key 'price' of each p with in items.
        print(f'The cheapest product cost: R${min(p['price']for p in items)}') #take the lowest value associated with the key 'price' of each p with in items.
        break
    else:
        while repeat.lower() not in ('yes' , 'no'):
            repeat = input('enter a valid option plis (yes/no): ')