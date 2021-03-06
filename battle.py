'''
battle.py - Battle code for DQ1 sim. Holds both player and enemy code.
'''


import random
import tkinter as tk
import view as View


class Battle():
    '''
    Main battle controller
    '''

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.output = model["output"]
        self.p = PlayerBattle(model["player"], self.output)
        self.e = None
        self.view.frames[View.BattleFrame].attack_btn.bind("<Button-1>", self.player_attack)
        self.view.frames[View.BattleFrame].herb_btn.bind("<Button-1>", self.use_herb)
        self.view.frames[View.BattleFrame].run_btn.bind("<Button-1>", self.run_away)
        self.view.frames[View.BattleFrame].cast_btn.bind("<Button-1>", self.player_cast_magic)
        self.fight_over = tk.BooleanVar()
        self.fight_over.set(False)
        self.herb_range = (23, 30)


    ## Core Fight Routines

    def setup_battle(self):
        '''Performs setup tasks for the battle prior to start'''
        self.view.update_ptext(self.p.model)
        self.view.update_magic()
        self.e = EnemyBattle(self.model["enemy"])
        self.view.show_frame(View.BattleFrame)
        self.output.clear()
        self.do_fight()

    def do_fight(self):
        '''Starts the battle loop'''
        p_turn = self.p.agi * random.randint(1,255) > self.e.agi * random.randint(1, 255) * 0.25

        self.view.main_frame.txt["state"] = 'normal'
        self.output.output = f'''You are fighting the {self.e.name}!\n'''
        #self.model["output"].output =

        if p_turn is False:
            self.output.output = f'''The {self.e.name} surprises you! Free attack!\n'''
            self.enemy_turn()
        else:
            self.player_turn()

    def end_fight(self):
        '''Triggers the flag that tells the controller battle is over'''
        self.fight_over.set(True)

    def player_turn(self):
        '''Runs at the start of player turn. Checks for sleep status and updates it, then waits for user to hit a button'''
        is_asleep = self.p.is_asleep()
        if is_asleep:
            self.enemy_turn()

    def crit(self):
        return random.randint(1,32) == 1

    def dodge(self, chance):
        return random.randint(1,64) <= chance

    def resist(self, chance):
        return random.randint(1,16) <= chance

    def damage_range(self,x,y):
        return (((x - y // 2) // 4), ((x - y // 2) // 2))

    def crit_range(self,x):
        return ((x//2), x)

    def weak_range(self, x):
        return (0, ((x+4) // 6))

    def player_attack(self, *_):
        e_dodged = self.dodge(self.model["enemy"]["dodge"])
        is_crit = self.crit()
        p_attack_stat = self.model["player"]["strength"] + self.model["player"]["weapon"][1]
        damage_dealt = 0
        x = 0
        y = 0

        if is_crit:
            x, y = self.crit_range(p_attack_stat)
        else:
            x, y = self.damage_range(p_attack_stat, self.model["enemy"]["agility"])

        if x < 0:
            x = 0
        if y < 0:
            y = 1

        damage_dealt = random.randint(x, y)

        if e_dodged:
            damage_dealt = 0

        if is_crit and not "voidCrit" in self.model["enemy"]:
            self.output.output = '\nYou attack with an excellent attack!!\n'
        else:
            self.output.output = '''\nYou attack!\n'''

        if e_dodged:
            self.output.output = f'''But the {self.model["enemy"]["name"]} dodged your attack!\n'''
            self.enemy_attack()
        else:
            self.output.output = f'''You hit {self.model["enemy"]["name"]} for {damage_dealt} points of damage!\n'''
            self.model["enemy"]["hp"] -= damage_dealt
            self.view.update_einfo(self.model["enemy"])
            self.is_enemy_defeated()

    def is_enemy_defeated(self):
        if self.model["enemy"]["hp"] <= 0:
            self.output.output = f'''You have defeated the {self.model["enemy"]["name"]}!\n'''
            self.end_fight()
        else:
            self.enemy_turn()

    def is_player_defeated(self):
        if self.model["player"]["hp"] <= 0:
            self.output.output = f'''You have been defeated by the {self.model["enemy"]["name"]}...'''
            self.end_fight()
        else:
            self.player_turn()

    def enemy_turn(self):
        ''' Enemy turn start'''
        if self.model["enemy"]["e_sleep"] > 0:
            self.enemy_asleep()
        elif self.model["player"]["strength"] > self.model["enemy"]["strength"] * 2 and random.randint(1,4) == 4:
            self.enemy_flees()
        else:
            chosen_attack = self.enemy_choose_attack()
            if chosen_attack == "attack":
                self.enemy_attack()
            elif chosen_attack == "hurt":
                self.enemy_casts_hurt(False)
            elif chosen_attack == "hurtmore":
                self.enemy_casts_hurt(True)
            elif chosen_attack == "heal":
                self.enemy_casts_heal(False)
            elif chosen_attack == "healmore":
                self.enemy_casts_heal(True)
            elif chosen_attack == "sleep":
                self.enemy_casts_sleep()
            elif chosen_attack == "stopspell":
                self.enemy_casts_stopspell()
            elif chosen_attack == "fire":
                self.enemy_breathes_fire(False)
            elif chosen_attack == "strongfire":
                self.enemy_breathes_fire(True)
            else:
                self.output.output = "Enemy tried to attack with something not programmed yet!!"

    def enemy_heal_thresh(self):
        return self.model["enemy"]["hp"] / self.model["enemy"]["maxhp"] < 0.25

    def enemy_choose_attack(self):
        atk_list = self.model["enemy"]["pattern"]
        choice = None
        for item in atk_list:
            chance = item["weight"]
            if random.randint(1,100) <= chance:
                if item["id"] == "attack":
                    choice = item["id"]
                    break
                if item["id"] == "hurt":
                    choice = item["id"]
                    break
                if item["id"] == "heal" and self.enemy_heal_thresh():
                    choice = item["id"]
                    break
                if item["id"] == "sleep" and self.model["player"]["p_sleep"] is False:
                    choice = item["id"]
                    break
                if item["id"] == "stopspell" and self.model["player"]["p_stop"] is False:
                    choice = item["id"]
                    break
                if item["id"] == "fire":
                    choice = item["id"]
                    break
                if item["id"] == "healmore" and self.enemy_heal_thresh():
                    choice = item["id"]
                    break
                if item["id"] == "hurtmore":
                    choice = item["id"]
                    break
                if item["id"] == "strongfire":
                    choice = item["id"]
                    break
        if choice is None:
            choice = "attack"
        return choice

    def enemy_flees(self):
        ''' Enemy runs away. End the combat'''
        self.output.output = f'''The {self.model["enemy"]["name"]} flees from your superior strength!'''
        self.fight_over.set(True)

    def enemy_asleep(self):
        ''' Handles the sleep logic when player puts the enemy to sleep'''
        if self.model["enemy"]["e_sleep"] == 2:
            self.model["enemy"]["e_sleep"] -= 1
            self.output.output = f'''The {self.model["enemy"]["name"]} is asleep'''
        else:
            if random.randint(1,3) == 3:
                self.output.output = f'''The {self.model["enemy"]["name"]} woke up!'''
                self.model["enemy"]["e_sleep"] = 0
                self.enemy_turn()
            else:
                self.output.output = f'''The {self.model["enemy"]["name"]} is still asleep...'''

    def enemy_attack(self):
        '''Enemy attacks normally'''
        self.output.output = '''\nEnemy turn\n'''
        hero_defense = (self.model["player"]["agility"] + self.model["player"]["armor"][1] + self.model["player"]["shield"][1]) // 2
        low = 0
        high = 0
        damage_dealt = 0
        if hero_defense > self.model["enemy"]["strength"]:
            low, high = self.weak_range(self.model["enemy"]["strength"])
            damage_dealt = random.randint(low, high)
        else:
            low, high = self.damage_range(self.model["enemy"]["strength"], hero_defense)
            damage_dealt = random.randint(low, high)

        self.model["player"]["hp"] -= damage_dealt
        self.view.update_ptext(self.model["player"])

        self.output.output = f'''{self.model["enemy"]["name"]} attacks! {self.model["enemy"]["name"]} hits you for {damage_dealt} damage.\n'''
        self.is_player_defeated()

    def enemy_casts_hurt(self, more):
        ''' Enemy handling of hurt and hurtmore'''
        spell_name = "Hurtmore" if more else "Hurt"
        if self.model["enemy"]["e_stop"]:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but their spell has been blocked!'''
            return

        hurt_high = [3, 10]
        hurt_low = [2, 6]
        hurtmore_high = [30, 45]
        hurtmore_low = [20, 30]

        mag_def = self.model["player"]["mag_def"]
        hurt_dmg = 0

        if mag_def and more:
            hurt_dmg = random.randint(hurtmore_low[0], hurtmore_low[1])
        elif mag_def and not more:
            hurt_dmg = random.randint(hurt_low[0], hurt_low[1])
        elif more:
            hurt_dmg = random.randint(hurtmore_high[0], hurtmore_high[1])
        else:
            hurt_dmg = random.randint(hurt_high[0], hurt_high[1])

        self.model["player"]["hp"] -= hurt_dmg
        self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}! {self.model["player"]["name"]} is hurt for {hurt_dmg} damage!'''
        self.is_player_defeated()

    def enemy_casts_heal(self, more):
        ''' Enemy handling of heal and healmore'''
        spell_name = "Healmore" if more else "Heal"
        if self.model["enemy"]["e_stop"]:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but their spell has been blocked!'''
            return

        heal_range = [20, 27]
        healmore_range = [85, 100]

        heal_max = self.model["enemy"]["maxhp"] - self.model["enemy"]["hp"]

        heal_rand = random.randint(healmore_range[0], healmore_range[1]) if more else random.randint(heal_range[0], heal_range[1])

        heal_amt = heal_rand if heal_rand < heal_max else heal_max

        self.model["enemy"]["hp"] += heal_amt
        self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}! {self.model["enemy"]["name"]} is healed {heal_amt} hit points!'''
        self.view.update_einfo(self.model["enemy"])
        self.player_turn()

    def enemy_casts_sleep(self):
        '''Enemy attempts to cast sleep'''
        spell_name = "Sleep"
        if self.model["enemy"]["e_stop"]:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but their spell has been blocked!'''
        else:
            self.p.asleep = True
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}. You fall asleep!!'''
        self.player_turn()

    def enemy_casts_stopspell(self):
        ''' Enemy attempts to cast stopspell. 50% chance of failure'''
        spell_name = "Stopspell"
        if self.model["enemy"]["e_stop"]:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but their spell has been blocked!'''
        elif random.randint(1,2) == 2:
            self.model["player"]["p_stop"] = True
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}! Your magic has been blocked!'''
        else:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but the spell fails!'''
        self.player_turn()

    def enemy_breathes_fire(self, more):
        ''' Enemy handling of breath attacks'''
        spell_name = "strong flames at you!" if more else "fire"
        if self.model["enemy"]["e_stop"]:
            self.output.output = f'''The {self.model["enemy"]["name"]} casts {spell_name}, but their spell has been blocked!'''
            return

        fire_high = [16, 23]
        fire_low = [10, 14]
        strongfire_high = [65, 72]
        strongfire_low = [42, 48]

        fire_def = self.model["player"]["fire_def"]
        fire_dmg = 0

        if fire_def and more:
            fire_dmg = random.randint(strongfire_low[0], strongfire_low[1])
        elif fire_def and not more:
            fire_dmg = random.randint(fire_low[0], fire_low[1])
        elif more:
            fire_dmg = random.randint(strongfire_high[0], strongfire_high[1])
        else:
            fire_dmg = random.randint(fire_high[0], fire_high[1])

        self.model["player"]["hp"] -= fire_dmg
        self.output.output = f'''The {self.model["enemy"]["name"]} breathes {spell_name}! {self.model["player"]["name"]} is hurt for {fire_dmg} damage!'''
        self.is_player_defeated()

    def use_herb(self, *_):
        ''' Handle herb consumption'''
        if self.model["player"]["herb_count"] <= 0:
            self.output.output = '''You have no herbs!'''
            return
        else:
            self.model["player"]["herb_count"] -= 1

        if self.model["player"]["hp"] >= self.model["player"]["maxhp"]:
            self.output.output = '''You eat a herb, but your hit points are already at maximum!\n'''
        else:
            low, high = self.herb_range
            heal_amt = random.randint(low, high)
            heal_diff = self.model["player"]["maxhp"] - self.model["player"]["hp"]
            if heal_diff < heal_amt:
                heal_amt = heal_diff
            self.model["player"]["hp"] += heal_amt
            self.output.output = f'''You eat a herb and regain {heal_amt} hit points!\n'''

        self.enemy_turn()

    def run_away(self, *_):
        '''Player attempts to flee battle.'''
        run_modifiers = [0.25, 0.375, 0.75, 1]
        p_run_chance = random.randint(0, 254)
        e_block_chance = random.randint(0, 254)
        e_block_mod = run_modifiers[self.model["enemy"]["run"]]
        self.output.output = '''You attempt to run away...\n'''
        succeed_flee = self.model["player"]["agility"] * p_run_chance > self.model["enemy"]["agility"] * e_block_chance * e_block_mod
        if succeed_flee:
            self.output.output = '''You successfully flee!\n'''
            self.end_fight()
        else:
            self.output.output = f'''...but the {self.model["enemy"]["name"]} blocks you from running away!\n'''
            self.enemy_turn()

    def player_cast_magic(self, *_):
        spell = self.view.chosen_magic.get()
        spell_switch = {
            "Heal": lambda: self.player_heal(False),
            "Healmore": lambda: self.player_heal(True),
            "Hurt": lambda: self.player_hurt(False),
            "Hurtmore": lambda: self.player_hurt(True),
            "Sleep": self.player_casts_sleep,
            "Stopspell": self.player_casts_stopspell
        }
        spell_cost = {
            "Heal": 4,
            "Healmore": 10,
            "Hurt": 2,
            "Hurtmore": 5,
            "Sleep": 2,
            "Stopspell": 2
        }

        can_cast = self.model["player"]["mp"] > spell_cost.get(spell)
        if not can_cast:
            self.output.output = f'''Player tries to cast {spell}, but doesn't have enough MP!\n'''
        else:
            self.model["player"]["mp"] -= spell_cost.get(spell)
            if self.model["player"]["p_stop"]:
                self.output.output = f'''Player casts {spell}, but their magic has been sealed!\n'''
            else:
                spell_switch.get(spell)()
        self.view.update_ptext(self.model["player"])
        self.is_enemy_defeated()

    def player_heal(self, more):
        player_heal_range = [10, 17]
        player_healmore_range = [85, 100]
        spell_name = "Healmore" if more else "Heal"
        heal_total = 0

        if more:
            heal_total = self.calc_heal(player_healmore_range)
        else:
            heal_total = self.calc_heal(player_heal_range)

        if heal_total == 0:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts {spell_name}, but their hit points were already at maximum!\n'''
            )
        else:
            self.model["player"]["hp"] += heal_total
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts {spell_name}! Player is healed {str(heal_total)} hit points!\n'''
            )


    def calc_heal(self, heal_range):
        heal_max = self.model["player"]["maxhp"] - self.model["player"]["hp"]
        heal_amount = random.randint(heal_range[0], heal_range[1])
        return heal_max if heal_max < heal_amount else heal_amount

    def player_hurt(self, more):
        ''' Handles player casting of Hurt and Hurtmore'''
        player_hurt_range = [5, 12]
        player_hurtmore_range = [58, 65]
        enemy_hurt_resistance = self.model["enemy"]["hurtR"]
        spell_name = "Hurtmore" if more else "Hurt"
        hurt_dmg = random.randint(player_hurtmore_range[0], player_hurtmore_range[1]) if more else random.randint(player_hurt_range[0], player_hurt_range[1])

        if (random.randint(1, 16) <= enemy_hurt_resistance):
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts {spell_name}, but the enemy resisted!\n'''
            )
        else:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts {spell_name}! {self.model["enemy"]["name"]} is hurt by {str(hurt_dmg)} hit points!\n'''
            )
            self.model["enemy"]["hp"] -= hurt_dmg

    def player_casts_sleep(self):
        ''' Player tries to cast Sleep on the enemy'''
        enemy_sleep_resistance = self.model["enemy"]["sleepR"]
        if self.model["enemy"]["e_sleep"] > 0:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Sleep! But the {self.model["enemy"]["name"]} is already asleep!\n'''
            )
        elif (random.randint(1, 16) <= enemy_sleep_resistance):
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Sleep! But the {self.model["enemy"]["name"]} resisted!\n'''
            )
        else:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Sleep! The {self.model["enemy"]["name"]} is now asleep!\n'''
            )
            self.model["enemy"]["e_sleep"] = 2
        return

    def player_casts_stopspell(self):
        ''' Player tries to cast Stopspell on the enemy'''
        enemy_stop_resistance = self.model["enemy"]["stopR"]
        if self.model["enemy"]["e_stop"]:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Stopspell! But the {self.model["enemy"]["name"]}'s magic was already blocked!\n'''
            )
        elif (random.randint(1, 16) <= enemy_stop_resistance):
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Stopspell! But the {self.model["enemy"]["name"]} resisted!\n'''
            )
        else:
            self.view.main_frame.txt.insert(
                tk.END,
                f'''Player casts Stopsell! The {self.model["enemy"]["name"]}'s magic is now blocked!!\n'''
            )
            self.model["enemy"]["e_stop"] = True

class PlayerBattle():
    '''Player Battle Class'''
    def __init__(self, p_model, output):
        self.model = p_model
        self.agi = p_model["agility"]
        self.asleep = p_model["p_sleep"]
        self.output = output

    def is_asleep(self):
        if self.asleep:
            self.model["sleep_count"] -= 1
            if random.randint(1,2) == 2 or self.model["sleep_count"] <= 0:
                self.asleep = False
                self.model["sleep_count"] = 6
            if self.asleep is False:
                self.output.output = "You wake up!\n"
                return False
            else:
                self.output.output = "You're still asleep...\n"
                return True
        return False


class EnemyBattle():
    '''Enemy Battle Class'''
    def __init__(self, e_model):
        self.model = e_model
        self.name = e_model["name"]
        self.agi = e_model["agility"]


