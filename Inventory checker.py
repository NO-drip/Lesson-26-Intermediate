items = ["laptop","glue","books","pencils","pens","erasers"]
stock_count = [5,2,0,8,9,6]
inventory = {x:count for x, count in zip(items,stock_count)}
print("The stock of these items is:",inventory)

in_stock_item = [x for x in inventory if inventory[x]>0]
print("The items in stock are",in_stock_item)

chosen_item = input("Which item would you like to buy?")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print("Item is not there!")
    exit()

prices = [2,4,5,8,9]
markup = int(input("Enter the markup price."))

markup_price = list(map(lambda p: p + markup, prices))
print ("The marked up prices are:",markup_price)

index_item = items.index(chosen_item)
chosen_price = markup_price[index_item]
print("The price of your chosen item is:",chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1

print()
print("Item chosen",chosen_item)
print("Price of item",chosen_price)
print("Updated inventory:",inventory)
print("THANK YOU")