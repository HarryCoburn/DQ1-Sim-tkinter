'''
    view.py - Holds the view for the MVC program
'''

import tkinter as tk
import tkinter.scrolledtext as scrolledtext

import inspect
from items import w_strings, a_strings, s_strings
from enemy_dict import e_strings


class View(tk.Tk):
    '''
    View class for the application
    '''
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # View Variables
        self.name_text = tk.StringVar()
        self.name_text.set("Rollo")
        self.level_change = tk.StringVar()
        self.chosen_weapon = tk.StringVar()
        self.chosen_weapon.set("Unarmed")
        self.chosen_armor = tk.StringVar()
        self.chosen_armor.set("Naked")
        self.chosen_shield = tk.StringVar()
        self.chosen_shield.set("Naked")
        self.chosen_enemy = tk.StringVar()
        self.chosen_enemy.set("Select Enemy")
        self.chosen_magic = tk.StringVar()
        self.chosen_magic.set("None")
        self.spell_strings = []
        self.curr_frame = None



        # Main window basics
        self.title("DQ1 Battle Simulator")
        self.geometry("1224x620+50+50")
        #self.resizable(False, False)

        # Now create the containers
        ctrl_container = tk.Frame(self, height=768, width=256, bg="blue")
        main_container = tk.Frame(self, height=768, width=768, bg="red")

        # Pack it
        ctrl_container.pack(side="left", fill="both", expand=True)
        main_container.pack(side="right", fill="both", expand=True)

        # Grid it
        ctrl_container.grid_rowconfigure(0, weight=1)
        ctrl_container.grid_columnconfigure(0, weight=1)
        ctrl_container.grid_propagate(0)

        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        # Frame dictionary
        self.frames={}
        for F in (SetupFrame, BattleFrame):
            frame = F(ctrl_container, self)
            self.frames[F] = frame


        self.show_frame(SetupFrame)
        self.main_frame = MainFrame(main_container, self)
        self.main_frame.grid(row=0, column=0)

    def show_frame(self, cont):
        '''
        Switches one frame for another. Assumes frames are overlapping.
        '''
        frame = self.frames[cont]
        if self.curr_frame is not None:
            self.curr_frame.grid_remove()
        self.curr_frame=frame
        frame.tkraise()
        frame.grid(row=0, column=0)

    def update_magic(self):
        '''
        Updates the magic menu in BattleFrame
        '''
        menu = self.frames[BattleFrame].magic["menu"]
        menu.delete(0, "end")
        for string in self.spell_strings:
            menu.add_command(label=string,
                             command=lambda value=string: self.chosen_magic.set(value))

    def update_ptext(self, pinfo):
        '''
        Updates the player label
        '''
        self.main_frame.player_label["text"] = inspect.cleandoc(f'''\
            Name: {pinfo["name"]}
            Level: {pinfo["level"]}
            HP: {pinfo["hp"]}/{pinfo["maxhp"]}
            MP: {pinfo["mp"]}

            Weapon: {pinfo["weapon"][0]}
            Armor: {pinfo["armor"][0]}
            Shield: {pinfo["shield"][0]}

            Strength: {pinfo["strength"]}
            Agility: {pinfo["agility"]}

            Herbs remaining: {pinfo["herb_count"]}

            Asleep?: {pinfo["p_sleep"]}
            Spells stopped?: {pinfo["p_stop"]}
        ''')
        self.spell_strings = pinfo["p_magic"]

    def update_einfo(self, einfo):
        '''
        Updates enemy label
        '''
        self.main_frame.enemy_label["text"] = inspect.cleandoc(f'''\
            Name: {einfo["name"]}
            HP: {einfo["hp"]}

            Strength: {einfo["strength"]}
            Agility: {einfo["agility"]}
        ''')

    def append_output(self, string):
        '''Appends output to the main output window'''
        self.main_frame.txt.insert(tk.END, string + "\n")

    def clear_output(self):
        '''Erases all output in the main output'''
        self.main_frame.txt["state"] = 'normal'
        self.main_frame.txt.delete(1.0, tk.END)

class SetupFrame(tk.Frame):
    '''
    Frame for fight setup buttons
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.configure(bg='red')

        self.buy_herb_button = tk.Button(self, text="Buy Herb")
        self.start_fight_button = tk.Button(self, text="FIGHT!")
        name_label = tk.Label(self, text="Name: ")
        name_entry = tk.Entry(self, textvariable=controller.name_text, width=7)
        level_spinbox = tk.Spinbox(
            self,
            from_=1,
            to=30,
            width=3,
            textvariable=controller.level_change,
            state="readonly"
            )
        level_label = tk.Label(self, text="Level: ")
        weapons = tk.OptionMenu(self, controller.chosen_weapon, *w_strings)
        armors = tk.OptionMenu(self, controller.chosen_armor, *a_strings)
        shields = tk.OptionMenu(self, controller.chosen_shield, *s_strings)
        enemies = tk.OptionMenu(self, controller.chosen_enemy, "Select Enemy", *e_strings)

        enemies.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
        self.start_fight_button.grid(column=0, row=1, pady=10, padx=10, columnspan=2)
        name_label.grid(column=0, row=2)
        name_entry.grid(column=1, row=2, pady=10, padx=10)
        level_label.grid(column=0, row=3, padx=10)
        level_spinbox.grid(column=1, row=3, pady=10, padx=10)

        weapons.grid(column=0, row=4, pady=10, padx=10, columnspan=2)
        armors.grid(column=0, row=5, pady=10, padx=10, columnspan=2)
        shields.grid(column=0, row=6, pady=10, padx=10, columnspan=2)
        self.buy_herb_button.grid(column=0, row=7, pady=10, padx=10, columnspan=2)

class BattleFrame(tk.Frame):
    '''
    Frame for running the fight
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.configure(bg='green')

        self.attack_btn = tk.Button(self, text="Attack")
        self.herb_btn = tk.Button(self, text="Use Herb")
        self.run_btn = tk.Button(self, text="Run")
        self.cast_btn = tk.Button(self, text="Cast")
        self.magic = tk.OptionMenu(
            self,
            controller.chosen_magic,
            controller.chosen_magic.get(),
            *controller.spell_strings
            )
        self.show_model_btn = tk.Button(self, text="Show Model")

        self.attack_btn.grid(column=0, row=0, pady=10, padx=10)
        self.herb_btn.grid(column=0, row=1, pady=10, padx=10)
        self.run_btn.grid(column=0, row=2, pady=10, padx=10)
        self.cast_btn.grid(column=0, row=3, pady=10, padx=10)
        self.magic.grid(column=1, row=3, pady=10, padx=10)
        self.show_model_btn.grid(column=0, row=4, pady=10, padx=10)

class MainFrame(tk.Frame):
    '''
    Main frame of the program. Holds output
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='purple')
        self.controller = controller

        # Player Label
        self.player_label = tk.Label(
            master=self,
            #width=256,
            #wraplength=200,
            #justify=tk.RIGHT,
            borderwidth=1,
            relief="solid",
            anchor=tk.NW,
            font=('consolas','12'),
            #height=30
            )
        self.player_label.grid(column=0, row=0, sticky="n", padx=10, ipadx=3)


        #Enemey label
        self.enemy_label = tk.Label(
            master=self,
            #width=256,
            #wraplength=200,
            #justify=tk.RIGHT,
            borderwidth=1,
            relief="solid",
            anchor=tk.NW,
            font=('consolas','12'),
            text="Enemy not selected.",
            #height=30
            )
        self.enemy_label.grid(column=1, row=0, sticky="n", padx=10, ipadx=3)

        #Output window
        self.txt = scrolledtext.ScrolledText(
            master=self,
            undo=True,
            font=('consolas','12'),
            width=40,
            #height=30,
            wrap=tk.WORD
            )
        self.txt.grid(column=2, row=0, padx=10, ipadx=3)
        self.txt.insert('1.0', ('Dragon Quest 1 Battle Simulator.'
            'Please select an enemy, then click fight.'))
        self.txt.configure(state="disabled")
