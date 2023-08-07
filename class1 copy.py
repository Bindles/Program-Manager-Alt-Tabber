import re
import inspect


class Item:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value


class Weapon (Item):
    def __init__(self, damage, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage


# Example usage:
redsword = Weapon(damage=25, name='redsword', cost=250, value=18)
# Output: {'name': 'redsword', 'cost': 250, 'value': 18, 'damage': 25}
print(redsword.__dict__)
