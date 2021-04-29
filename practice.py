import random as r
from time import sleep


class battle:
    def __init__(self):
        # Enemies
        # Basic enemies (Name, Health, Attack, Strength(Attack Multiplier))
        self.unarmed_spirit = ['Unarmed Spirit',2,0,0]
        self.goblin = ['Goblin',5,1,1]
        self.goblin_w_armor = ['Goblin with armor',8,1,1]

        # Ranged enemies (Health, Attack, Ammunition)
        self.goblin_bow = ['Goblin with a bow',3,2,8]
        self.gang_member_w_gun = ['Gang member with a gun',9,4,12]

        # Game mechanics
        # Enemy on field
        self.enemy1 = 0

        # Turns
        self.choseturn = 0

        # Player tactics
        self.fightmenu = ['- [attack]','- [skip] turn']

        # Player weapons (Name, Attack, Durability (or Ammunition))
        self.stick = ['Stick',1,5]
        self.knife = ['Knife',3,20]
        self.bow = ['Bow',2,8]
        self.pistol = ['Pistol',4,12]

        # Player information
        self.health = 50
        self.armor = 1
        self.inv = [['Fists',1]]
        self.currentweapon = ['Fists',1]
        self.deathh = 0

    def spawn(self):
        a = r.randint(0,5)
        if a == 0:      # Spawns basic enemies
            b = r.randint(0,3)
            if b == 0:
                self.enemy1 = self.unarmed_spirit
            elif b == 1:
                self.enemy1 = self.goblin
            elif b == 2:
                self.enemy1 = self.goblin_w_armor
        elif a == 1:    # Spawn ranged enemies
            b = r.randint(0,2)
            if b == 0:
                self.enemy1 = self.goblin_bow
            elif b == 1:
                self.enemy1 = self.gang_member_w_gun
        else:
            print("Nothing has spawned... Yet...")
            sleep(1)
            self.spawn()

        if self.enemy1 != 0:
            print("\n! - A", self.enemy1[0], "has appeared! Get ready to fight!")
            sleep(2)
            self.firstturn()

    def firstturn(self):
        print("\nLet's see who goes first",end="")
        sleep(1)
        for i in range(4):
            print('.',end="")
        a = r.randint(1,3)
        if a == 1:
            print("\nIt looks like you have initiative to go first.")
            self.choseturn = 0
        elif a == 2:
            print('\n',self.enemy1[0],"goes first.")
            self.choseturn = 1
        sleep(2)
        self.turn()

    def turn(self):
        if self.health <= 0:
            print('rip... Game over...')
            self.deathh = 1
            self.death()
            sleep(2)
            
        elif self.enemy1[1] <= 0:
            self.enemy1 = 0
            print('Enemy has been defeated! Congrats!')
            sleep(2)

        if self.choseturn == 0:
            print("\n------\n>>>Your turn\n------\n")
            if self.deathh == 0:
              self.playerturn()
            else:
              print("rip")
        elif self.choseturn == 1:
            print("\n------\n>>>Enemy's turn\n------\n")
            try:
              self.enemyturn()
            except:
              print("Well shoot he's ded. Time to look for someone else...")
              self.spawn()

    def playerturn(self):
        for i in self.fightmenu:
            print(i)
        inp = input(">")
        if inp == 'attack':
            dmg = self.currentweapon[1]
            self.enemy1[1]-=dmg
            print("The",self.enemy1[0],"was hit for",dmg,"damage!","\nRemaining enemy health:", self.enemy1[1])
            try:
                self.currentweapon[2]-=1
            except:
                pass
            self.choseturn = 1
            self.turn()

        elif inp == 'skip':
            print("\nYou skipped your turn...")
            self.choseturn = 1
            sleep(1)
            self.turn()
        else:
            print("Please use words instead of numbers...")
            self.playerturn()

    def enemyturn(self):
        dmg = self.enemy1[2] * self.enemy1[3]
        self.health -= dmg
        print("The",self.enemy1[0],"has attack you for",dmg,"\nYour health:",self.health)
        self.choseturn = 0
        sleep(1)
        self.turn()
    
    def death(self):
      print("\nToday is a sad day...")
      sleep(3)
      print("I mean, they just let themselves... Die")
      sleep(3)
      print("The killer",self.enemy1[0],"is here to speak... Go ahead...")
      sleep(3)
      print(self.enemy1[0],"- uh yeah...")
      sleep(1)
      print(self.enemy1[0],"- The program made me commit the players murder... It wasn't me I swear.")
      sleep(3)
      print("The audience gasps, and then talking.")
      sleep(2)
      print("Okay, okay enough talking... We need more answers to this murder...")
      sleep(3)
      print("But, who would it be?")

fight = battle()
fight.spawn()