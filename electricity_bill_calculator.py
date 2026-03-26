from num2words import num2words

start = float(input("Oy boshidagi ko'rsatkich: "))
end = float(input("Oy oxiridagi ko'rsatkich: "))

total = end - start
price = round(total * 0.45, 2)

print(f"To'lov: ${price} ({num2words(price)}, {num2words(price, lang='ru')})")
