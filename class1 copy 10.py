import inspect
import re


def extract_attributes(cls_name):
    cls = globals()[cls_name]
    cls_def = inspect.getsource(cls)
    pattern = r"def __init__\((.*?)\)"
    match = re.search(pattern, cls_def)
    if match:
        attrs = match.group(1).split(',')
        return tuple(attr.strip().strip("'") for attr in attrs[1:])


class Item:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value


attributes = extract_attributes('Item')
print(attributes)
print(type(attributes))


class Weapon (Item):
    def __init__(self, damage, *attributes):
        super().__init__(*attributes)
        self.damage = damage


# You can now create an instance of the Weapon class by passing the arguments in the order they are defined in the class definition
redsword = Weapon(25, "redsword", 250, 18)
print(attributes)
print(redsword.__dict__)
