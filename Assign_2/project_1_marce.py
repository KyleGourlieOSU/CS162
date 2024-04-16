class Character:
    def __init__(
            self,
            new_playername = "none given",
            new_level = 5,
            new_vigor = 10,
            new_mind = 11,
            new_endurance = 10,
            new_strength = 9,
            new_dexterity = 13,
            new_intelligence = 9,
            new_faith = 8,
            new_arcane = 14,
            new_weapon_right = "Great Knife",
            new_weapon_left = "empty",
            new_helm = "none",
            new_chest_armor = "none"
            ):
        self.playername = new_playername
        self.level = new_level
        self.vigor = new_vigor
        self.mind = new_mind
        self.endurance = new_endurance
        self.strength = new_strength
        self.dexterity = new_dexterity
        self.intelligence = new_intelligence
        self.faith = new_faith
        self.arcane = new_arcane
        self.weapon_right = new_weapon_right
        self.weapon_left = new_weapon_left
        self.helm = new_helm
        self.chest_armor = new_chest_armor
    
    def __str__(self):
        result = f"playername: {self.playername}\n" \
        f"level: {self.level}\n" \
        f"stats-\nvigor: {self.vigor}\n" \
        f"mind: {self.mind}\n" \
        f"endurance: {self.endurance}\n" \
        f"strength: {self.strength}\n" \
        f"dexterity: {self.dexterity}\n" \
        f"intelligence: {self.intelligence}\n" \
        f"faith: {self.faith}\n" \
        f"arcane: {self.arcane}\n" \
        f"\nequipment-\nrighthand: {self.weapon_right}\n" \
        f"lefthand: {self.weapon_left}\n" \
        f"helm: {self.helm}\n" \
        f"chest_armor: {self.chest_armor}"
        return result

letmesoloher = Character(new_playername="Let Me Solo Her", new_level=179, new_weapon_right="uchigatana", new_weapon_left="Rivers of Blood", new_helm="Jar",new_vigor=40, new_mind=24, new_endurance=40, new_strength=38, new_dexterity=48, new_intelligence=28, new_faith=22, new_arcane=20 )
default = Character()
#user_input = Character(new_playername=input('enter your:\nPlayername: '), new_level=input('level: '), new_vigor=input('vigor: '), new_mind=input('mind: '), new_endurance=input('endurance: '), new_strength=input('strength: '), new_dexterity=input('dexterity: '), new_intelligence=input('intelligence: '), new_faith=input('faith: '), new_arcane=input('arcane: '))


print("##### prog. start #####")
while exit != 1:
    print("\n enter one of the listed numbers to use that function\n -1 - load your own stats\n 0 - enter your own stats\n 1 - view default stats\n 2 - view preset\n 3 - print your character stats\ntype exit to close program")
    menu_input = input('enter your choice: ')
    if menu_input == '0':
        user_input = Character(
        new_playername=(input('enter your-\nPlayername: ') or 'none given'),
        new_level=input('level: '), 
        new_vigor=input('vigor: '), 
        new_mind=input('mind: '), 
        new_endurance=input('endurance: '), 
        new_strength=input('strength: '), 
        new_dexterity=input('dexterity: '), 
        new_intelligence=input('intelligence: '), 
        new_faith=input('faith: '),
        new_arcane=input('arcane: '))
    elif menu_input == '1':
        print(default)
    elif menu_input == '2':
        print(letmesoloher)
    elif menu_input == '3':
        try:
            print(user_input)
        except:
            print('you must enter character stats first')

    elif menu_input == '-1':
        print('\nLOADING DATA...')
        
        with open('stats.txt', 'r') as file:
            chars=[]
            stats={}
            for line in file:
                if line == '-----\n':
                    char = Character(
    new_playername=stats['playername'],
    new_level=stats['level'],
    new_vigor=stats['vigor'],
    new_mind=stats['mind'],
    new_endurance=stats['endurance'],
    new_strength=stats['strength'],
    new_dexterity=stats['dexterity'],
    new_intelligence=stats['intelligence'],
    new_faith=stats['faith'],
    new_arcane=stats['arcane']
)

                    chars.append(char)
                    stats={}

                else:
                    line_1=line.strip('\n')
                    line_2=line_1.strip(' ')
                    lines=line_2.split(':')
                    stats[lines[0]] = lines[1]
