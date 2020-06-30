from math import floor, pow

Cp_multiplier = {
    1 : 0.094,
    1.5 : 0.1351374318,
    2 : 0.16639787,
    2.5 : 0.192650919,
    3 : 0.21573247,
    3.5 : 0.2365726613,
    4 : 0.25572005,
    4.5 : 0.2735303812,
    5 : 0.29024988,
    5.5 : 0.3060573775,
    6 : 0.3210876,
    6.5 : 0.3354450362,
    7 : 0.34921268,
    7.5 : 0.3624577511,
    8 : 0.3752356,
    8.5 : 0.387592416,
    9 : 0.39956728,
    9.5 : 0.4111935514,
    10 : 0.4225,
    10.5 : 0.4329264091,
    11 : 0.44310755,
    11.5 : 0.4530599591,
    12 : 0.4627984,
    12.5 : 0.472336093,
    13 : 0.48168495,
    13.5 : 0.4908558003,
    14 : 0.49985844,
    14.5 : 0.508701765,
    15 : 0.51739395,
    15.5 : 0.5259425113,
    16 : 0.5343543,
    16.5 : 0.5426357375,
    17 : 0.5507927,
    17.5 : 0.5588305862,
    18 : 0.5667545,
    18.5 : 0.5745691333,
    19 : 0.5822789,
    19.5 : 0.5898879072,
    20 : 0.5974,
    20.5 : 0.6048236651,
    21 : 0.6121573,
    21.5 : 0.6194041216,
    22 : 0.6265671,
    22.5 : 0.6336491432,
    23 : 0.64065295,
    23.5 : 0.6475809666,
    24 : 0.65443563,
    24.5 : 0.6612192524,
    25 : 0.667934,
    25.5 : 0.6745818959,
    26 : 0.6811649,
    26.5 : 0.6876849038,
    27 : 0.69414365,
    27.5 : 0.70054287,
    28 : 0.7068842,
    28.5 : 0.7131691091,
    29 : 0.7193991,
    29.5 : 0.7255756136,
    30 : 0.7317,
    30.5 : 0.7347410093,
    31 : 0.7377695,
    31.5 : 0.7407855938,
    32 : 0.74378943,
    32.5 : 0.7467812109,
    33 : 0.74976104,
    33.5 : 0.7527290867,
    34 : 0.7556855,
    34.5 : 0.7586303683,
    35 : 0.76156384,
    35.5 : 0.7644860647,
    36 : 0.76739717,
    36.5 : 0.7702972656,
    37 : 0.7731865,
    37.5 : 0.7760649616,
    38 : 0.77893275,
    38.5 : 0.7817900548,
    39 : 0.784637,
    39.5: 0.7874736075,
    40 : 0.7903,
    41 : 0.79530001,
    42 : 0.8003,
    43 : 0.8053,
    44 : 0.81029999,   
    45 : 0.81529999,   
}
    
class baseStat():
    def __init__(self, attack, defense, stamina):
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        
    def __repr__(self):
        return super().__repr__()
    
    def setStats(self, attack, defense, stamina):
        self.attack = attack
        self.defense = defense
        self.stamina = stamina

def cp_calc(baseStat, attack_iv, defense_iv, hp_iv, power_up_value):
    return max(10, floor(
        (baseStat.attack + attack_iv) *
        (pow((baseStat.defense + defense_iv), 0.5)) *
        (pow((baseStat.stamina + hp_iv), 0.5)) *
        pow(Cp_multiplier[power_up_value], 2) / 10
    ))
    
def base_stat_calc(hp, attack, sp_attack, defense, sp_defense, speed):
    speed_mult = 1 + ((speed - 75) / 500)
    attack_go = ((1/4)*min(attack, sp_attack) + (7/4)*max(attack, sp_attack)) * speed_mult
    defense_go = ((3/4)*min(defense, sp_defense) + (5/4)*max(defense, sp_defense)) * speed_mult
    stamina_go = 50 + 1.75 * hp
    
    x = baseStat(attack_go, defense_go, stamina_go)
    if cp_calc(x, 15, 15, 15, 40) > 4000:
        x.setStats(attack_go * 0.91, defense_go * 0.91, stamina_go * 0.91)
    
    return x

def Menu():

    menu = {}
    menu['1'] = "Calculate CP."
    menu['2'] = "Populate Base Stats"
    menu['0'] = "Exit."
    
    while True:
        options=menu.keys()
        for entry in options:
            print(entry, menu[entry])
        option = int(input("Choose an option: "))
        if option == 1:
            attack_base = int(input("Base Attack -> "))
            defense_base = int(input("Base Defense -> "))
            hp_base = int(input("Base Hp -> "))
            attack_iv = int(input("Attack Iv -> "))
            defense_iv = int(input("Defense Iv -> "))
            hp_iv = int(input("Hp Iv -> "))
            power_up_value = float(input("Level -> "))

            base_stat = baseStat(attack_base, defense_base, hp_base)
            
            value = cp_calc(base_stat, defense_iv, hp_base, hp_iv, power_up_value)
            print(value)
        elif option == 2:
            pass
        elif option == 0:
            break
        else:
            print("Invalid option!")
    
if __name__ == "__main__":
    Menu()
    
    
# Some Regex to find files in csv file
# (\d+,(\w[^\d]+),\w+,(\w+[^,])?,\d+,\d+)
