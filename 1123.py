import random

e_phone = [186,]
for i in range(8):
    e_phone.append(random.randrange(0,9))
print(e_phone)
phone = "".join([str(x) for x in e_phone])
print(phone)