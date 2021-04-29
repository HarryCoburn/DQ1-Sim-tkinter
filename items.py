'''
items.py - Lists of tuples for different item classes, plus string generation for item names.
Pattern of (name, modifer)
'''

weapons = [
    ("Unarmed", 0),
    ("Bamboo Pole", 2),
    ("Club", 4),
    ("Copper Sword", 10),
    ("Hand Axe", 15),
    ("Broad Sword", 20),
    ("Flame Sword", 28),
    ("Edrick's Sword", 40)
]

armors = [
    ("Naked", 0, False, False),
    ("Clothes", 2, False, False),
    ("Leather Armor", 4, False, False),
    ("Chain Mail", 10, False, False),
    ("Half Plate", 16, False, False),
    ("Full Plate", 24, False, False),
    ("Magic Armor", 24, True, False),
    ("Edrick's Armor", 28, True, True)
]


shields = [
    ("Naked", 0),
    ("Small Shield", 4),
    ("Large Shield", 10),
    ("Silver Shield", 25)
]

w_strings = [i for i, j in weapons]
a_strings = [i for i, j, k, l in armors]
s_strings = [i for i,j in shields]
