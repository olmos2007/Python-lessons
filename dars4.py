
# List - Royxat bolib, ko'plab obyektlarni chaqirish, ular ustida amallar bajarish uchun ishlatiladi
# 
# Listda element va objectlarni qabel qiladi 
# Element doim 0 dan boshlanadi
# list = ["asd", "gas", "hjyg"]
# tuple = ("fvc", "wfe", "wef")
# set = {"sfc", "sdc", "f"}
# print(list[0])

# a = input("Your name: ")
# print(a[0], a[-1])


# Python da len metodi bizga son yoki gapni,
# nechta harf yoki necha xonali son bolshiga shart qoyaolamiz len yordamida 
a = input("son: ")
if len(a) == 3:
    print(f"{a[0]}00 {a[1]}0 {a[2]}")
elif len(a) < 3:
    print("xatolik")
else:
    print("xatolik")

