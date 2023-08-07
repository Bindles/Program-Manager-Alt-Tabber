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
type(attributes)
