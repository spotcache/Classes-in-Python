class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int, cd: float) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        self.cd = cd

iron_sword = weapon(name='Iron Sword',
                    weapon_type = 'Sharp',
                    damage = 5,
                    value = 10,
                    cd = 0.5)   

short_bow = weapon(name='Short Bow',
                    weapon_type = 'Ranged',
                    damage = 4,
                    value = 8,
                    cd = 1.0)

fists = weapon(name='Fists',
                    weapon_type = 'Blunt',
                    damage = 2,
                    value = 0,
                    cd = 0.5)     

diamond_sword = weapon(name = 'Diamond Sword',
                    weapon_type = 'Very Sharp',
                    damage = 10,
                    value = 20,
                    cd = 0.2)

cross_bow = weapon(name = 'Cross Bow',
                    weapon_type = 'Long Ranged',
                    damage = 8,
                    value = 16,
                    cd = 2.0)    

pistol = weapon(name = 'Pistol',
                    weapon_type = 'Long Range',
                    damage = 20,
                    value = 40,
                    cd = 1.5)

awm = weapon(name = 'AWM',
                    weapon_type = 'Sniper Rifle',
                    damage = 40,
                    value = 60,
                    cd = 5.0)