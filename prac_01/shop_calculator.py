DISCOUNT_RATE = 0.1
DISCOUNT_THRESHOLD = 100
total_price = 0


number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price - total_price * DISCOUNT_RATE

print(f"Total price for {number_of_item} items is {total_price:.2f}")
