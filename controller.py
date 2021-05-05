'''
controller.py - Core controller for the simulation
'''
import tkinter as tk
import pprint
import view as View
import items
import levels
import enemy_dict
import enemy
import battle as Battle

class Controller():
    ''' Main controller class'''
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.update_ptext(self.model["player"])
        self.output = model["output"]
        self.output.attach(self)
        self.output.output = "DQ1 Battle Sim"

        self.battle = Battle.Battle(self.model, self.view)
        self.view.frames[View.SetupFrame].buy_herb_button.bind("<Button-1>", self.herb_inc)
        self.view.frames[View.SetupFrame].start_fight_button.bind("<Button-1>", self.start_battle)
        self.view.name_text.trace('w', self.update_name)
        self.view.level_change.trace('w', self.update_level)
        self.view.chosen_weapon.trace('w', self.update_weapon)
        self.view.chosen_armor.trace('w', self.update_armor)
        self.view.chosen_shield.trace('w', self.update_shield)
        self.view.chosen_enemy.trace('w', self.update_einfo)
        self.battle.fight_over.trace('w', self.end_battle)
        self.view.frames[View.BattleFrame].show_model_btn.bind("<Button-1>", self.update_text)
        #self.model["output"].attach(self)
        #self.model["output"].output = "DQ1 Battle Sim"

    def update_frame(self, *args):
        ''' Tells view.ctrl_frame to change the frame'''
        self.view.ctrl_frame.show_frame(args[0])

    def start_battle(self, *_):
        ''' Performs the handoff to battle.py for battle control'''
        if self.model["enemy"] is None:
            pass
        else:
            self.battle.setup_battle()

    def end_battle(self, *_):
        '''Cleans up after the battle is done and resets the simulator'''
        self.model["enemy"] = None
        self.model["player"]["hp"] = self.model["player"]["maxhp"]
        self.model["player"]["mp"] = self.model["player"]["maxmp"]
        self.model["player"]["herb_count"] = 0
        self.view.main_frame.txt["state"] = "disabled"
        self.update_einfo()
        self.update_ptext()
        self.view.show_frame(View.SetupFrame)

    def update_text(self, text, *_):
        '''
        Updates the main text box with output. When text is None, outputs the model and other
        debugging information
        '''
        #pp = pprint.PrettyPrinter()
        #p_model = pp.pformat(self.model)

        self.view.clear_output()
        self.view.main_frame.txt["state"] = 'normal'

        for line in text.output:
            self.view.main_frame.txt.insert(tk.END, line + "\n")
        #else:
        #    self.view.main_frame.txt.insert(1.0, p_model + "\n\n" + str(self.view.chosen_magic.get()))

        self.view.main_frame.txt["state"] = "disabled"

    def update_name(self, *_):
        ''' Updates the player name and triggers stat recalculations '''
        self.model["player"]["name"] = self.view.name_text.get()
        self.model["player"] = levels.level_up(self.model["player"])
        self.update_ptext()

    def update_ptext(self, *_):
        '''Tells the view to update the player label'''
        self.view.update_ptext(self.model["player"])

    def update_einfo(self, *_):
        '''Tells the view to update the enemy label'''
        chosen_enemy = self.view.chosen_enemy.get()
        for _, v in enemy_dict.enemy_dict.items():
            if chosen_enemy == v["name"]:
                self.model["enemy"] = enemy.prep_enemy(v)
                self.view.update_einfo(self.model["enemy"])
                break

    def update_level(self, *_):
        '''Updates stats when level spinbox changes'''
        self.model["player"]["level"] = self.view.level_change.get()
        self.model["player"] = levels.level_up(self.model["player"])
        self.update_ptext()

    def update_weapon(self, *_):
        '''Updates weapon when new weapon is selected'''
        chosen_weapon = self.view.chosen_weapon.get()
        for name, mod in items.weapons:
            if chosen_weapon == name:
                self.model["player"]["weapon"] = (name, mod)
                break
        self.update_ptext()

    def update_armor(self, *_):
        '''Updates armor when new armor is selected'''
        chosen_armor = self.view.chosen_armor.get()
        for name, mod, mag_def, fire_def in items.armors:
            if chosen_armor == name:
                self.model["player"]["armor"] = (name, mod)
                self.model["player"]["mag_def"] = mag_def
                self.model["player"]["fire_def"] = fire_def
                break
        self.update_ptext()

    def update_shield(self, *_):
        '''Updates shield when new shield is selected'''
        chosen_shield = self.view.chosen_shield.get()
        for name, mod in items.shields:
            if chosen_shield == name:
                self.model["player"]["shield"] = (name, mod)
                break
        self.update_ptext()

    def herb_inc(self, *_):
        '''Handles incrementing the herb count'''
        if self.model["player"]["herb_count"] >= 6:
            self.output.output = '''You cannot buy any more herbs.\n'''
        else:
            self.model["player"]["herb_count"] += 1
            self.update_ptext(self.model["player"])
