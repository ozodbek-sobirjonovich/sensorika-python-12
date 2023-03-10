# 2-darsni uyga vazifasi. 01.

# ismi, familiyasi, email, parol = input(), input(), input(), input()

# ismi = input("Ismingiz nima?: ")
# familiyasi = input("Familiyangiz nima?: ")
# yili = int(input("Nechanchi yil tug'ilgansiz?: "))
# email = input("E-mail manzilini kiriting: ")
# parol = input("Parolingizni kiriting: ")

# print(f"Mening ismim {ismi} {familiyasi}. Mening yoshim {2023 - yili} da! E-pochta manzilim: {email}, uning paroli esa ****{parol[4:-2]}***")

# 2-darsni uyga vazifasi. 02.

# text = "Mexanizatsiyalashtirishmoqchiliginiaytganinisezibqoldimmikananimadeysanukaginam?"

# print(text[0:13])
# print(text[31:33] + text[13:15] + text[-2:-1])
# print(text[3:7][::-1])


# Konditsioner!
# temp = 15  # o'rtacha xarorat 20 daraja!
# konditsioner = ""

# if temp < 20:
#     konditsioner = "HOT!"
# elif temp == 20:
#     konditsioner = "NORM!"
# else:
#     konditsioner = "COOL!"

# print(konditsioner)

# obhavo = 20

# # Agar
# if obhavo <= 10:
#     print("Obhavo salqin")
# elif obhavo > 10:
#     if obhavo <= 20:
#         print("Obhavo iliq")
#     else:
#         print("Obhavo issiq")

#  1-topshiriq!

# Berilgan son TOQ yoki JUFT ekanligini aniqlovchi dastur tuzilsin!

# son = 21
# if son % 2 == 0:
#     print("JUFT")
# else:
#     print("TOQ")



# Odatiy holati
# power = "on"
# if power == "on":
#     print("Power ON!")
# else:
#     print("Power OFF!")

# Ternary operator
# power = "off"
# print("Power ON!" if power == "on" else "Power OFF!")

obhavo = 5

if obhavo <= 10:
    print("Obhavo salqin")
elif obhavo > 10 and obhavo <= 20:
    print("Obhavo iliq")
else:
    print("Obhavo issiq")
