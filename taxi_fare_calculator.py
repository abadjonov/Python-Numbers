from num2words import num2words

# 1. Masofani kiritish
distance = float(input("Masofani kiriting (km): "))

total_price = 3.00 + (distance * 1.20)

total_price = round(total_price, 2)

words_en = num2words(total_price, lang='en')
words_ru = num2words(total_price, lang='ru')

print(f"${total_price:.2f} ({words_en}, {words_ru})")