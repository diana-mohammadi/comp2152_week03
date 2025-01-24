import random
#Dice options created using list()and range()
diceOptions = list(range(1,7))
 
 #weapons list
weapons = ["first","knife","club","gun", "bomb", "Nuclear Bomb"]

print("Available Weapons: ", ", ".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1<=value <=6:
            return value
        else:
            print("invalid input! please enter a number between 1 and 6")

combatStrength= getCombatStrength("PLease enter a number between 1-6 for player: ")   
mCombatStrength= getCombatStrength("PLease enter a number between 1-6 for monster: ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll-1]
    monsterWeapon = weapons[monsterRoll-1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n Hero rolled {heroRoll}, monster rolled {monsterRoll}")
    print(f"\n Hero selected {heroWeapon}, monster selected {monsterWeapon}")
    print(f"\n Hero total strength: {heroTotal}, monster total strength: {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Hero wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins!")
    else:
        print("It's a Tie!")
