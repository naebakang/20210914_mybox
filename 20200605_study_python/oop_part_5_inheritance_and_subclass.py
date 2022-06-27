# File encoding: utf8


class Unit:
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life

    def show_status(self):
        print("name: {}".format(self.name))
        print("rank: {}".format(self.rank))
        print("size: {}".format(self.size))
        print("life: {}".format(self.life))


class Goblin(Unit):
    def __init__(self, rank, size, life, attack_type, damage):
        super(Goblin, self).__init__(rank, size, life)
        self.attack_type = attack_type
        self.damage = damage

    def show_status(self):
        super(Goblin, self).show_status()
        print("attack_type: {}".format(self.attack_type))
        print("damage: {}".format(self.damage))

    def attack(self, unit):
        unit.life = unit.life - self.damage
        print("Under the attack by [{}]!, damage of attacker: {}".format(self.name, self.damage))


class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        super(SphereGoblin, self).__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type

    def show_status(self):
        super(SphereGoblin, self).show_status()
        print("sphere type: {}".format(self.sphere_type))


goblin_1 = Goblin("soldier", "small", 100, "shorts", 10)
goblin_1.show_status()

print(Goblin.__dict__)
print(help(Goblin))
print(dir(Goblin))

sphere_goblin_1 = SphereGoblin("soldier", "small", 100, "range attack", 10, "long")
sphere_goblin_1.show_status()

sphere_goblin_1.attack(goblin_1)
goblin_1.show_status()
