
from num2words import num2words

pul = int(input("Pul miqdorini kiriting ($): "))

b50 = pul // 50
pul = pul % 50

b10 = pul // 10
money = pul % 10

b5 = pul // 5
money = pul % 5

b1 = pul

total = b50*50 + b10*10 + b5*5 + b1

print(f"$50 kupyuradan: {b50} ta")
print(f"$10 kupyuradan: {b10} ta")
print(f"$5 kupyuradan: {b5} ta")
print(f"$1 kupyuradan: {b1} ta")
print(f"Umumiy summa: ${total} ({num2words(total)}, {num2words(total, lang='ru')})")