homyak = {"HP": 100, "stamina": 50, "damage": 35, "mana": 100}
humster = {"HP": 250, "stamina": 80, "damage": 50, "mana": 100}

#atack
def attack(pers,enemy):
    if pers["stamina"] > 5:
        enemy["HP"] -= pers["damage"]
        pers["stamina"] -= 5
    else:
        pers["HP"] -= 25
#строка информации
def show_info():
    print(f"homyak HP - {homyak['HP']} ST - {homyak['stamina']}")
    print(f"humster HP - {humster['HP']} ST - {humster['stamina']}")
    print("===================================================")


#Восстановление сил
def rest(pers):
    pers["stamina"] += 10


#Восстановление здоровья
def heal(pers):
    pers["HP"] += 50


#Магический урон
def mag_damage(pers, enemy):
    enemy["HP"] -= 100


#Критический урон
def crit_damage(pers, enemy):
    pers["HP"] -= 50


#Процесс игры
while True:
    action1 = input("Введите действия для homyak (a, r, h, m): ")
    action2 = input("Введите действия для humster (a, r, h, c): ")
    if action1 == "a":
        attack(homyak, humster)
    elif action1 == "r":
        rest(homyak)
    elif action1 == "h":
        heal(homyak)
    else:
        print("Неверное действие")

    if action2 == "a":
        attack(homyak, humster)
    elif action2 == "r":
        rest(humster)
    elif action2 == "h":
        heal(humster)
    else:
        print("Неверное действие")

    show_info()

    if homyak["HP"] <= 0:
        print("Хомяк сдох")
        break
    elif humster["HP"] <= 0:
        print("Хамстер сдох")
        break



