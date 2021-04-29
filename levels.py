'''
levels.py - Code that controls the player's level and resulting stats
'''


import math

levels = [
  [4, 4, 15, 0],
  [5, 4, 22, 0],
  [7, 6, 24, 5],
  [7, 8, 31, 16],
  [12, 10, 35, 20],
  [16, 10, 38, 24],
  [18, 17, 40, 26],
  [22, 20, 46, 29],
  [30, 22, 50, 36],
  [35, 31, 54, 40],
  [40, 35, 62, 50],
  [48, 40, 63, 58],
  [52, 48, 70, 64],
  [60, 55, 78, 70],
  [68, 64, 86, 72],
  [72, 70, 92, 95],
  [72, 78, 100, 100],
  [85, 84, 115, 108],
  [87, 86, 130, 115],
  [92, 88, 138, 128],
  [95, 90, 149, 135],
  [97, 90, 158, 146],
  [99, 94, 165, 153],
  [103, 98, 170, 161],
  [113, 100, 174, 161],
  [117, 105, 180, 168],
  [125, 107, 189, 175],
  [130, 115, 195, 180],
  [135, 120, 200, 190],
  [140, 130, 210, 200]
]

# Now for the silly level mod by name bit of the sim.

def slow_prog(name_sum, stat):
    '''
    Formula for lower stats
    '''
    return math.floor(stat * (9 / 10) + (math.floor(name_sum / 4) % 4))

def letter_stat(ltr):
    '''
    Calculates letter values of the name for stat calculations
    '''
    ltr_clusters = ["gwM", "hxN", "iyO", "jzP", "kAQ", "lBR", "mCS", "nDT", "oEU", "pFV", "aqGW",
    "brHX", "csIY", "dtJZ", "euK", "fvL"]
    for index, cluster in enumerate(ltr_clusters):
        if ltr in cluster:
            return index
    return 0

def progress_mods(name):
    '''
    Calcualte name_sum and the progression modifier
    '''
    letters = name[0:4]
    name_sum = sum(map(letter_stat, letters))
    return (name_sum, math.floor(name_sum % 4))

def level_up(model):
    '''
    Main level up function
    '''
    level_base = levels[int(model["level"]) - 1]
    name_sum, prog = progress_mods(model["name"])
    if prog == 0:
        model["strength"] = slow_prog(name_sum, level_base[0])
        model["agility"] = slow_prog(name_sum, level_base[1])
        model["maxhp"] = level_base[2]
        model["mp"] = level_base[3]
    elif prog == 1:
        model["strength"] = level_base[0]
        model["agility"] = slow_prog(name_sum, level_base[1])
        model["maxhp"] = level_base[2]
        model["mp"] = slow_prog(name_sum, level_base[3])
    elif prog == 2:
        model["strength"] = slow_prog(name_sum, level_base[0])
        model["agility"] = level_base[1]
        model["maxhp"] = slow_prog(name_sum, level_base[2])
        model["mp"] = level_base[3]
    else:
        model["strength"] = level_base[0]
        model["agility"] = level_base[1]
        model["maxhp"] = slow_prog(name_sum, level_base[2])
        model["maxmp"] = slow_prog(name_sum, level_base[3])
    model["hp"] = model["maxhp"]
    model["mp"] = model["maxmp"]
    model["p_magic"] = build_p_magic_list(model["level"])
    return model


def build_p_magic_list(level):
    '''
    Create a list of available spells based on level
    '''
    level = int(level)
    m_list = []
    if level >= 3:
        m_list.append("Heal")
    if level >= 4:
        m_list.append("Hurt")
    if level >= 7:
        m_list.append("Sleep")
    if level >= 10:
        m_list.append("Stopspell")
    if level >= 17:
        m_list.append("Healmore")
    if level >= 19:
        m_list.append("Hurtmore")
    return m_list
