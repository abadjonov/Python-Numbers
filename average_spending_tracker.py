
from num2words import num2words

qiymat1 = float(input("1-kun: "))
qiymat2 = float(input("2-kun: "))
qiymat3 = float(input("3-kun: "))
qiymat4 = float(input("4-kun: "))
qiymat5 = float(input("5-kun: "))
qiymat6 = float(input("6-kun: "))
qiymat7 = float(input("7-kun: "))

avg = round((qiymat1 + qiymat2 + qiymat3 + qiymat4 + qiymat5 + qiymat6 + qiymat7) / 7, 2)

print("O'rtacha harajat: $", avg)
print(num2words(avg))
print(num2words(avg, lang='ru'))