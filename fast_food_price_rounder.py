from num2words import num2words

price01 = float(input("1-mahsulot: "))
price02 = float(input("2-mahsulot: "))
price03 = float(input("3-mahsulot: "))

total_price = round(price01 + price02 + price03, 2)
rounded_price = round(total_price, 1)

print("Umumiy narx: $", total_price)
print(num2words(int(total_price)), num2words(int(total_price), lang='ru'))

print("Yaxlitlangan narx: $", rounded_price)
print(num2words(int(rounded_price)), num2words(int(rounded_price), lang='ru'))