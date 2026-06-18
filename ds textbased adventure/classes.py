import random 
def classes():
    class Player:
        def __init__(self, name="Ashen One", hp=100, max_hp=100, attack_power=15):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power
            self.level = 1
            self.estus_flask = 3
            self.max_estus_flask = 3
            self.stamina = 100
            self.max_stamina = 100
            self.stamina_recovery = 15
            self.souls = 0

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, damage):
            self.hp = max(0, self.hp - damage)

        def recover_stamina(self, amount=None):
            if amount is None:
                amount = self.stamina_recovery
            self.stamina = min(self.max_stamina, self.stamina + amount)

        def spend_stamina(self, amount):
            if self.stamina < amount:
                return False
            self.stamina -= amount
            return True


    class Enemy:
        def __init__(self, name="Hollow", hp=40, max_hp=40, attack_power=5):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def __init__(self, name="Starved Hound", hp=25, max_hp=25, attack_power=10):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def __init__(self, name="Lothric Knight Sword", hp=85, max_hp=85, attack_power=25):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def __init__(self, name="Lothric Knight Spear", hp=75, max_hp=75, attack_power=30):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def __init__(self, name="Puss of Man", hp=135, max_hp=135, attack_power=55):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def __init__(self, name="Winged Knight", hp=100, max_hp=100, attack_power=40):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.attack_power = attack_power

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, damage):
            self.hp = max(0, self.hp - damage)


    class Boss(Enemy):
        def __init__(self, name="Iudex Gundyr", hp=120, max_hp=120, attack_power=15, heavy_attack_power=20):
            super().__init__(name=name, hp=hp, max_hp=max_hp, attack_power=attack_power)
            self.heavy_attack_power = heavy_attack_power
            self.phase = 1

        def update_phase(self):
            if self.hp <= self.max_hp // 2 and self.phase == 1:
                self.phase = 2
                print(f"\n{self.name} enters a more aggressive second phase!\n")

        def choose_attack_damage(self):
            self.update_phase()
            if self.phase == 1:
                return random.choice([self.attack_power, self.attack_power + 4])
            return random.choice([self.attack_power + 6, self.heavy_attack_power, self.heavy_attack_power + 4])


    class Second(Enemy):
        def __init__(self, name="Vordt of the Boreal Valley", hp=155, max_hp=155, attack_power=25, heavy_attack_power=40):
            super().__init__(name=name, hp=hp, max_hp=max_hp, attack_power=attack_power)
            self.heavy_attack_power = heavy_attack_power
            self.phase = 1

        def update_phase(self):
            if self.hp <= self.max_hp // 2 and self.phase == 1:
                self.phase = 2
                print(f"\n{self.name} enters a more aggressive second phase!\n")

        def choose_attack_damage(self):
            self.update_phase()
            if self.phase == 1:
                return random.choice([self.attack_power, self.attack_power + 6])
            return random.choice([self.attack_power + 8, self.heavy_attack_power, self.heavy_attack_power + 8])

    player = Player()
    return Player,Enemy,Boss,Second,player
