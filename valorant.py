print("Welcome to Valorant Game")
dict = {
    'Breach': 'Initiator',
    'Brim': 'Controller',
    'Cypher': 'Sentinel',
    'Jett': 'Duelist',
    'Omen': 'Controller',
    'Phoenix': 'Duelist',
    'Raze': 'Duelist',
    'Reyna': 'Duelist',
    'Sage': 'Sentinel',
    'Sova': 'Initiator',
    'Skye' : 'Initiator',
    'Killjoy': 'Sentinel'
}
duelist = 0
controller = 0
initiator = 0
sentinel = 0

print("\nHeroes are :")
selected_heroes = []
roles= []

for hero, role in dict.items():
    print(hero,' >> role : ',role)

print("\nSelect 7 Hero : ")
for i in range(7):
    chose = input()
    selected_heroes.append(chose)

print(selected_heroes)
for hero in selected_heroes:
    for key, value in dict.items():
        if hero == key:
            roles.append(value)

for i in roles:
    if "Duelist" == i:
        duelist = duelist + 1
    if "Controller" == i:
        controller = controller + 1
    if "Initiator" == i:
        initiator = initiator + 1
    if "Sentinel" == i:
        sentinel = sentinel + 1

if duelist >= 2 and controller >= 1 and initiator >= 1 and sentinel >= 1:
    print("\nWe have a perfect team. Let's Win this game")
else:
    print("\nWe don't have perfect team. It will be hard to win this match.") 

    