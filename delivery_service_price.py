from num2words import num2words

distance = float(input("Masofani kiriting (km): "))

total_price = 5.00 + (distance * 0.80)

total_price = round(total_price, 2)

words_en = num2words(total_price, lang='en')
words_ru = num2words(total_price, lang='ru')

print(f"${total_price:.2f} ({words_en}, {words_ru})")