from operator import __add__
from functools import reduce
# ==============================================================================
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
print(reduce( __add__, list( map( lambda x: x['length']*x['width'], rooms ) ) ) )


# ==============================================================================


def rooms_sqr(x):
    return x["length"] * x["width"]
# ==============================================================================


def union(a, b):
    return a + b


# ==============================================================================
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
print(reduce(union, list( map( rooms_sqr, rooms ) ) ) )