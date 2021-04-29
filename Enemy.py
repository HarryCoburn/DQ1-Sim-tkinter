import random

def prep_enemy(enemy):
    battle_vars = {"e_sleep": 0, "e_stop": False}
    new_enemy = {**enemy, **battle_vars}
    if type(new_enemy["hp"]) is list:
        new_enemy["hp"] = random.randint(new_enemy["hp"][0], new_enemy["hp"][1])
        new_enemy["maxhp"] = new_enemy["hp"]
    return new_enemy
