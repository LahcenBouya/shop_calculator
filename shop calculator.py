

print("***welcome to shop calculator***")
basket = []
price = []
items = int(input("how many items are there in your basket today?  "))
print("let's get to counting them....")
for i in range(items):
    name_of_item = input(f"please tell me the name of the item number {i + 1}: ").lower()
    his_price = float(input(f"what is the price of {name_of_item}: "))
    basket.append(name_of_item)
    price.append(his_price)

see_basket = input("would you like to see your entire basket item?: ").lower()

if see_basket == "yes":
    print(basket)

total_price = input("would you like to see how much it'll cost? ").lower()

if total_price == "yes":
    print(sum(price))

print("thanks for using our app")