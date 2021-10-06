sum=0
i=1
dict_1 ={"Item_Name" : "Item_Price"}
while True:
    item_name =input("[+] please enter the Item Name or q to quit :  ")
        
    if item_name == 'q':
        print(f"\n[+] Your bill amount is {sum} . Thanks for shopping here \n")
        break        
    else:
        item_price =input("Please enter Item Price $ ")
        sum = sum+float(item_price)
        dict_1[item_name]= item_price
        print("order sum till now {}" .format(sum))

for key, value in dict_1.items():
    print("[+] {}" .format(i), key , "====>" ,value)
    i=i+1
    #i+=1

#===another way for for loop============
# for keys in dict_1:
#     print(keys, "====" ,dict_1[keys])

# for i in enumerate(dict_1.items()):
#     print (i)

