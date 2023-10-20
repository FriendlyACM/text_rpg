# take input for character name
# intialize character stats and attacks
maincharStats = {
    'type' : 'neutral',
    'health' : 300,
    'atk' : 10,
    'def' : 10,
}
larryStats = {
    'type' : 'fire',
    'health' : 100,
    'atk' : 12,
    'def' : 8,
}
barryStats = {
    'type' : 'water',
    'health' : 100,
    'atk' : 12,
    'def' : 8,
}
jerryStats = {
    'type' : 'electric',
    'health' : 100,
    'atk' : 12,
    'def' : 8,
}

# intialize combat system
def typeCheck(attackType, prey):
    if prey == 'fire':
        if attackType == 'fire':
            return 'neutral'
        elif attackType == 'water':
            return 'strong'
        elif attackType == 'electric':
            return 'weak'
    elif prey == 'water':
        if attackType == 'water':
            return 'neutral'
        elif attackType == 'electric':
            return 'strong'
        elif attackType == 'electric':
            return 'weak'
    elif prey == 'electric':
        if attackType == 'electric':
            return 'neutral'
        elif attackType == 'fire':
            return 'strong'
        elif attackType == 'electric':
            return 'weak'
    elif prey == 'neutral':
        return 'neutral'
    else:
        return None 
def damageValue(power, attackerStats, preyStats):
    attackerAtk = attackerStats.get("atk")
    preyDef = preyStats.get("def")
    if power == 'neutral':
        return attackerAtk - preyDef
    elif power == 'strong':
        return (attackerAtk - preyDef)*2
    elif power == 'weak':
        return (attackerAtk - preyDef)*0.5
    else:
        return None
# start the adventure
# encounter 1
input("You stumble upon Larry. He is a fire goblin. He needs to be defeated. You're the one to do it.\n(Press Enter to Fight!)")
while maincharStats.get('health') > 0:
    spell = input("Which spell would you like to use?\n1. Fire\n2. Water\n3. Electric\n(Type the number to select a spell)\n")
    if spell == '1':
        spell = 'fire'
    elif spell == '2':
        spell = 'water'
    elif spell == '3':
        spell = 'electric'
    else:
        print("Not a valid spell")
        continue
    damage = int(damageValue(typeCheck(spell,larryStats.get('type')),maincharStats,larryStats))
    healthUpdate = larryStats.get('health') - damage
    larryStats.update({'health':healthUpdate})
    print(f"You did {damage} damage to Larry!")
    input(f"He is at {larryStats.get('health')} health\n(Press Enter to continue)")
    damage = int(damageValue(typeCheck('fire',maincharStats.get('type')),larryStats,maincharStats))
    healthUpdate = maincharStats.get('health') - damage
    maincharStats.update({'health':healthUpdate})
    print(f"Larry did {damage} to you!")
    input(f"You are at {maincharStats.get('health')} health\n(Press Enter to continue)")
    if larryStats.get('health') <= 0:
        print("You have defeated Jerry!")
        break
# encounter 2
input("Out of nowhere Larry's brother Barry appears. He is a water goblin. He also needs to be defeated. You're the one to do it.\n(Press Enter to Fight!)")
while maincharStats.get('health') > 0:
    spell = input("Which spell would you like to use?\n1. Fire\n2. Water\n3. Electric\n(Type the number to select a spell)\n")
    if spell == '1':
        spell = 'fire'
    elif spell == '2':
        spell = 'water'
    elif spell == '3':
        spell = 'electric'
    else:
        print("Not a valid spell")
        continue
    damage = int(damageValue(typeCheck(spell,barryStats.get('type')),maincharStats,barryStats))
    healthUpdate = barryStats.get('health') - damage
    barryStats.update({'health':healthUpdate})
    print(f"You did {damage} damage to Barry!")
    input(f"He is at {barryStats.get('health')} health\n(Press Enter to continue)")
    damage = int(damageValue(typeCheck('water',maincharStats.get('type')),barryStats,maincharStats))
    healthUpdate = maincharStats.get('health') - damage
    maincharStats.update({'health':healthUpdate})
    print(f"Barry did {damage} to you!")
    input(f"You are at {maincharStats.get('health')} health\n(Press Enter to continue)")
    if barryStats.get('health') <= 0:
        print("You have defeated Jerry!")
        break
# encounter 3
input("Another goblin brother appears. His name is Jerry He is a electric goblin. He also needs to be defeated. You're the one to do it.\n(Press Enter to Fight!)")
while maincharStats.get('health') > 0:
    spell = input("Which spell would you like to use?\n1. Fire\n2. Water\n3. Electric\n(Type the number to select a spell)\n")
    if spell == '1':
        spell = 'fire'
    elif spell == '2':
        spell = 'water'
    elif spell == '3':
        spell = 'electric'
    else:
        print("Not a valid spell")
        continue
    damage = int(damageValue(typeCheck(spell,jerryStats.get('type')),maincharStats,jerryStats))
    healthUpdate = jerryStats.get('health') - damage
    jerryStats.update({'health':healthUpdate})
    print(f"You did {damage} damage to Barry!")
    input(f"He is at {jerryStats.get('health')} health\n(Press Enter to continue)")
    damage = int(damageValue(typeCheck('electric',maincharStats.get('type')),jerryStats,maincharStats))
    healthUpdate = maincharStats.get('health') - damage
    maincharStats.update({'health':healthUpdate})
    print(f"Jerry did {damage} to you!")
    input(f"You are at {maincharStats.get('health')} health\n(Press Enter to continue)")
    if jerryStats.get('health') <= 0:
        print("You have defeated Jerry!")
        break