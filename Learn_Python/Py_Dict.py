#Dictionaries
Sup_Her = {'Thor': "Hammer", 'Ironman': 'Suit', 'Cap Amer': 'Shield' }
print(Sup_Her)
print(Sup_Her['Ironman'])
Sup_Her['Hulk']='Muscle'
Sup_Her['Black_w']='Martial_A'
print(Sup_Her)
print(Sup_Her['Black_w'])
del Sup_Her['Thor']
print(Sup_Her)
Sup_Her = {'Thor': "Hammer", 'Thor': "Hammer2",'Thor': "Hammer3" }
print(Sup_Her['Thor'])
'''
{'Thor': 'Hammer', 'Ironman': 'Suit', 'Cap Amer': 'Shield'}
Suit
{'Thor': 'Hammer', 'Ironman': 'Suit', 'Cap Amer': 'Shield', 'Hulk': 'Muscle', 'Black_w': 'Martial_A'}
Martial_A
{'Ironman': 'Suit', 'Cap Amer': 'Shield', 'Hulk': 'Muscle', 'Black_w': 'Martial_A'}
Hammer3
'''
