sum=0
list_1 =[]
while True:
    item_price=input("[+] please enter the item price or q to quit :  ")
    if item_price == 'q':
        print(f"\n[+] Your bill amount is {sum} . Thanks for shopping here ")
        print (list_1)
        break        
    else:
        sum = sum+float(item_price)
        list_1.append(sum)
        print("order sum till now {}" .format(sum))
       


