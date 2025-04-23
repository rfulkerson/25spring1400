characters = {'Cleric' : {'Armor' : 18, 'Health' : 30,
                'Spells': ['Cure','Guiding Bolt','Sanctuary']},
              'Wizard': {'Armor': 12, 'Health' : 22, 
                'Spells' : ['Magic Missile', 'Sleep', 'Shield']},
              'Fighter': { 'Armor': 18, 'Health': 35,
                           'Spells': [] },
              'Ranger' : { 'Armor': 25, 'Health': 15, 'Spells' : [] },
              
}

for char in characters:
    print(characters[char]['Health'])
#     
# for char in characters:
#     print(char['Health'])
#     
# allhealths = [characters['Health']]
# print(allhealths)
# 
# allhealths = [characters[char]['Health'] for char in characters]
