import re
import inspect


def extract_attributes(cls_name):
    cls = globals()[cls_name]
    cls_def = inspect.getsource(cls)
    pattern = r"def __init__\((.*?)\)"
    match = re.search(pattern, cls_def)
    if match:
        attrs_str = match.group(1)
        # Extract the default values for the attributes
        defaults = {}
        for attr in attrs_str.split(','):
            attr = attr.strip()
            if '=' in attr:
                name, default = attr.split('=')
                name = name.strip()
                default = default.strip()
                defaults[name] = default
        # Return a dictionary with the attribute names and default values
        return defaults


class Item:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value


attributes = extract_attributes('Item')


class Weapon (Item):
    def __init__(self, damage, **attributes):
        super().__init__(**attributes)
        self.damage = damage


# You can now create an instance of the Weapon class by passing the arguments in the order they are defined in the class definition
redsword = Weapon(25, name="redsword", cost=250, value=18)

print(redsword.__dict__)
