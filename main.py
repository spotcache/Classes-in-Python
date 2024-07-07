import os # os for clearing the console
from character import * # custom module/class import
from weapon import * # custom module/class import

weapon_choices = ['is', 'ds', 'cb', 'ps', 'awm'] # weapon choices list

# defining enemy var with the enemy sub-class
enemy = Enemy(name = 'Enemy', health = 1000, weapon = pistol) 
if enemy.health == 0:
    exit('Enemy is DEAD!')

# defining hero var with the hero sub-class
hero = Hero(name = 'Hero', health = 1000)
if hero.health == 0:
    exit('Hero is DEAD!')
elif enemy.health == 0:
    exit('The hero WON!')

# taking input for hero's weapon
hero_weapon = input('Enter weapon to equip (is,ds,cb,ps,awm): ').lower()
# checking if choices listed are used
if hero_weapon == weapon_choices[0]:
    hero.equip(iron_sword)
elif hero_weapon == weapon_choices[1]:
    hero.equip(diamond_sword)
elif hero_weapon == weapon_choices[2]:
    hero.equip(cross_bow)
elif hero_weapon == weapon_choices[3]:
    hero.equip(pistol)
elif hero_weapon == weapon_choices[4]:
    hero.equip(awm)
elif hero_weapon != weapon_choices:
    print('Invalid Choice')

# setting an infinite loop
while True:
    # clearing the console on each input
    os.system('cls')
    # calling the attack sequence
    hero.attack(enemy)
    enemy.attack(hero)
    # drawing the health bar's for the characters
    hero.health_bar.draw()
    enemy.health_bar.draw()
    # receiving the input for attack
    input("Press any key to attack: ")