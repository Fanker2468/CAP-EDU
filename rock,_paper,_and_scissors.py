import random
p_points = 0
ai_points = 0
#Приветствие
welcome = input('Здрасте, не хотите по играть со мной в камень(r), ножницы(s) и бумага(p)? (y/n):')
if welcome == 'n':
    print(":(")
else:
    print('играем до 3 раундов')

while p_points < 3 and ai_points < 3:
    marks = ('r','p','s')
    player = input('выбери "знак" (r/p/s);')
    ai = random.choice(marks)
    print(ai)
    if player == ai:
        print ("Ничья!")
    elif (player == 'r' and ai == 's') or (player == 's' and ai == 'p') or (player == 'p' and ai == 'r'):
        print("Одно очко тебе!")
        p_points += 1
    else:
        print("Одно очко мне!")
        ai_points += 1
if p_points > ai_points:
    print("Ты победил, поздравляю!")
else:
    print("Я победил! >:)")
