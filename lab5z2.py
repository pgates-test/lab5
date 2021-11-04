from numpy import random
from datetime import datetime

z = open('rand.txt', 'w').close()
f = open("rand.txt", "a")
j = 0
i = 0
while i < 1:
    date_time = datetime.now()
    rand1 = random.randint(1, 7)
    rand2 = random.randint(1, 7)
    now = date_time.strftime("%m/%d/%Y, %H:%M:%S")

    if rand1 == rand2 == 6:
        print(rand1, rand2, now)
        print("liczba rzutow: ", j + 1)
        f.write(str(rand1))
        f.write(" ")
        f.write(str(rand2))
        f.write(" ")
        f.write(str(now))
        i = i + 1
        break

    f.write(str(rand1))
    f.write(" ")
    f.write(str(rand2))
    f.write(" ")
    f.write(str(now))
    f.write("\n")
    j = j + 1

f.close()
