time = int(input("Сколько лет вы хотите рассматривать экспонаты?: "))
ex = 28000000
m = 5
d = 8*60*5
y = 8*60*365*5
years = time*y
print(str(years) + " экспонатов вы успеете посмотреть")

numb = int(input("Сколько экспонатов вы хотите посмотреть?: "))
numbm = numb*m
numbd = numb/d
numby = numb/y
if numb < d:
    print(str(numbm) + " минут вы потратите")
elif numb < y:
    print(str(numbd) + " дней вы потратите")
else:
    print(str(numby) + " лет вы потратите")
