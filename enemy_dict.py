'''
enemy_dict.py - Dictionary of all the enemies in the simulation,
along with a way to get all the names.
'''

enemy_dict = {
    'slime': {
        'name': "Slime",
        'strength': 5,
        'agility': 3,
        'hp': 3,
        'sleepR': 0,
        'stopR': 15,
        'hurtR': 0,
        'dodge': 1,
        'run': 0,
        'pattern': [{
            'id': 'attack',
            'weight': 100
            }]
      },
    'rslime': {
        'name': "Red Slime",
        'strength': 7,
        'agility': 3,
        'hp': 3,
        'sleepR': 0,
        'stopR': 15,
        'hurtR': 0,
        'dodge': 1,
        'pattern': [{ 'id': 'attack', 'weight': 100 }],
        'run': 0
  },
  'drakee': {
    'name': "Drakee",
    'strength': 9,
    'agility': 6,
    'hp': [5, 6],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "ghost": {
    'name': "Ghost",
    'strength': 11,
    'agility': 8,
    'hp': [6, 7],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 4,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "magician": {
    'name': "Magician",
    'strength': 11,
    'agility': 12,
    'hp': [10, 13],
    'sleepR': 0,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [
      { 'id': 'hurt', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "magidrakee": {
    'name': "Magidrakee",
    'strength': 14,
    'agility': 14,
    'hp': [12, 15],
    'sleepR': 0,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [
      { 'id': 'hurt', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "scorpion": {
    'name': "Scorpion",
    'strength': 18,
    'agility': 16,
    'hp': [16, 20],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "druin": {
    'name': "Druin",
    'strength': 20,
    'agility': 18,
    'hp': [17, 22],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "poltergeist": {
    'name': "Poltergeist",
    'strength': 18,
    'agility': 20,
    'hp': [18, 23],
    'sleepR': 0,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 6,
    'pattern': [
      { 'id': 'hurt', 'weight': 75 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "droll": {
    'name': "Droll",
    'strength': 24,
    'agility': 24,
    'hp': [19, 25],
    'sleepR': 0,
    'stopR': 14,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "drakeema": {
    'name': "Drakeema",
    'strength': 22,
    'agility': 26,
    'hp': [16, 20],
    'sleepR': 2,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 6,
    'pattern': [
      { 'id': 'heal', 'weight': 25 },
      { 'id': 'hurt', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "skeleton": {
    'name': "Skeleton",
    'strength': 28,
    'agility': 22,
    'hp': [16, 20],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 4,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "warlock": {
    'name': "Warlock",
    'strength': 28,
    'agility': 22,
    'hp': [23, 30],
    'sleepR': 3,
    'stopR': 1,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [
      { 'id': 'sleep', 'weight': 25 },
      { 'id': 'hurt', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "mscorpion": {
    'name': "Metal Scorpion",
    'strength': 36,
    'agility': 42,
    'hp': [17, 22],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "wolf": {
    'name': "Wolf",
    'strength': 40,
    'agility': 30,
    'hp': [26, 34],
    'sleepR': 1,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 0
  },
  "wraith": {
    'name': "Wraith",
    'strength': 44,
    'agility': 34,
    'hp': [26, 34],
    'sleepR': 7,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 4,
    'pattern': [
      { 'id': 'heal', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "Metal Slime": {
    'name': "Metal Slime",
    'strength': 10,
    'agility': 255,
    'hp': 4,
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 15,
    'dodge': 1,
    'pattern': [
      { 'id': 'hurt', 'weight': 75 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "specter": {
    'name': "Specter",
    'strength': 40,
    'agility': 38,
    'hp': [28, 36],
    'sleepR': 3,
    'stopR': 1,
    'hurtR': 0,
    'dodge': 4,
    'pattern': [
      { 'id': 'sleep', 'weight': 25 },
      { 'id': 'hurt', 'weight': 75 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "wolflord": {
    'name': "Wolflord",
    'strength': 50,
    'agility': 36,
    'hp': [29, 38],
    'sleepR': 4,
    'stopR': 7,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [
      { 'id': 'stopspell', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "druinlord": {
    'name': "Druinlord",
    'strength': 47,
    'agility': 40,
    'hp': [27, 35],
    'sleepR': 15,
    'stopR': 0,
    'hurtR': 0,
    'dodge': 4,
    'pattern': [
      { 'id': 'heal', 'weight': 75 },
      { 'id': 'hurt', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 0
  },
  "drollmagi": {
    'name': "Drollmagi",
    'strength': 52,
    'agility': 50,
    'hp': [29, 38],
    'sleepR': 2,
    'stopR': 2,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [
      { 'id': 'stopspell', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 1
  },
  "wyvern": {
    'name': "Wyvern",
    'strength': 56,
    'agility': 48,
    'hp': [32, 42],
    'sleepR': 4,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "rogue_scorpion": {
    'name': "Rogue Scorpion",
    'strength': 60,
    'agility': 90,
    'hp': [27, 35],
    'sleepR': 7,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 2,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "w_knight": {
    'name': "Wraith Knight",
    'strength': 68,
    'agility': 56,
    'hp': [35, 46],
    'sleepR': 5,
    'stopR': 0,
    'hurtR': 3,
    'dodge': 4,
    'pattern': [
      { 'id': 'heal', 'weight': 75 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 1
  },
  "golem": {
    'name': "Golem",
    'strength': 120,
    'agility': 60,
    'hp': [53, 70],
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 15,
    'dodge': 0,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "goldman": {
    'name': "Goldman",
    'strength': 48,
    'agility': 40,
    'hp': [38, 50],
    'sleepR': 13,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "knight": {
    'name': "Knight",
    'strength': 76,
    'agility': 78,
    'hp': [42, 55],
    'sleepR': 6,
    'stopR': 7,
    'hurtR': 0,
    'dodge': 1,
    'pattern': [
      { 'id': 'stopspell', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 1
  },
  "magiwyvern": {
    'name': "Magiwyvern",
    'strength': 78,
    'agility': 68,
    'hp': [44, 58],
    'sleepR': 0,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 0,
    'pattern': [
      { 'id': 'sleep', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 1
  },
  "d_knight": {
    'name': "Demon Knight",
    'strength': 79,
    'agility': 64,
    'hp': [38, 50],
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 15,
    'dodge': 15,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "werewolf": {
    'name': "Werewolf",
    'strength': 86,
    'agility': 70,
    'hp': [46, 60],
    'sleepR': 7,
    'stopR': 15,
    'hurtR': 0,
    'dodge': 7,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 1
  },
  "Green Dragon": {
    'name': "Green Dragon",
    'strength': 88,
    'agility': 74,
    'hp': [49, 65],
    'sleepR': 7,
    'stopR': 15,
    'hurtR': 2,
    'dodge': 2,
    'pattern': [
      { 'id': 'fire', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 2
  },
  "starwyvern": {
    'name': "Starwyvern",
    'strength': 86,
    'agility': 80,
    'hp': [49, 65],
    'sleepR': 8,
    'stopR': 0,
    'hurtR': 1,
    'dodge': 2,
    'pattern': [
      { 'id': 'healmore', 'weight': 75 },
      { 'id': 'fire', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 2
  },
  "wizard": {
    'name': "Wizard",
    'strength': 80,
    'agility': 70,
    'hp': [49, 65],
    'sleepR': 17,
    'stopR': 7,
    'hurtR': 15,
    'dodge': 2,
    'pattern': [
      { 'id': 'hurtmore', 'weight': 50 },
      { 'id': 'attack', 'weight': 50 }
    ],
    'run': 2
  },
  "axe_knight": {
    'name': "Axe Knight",
    'strength': 94,
    'agility': 82,
    'hp': [53, 70],
    'sleepR': 15,
    'stopR': 3,
    'hurtR': 1,
    'dodge': 1,
    'pattern': [
      { 'id': 'sleep', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 2
  },
  "blue_dragon": {
    'name': "Blue Dragon",
    'strength': 98,
    'agility': 84,
    'hp': [53, 70],
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 7,
    'dodge': 2,
    'pattern': [
      { 'id': 'fire', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 2
  },
  "stoneman": {
    'name': "Stoneman",
    'strength': 100,
    'agility': 40,
    'hp': [121, 160],
    'sleepR': 2,
    'stopR': 15,
    'hurtR': 7,
    'dodge': 1,
    'pattern': [{ 'id': 'attack', 'weight': 100 }],
    'run': 3
  },
  "armored_knight": {
    'name': "Armored Knight",
    'strength': 105,
    'agility': 86,
    'hp': [68, 90],
    'sleepR': 15,
    'stopR': 7,
    'hurtR': 1,
    'dodge': 2,
    'pattern': [
      { 'id': 'healmore', 'weight': 75 },
      { 'id': 'hurtmore', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 3
  },
  "red_dragon": {
    'name': "Red Dragon",
    'strength': 120,
    'agility': 90,
    'hp': [76, 100],
    'sleepR': 15,
    'stopR': 7,
    'hurtR': 15,
    'dodge': 2,
    'pattern': [
      { 'id': 'sleep', 'weight': 25 },
      { 'id': 'fire', 'weight': 25 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'run': 3
  },
  "dragonlord_first": {
    'name': "Dragonlord (first form)",
    'strength': 90,
    'agility': 75,
    'hp': [76, 100],
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 15,
    'dodge': 0,
    'pattern': [
      { 'id': 'stopspell', 'weight': 25 },
      { 'id': 'hurtmore', 'weight': 75 },
      { 'id': 'attack', 'weight': 100 }
    ],
    'voidCrit': True,
    'run': 3
  },
  "Dragonlord (second form)": {
    'name': "Dragonlord (second form)",
    'strength': 140,
    'agility': 200,
    'hp': 130,
    'sleepR': 15,
    'stopR': 15,
    'hurtR': 15,
    'dodge': 0,
    'pattern': [
      { 'id': 'strongfire', 'weight': 50 },
      { 'id': 'attack', 'weight': 100 }
    ],
    "voidCrit": True,
    'run': 3
  }
}

e_strings = []

for k, v in enemy_dict.items():
    e_strings.append(v["name"])
