'''
model.py - Default model for the simulation
'''

from player import default_player

model = {
    "battleText": []
    ,"player": default_player
    ,"enemy": None
    ,"cleanText": False
    ,"inBattle": False
    ,"initiative": False
    ,"sleep_count": 6
    ,"critHit": False
}

if __name__ == '__main__':
    for key, value in model.items():
        print(key, ":", value)