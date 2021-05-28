import random as r
from time import sleep


class battle:
    def __init__(self):
        # Enemies
        # Basic enemies (Name, Health, Attack, Strength(Attack Multiplier))
        self.unarmed_spirit = ['Unarmed Spirit', 2, 0, 0]
        self.goblin = ['Goblin', 5, 1, 1]
        self.goblin_w_armor = ['Goblin with armor', 8, 1, 1]

        # Ranged enemies (Health, Attack, Ammunition)
        self.goblin_bow = ['Goblin with a bow', 3, 2, 8]
        self.gang_member_w_gun = ['Gang member with a gun', 9, 4, 12]

        # Game mechanics
        # Enemy on field
        self.enemy1 = 0

        # Turns
        self.choseturn = 0

        # Player tactics
        self.fightmenu = ['- [attack]', '- [blitz]','- [skip] turn','- check [health]']

        # Player weapons (Name, Attack, Durability (or Ammunition))
        self.stick = ['Stick', 1, 5]
        self.knife = ['Knife', 3, 20]
        self.bow = ['Bow', 2, 8]
        self.pistol = ['Pistol', 4, 12]

        # Player information
        self.blitz = 0
        self.health = 50
        self.armor = 1
        self.inv = [['Fists', 1]]
        self.currentweapon = ['Fists',1]

    def spawn(self):
        a = r.randint(0, 5)
        if a == 0:  # Spawns basic enemies
            b = r.randint(0, 3)
            if b == 0: self.enemy1 = self.unarmed_spirit
            elif b == 1: self.enemy1 = self.goblin
            elif b == 2: self.enemy1 = self.goblin_w_armor
            else: self.spawn()
            self.appearance()
        elif a == 1:  # Spawn ranged enemies
            b = r.randint(0, 2)
            if b == 0: self.enemy1 = self.goblin_bow
            elif b == 1: self.enemy1 = self.gang_member_w_gun
            else: self.spawn()
            self.appearance()
        else:
            print("Nothing has spawned... Yet...")
            sleep(1)
            self.spawn()

    def appearance(self):
        print("\n! - A", self.enemy1[0],"has appeared! Get ready to fight!")
        sleep(2)
        self.firstturn()

    def firstturn(self):
        print("\nLet's see who goes first", end="")
        sleep(1)
        for i in range(4):
            print('.', end="")
        a = r.randint(1, 3)
        if a == 1:
            print("\nIt looks like you have initiative to go first.")
            self.choseturn = 0
        elif a == 2:
            print('\n', self.enemy1[0], "goes first.")
            self.choseturn = 1
        sleep(2)
        self.turn()

    def deathcheck(self):
        if self.health <= 0:
            self.blitz = 0
            self.death()
            sleep(2)
        elif self.enemy1[1] <= 0:
            self.enemy1 = 0
            print('Enemy has been defeated! Congrats!')
            sleep(2)
            self.enemy1 = 0
            self.blitz = 0
            self.spawn()
        else:
            self.turn()

    def turn(self):
        if self.choseturn == 0:
            print("\n","-"*6,"\n>>>Your turn\n","-"*6,"\n")
            self.playerturn()
        elif self.choseturn == 1:
            print("\n","-"*6,"\n>>>Enemy's turn\n","-"*6,"\n")
            try:
                self.enemyturn()
            except:
                print("Well shoot he's ded. Time to look for someone else...")
                self.spawn()

    def playerturn(self):
        if self.blitz != 0:
            print("Blitz is activated. Rounds until blitz is done: ",self.blitz+1,)
            try:
                dmg = self.currentweapon[1]
                self.enemy1[1] -= dmg
                print("The", self.enemy1[0], "was hit for", dmg, "damage!",
                    "\nRemaining enemy health:", self.enemy1[1])
                try:
                    self.currentweapon[2] -= 1
                except IndexError:
                    pass
                self.choseturn = 1
                self.blitz-=1
                self.deathcheck()
            except IndexError:
                self.deathcheck()

        for i in self.fightmenu:
            print(i)
        inp = input(">")


        # Listed actions

        if (inp == 'attack') or (inp == 'a'):
            try:
                dmg = self.currentweapon[1]
                self.enemy1[1] -= dmg
                print("The", self.enemy1[0], "was hit for", dmg, "damage!",
                        "\nRemaining enemy health:", self.enemy1[1])
                try:
                    self.currentweapon[2] -= 1
                except:
                    pass
                self.choseturn = 1
                self.deathcheck()
            except IndexError:
                print("?\n\nWhere's my weapon damage???")
                sleep(2)
                self.deathcheck()

        elif (inp == 'skip') or (inp == 's'):
            print("\nYou skipped your turn...")
            self.choseturn = 1
            sleep(1)
            self.deathcheck()

        elif (inp == 'blitz') or (inp == 'b'):
            print("\nHow much rounds do you want to blitz?")
            try:
                self.blitz = int(input("Rounds: "))
                self.blitz-=1
                print("Okay, blitzing...")
                self.playerturn()
            except ValueError:
                print("\n\n(Please give a valid number. Returning back to the menu)\n")
                sleep(3)
                self.playerturn()

        elif (inp == 'health') or (inp == 'h'):
            print("\nYour current health:",self.health,"\n\nEnemy's health:\n",self.enemy1[0],":",self.enemy1[1],"\n\n\n--Menu--")
            self.playerturn()
            
        # Unlisted actions

        elif (inp == 'kill') or (inp == 'k'):
            print("The rays from the gods come striking down.")
            sleep(2)
            print("The enemy screams and burns from the rays.")
            sleep(2)
            self.enemy1[1]-=self.enemy1[1]
            self.deathcheck()
        
        elif (inp == 'die') or (inp == 'd'):
            print("You just plop out a blanket and pillow.")
            sleep(2)
            print("Alright. This looks like a safe place to sleep... Goodnight!")
            sleep(1)
            print("zzz...")
            self.health-=self.health
            self.deathcheck()

        else:
            print("\nSay that again?")
            self.playerturn

    def enemyturn(self):
        dmg = self.enemy1[2] * self.enemy1[3]
        self.health -= dmg
        print("The", self.enemy1[0], "has attack you for", dmg,
              "\nYour health:", self.health)
        self.choseturn = 0
        sleep(1)
        self.deathcheck()

    def death(self):
        print("\n\n\n\n\nToday is a sad day...")
        sleep(3)
        print("I mean, they just let themselves... Die")
        sleep(3)
        print("The killer", self.enemy1[0], "is here to speak... Go ahead...")
        sleep(3)
        print(self.enemy1[0], "- uh yeah...")
        sleep(1)
        print(
            self.enemy1[0],
            "- The program made me commit the players murder... It wasn't me I swear."
        )
        sleep(3)
        print("The audience gasps, and then talking.")
        sleep(2)
        print(
            "Okay, okay enough talking... We need more answers to this murder..."
        )
        sleep(3)
        print("But, who would it be?")
        sleep(5)
        print("\n\n\nRetry? [y or n]")
        a = input(">")
        if (a == "y") or (a == "yes"):
            print("\nAlright. Here we go.")
            self.health = 50
            self.enemy1 = 0
            self.spawn()
        elif (a == "n") or (a == "no"):
            print("Okay, I'll just let you enjoy your death...")
