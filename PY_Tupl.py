#Tuples
manhwalist=("ORV","WB","Lookism")
print(manhwalist[1])
#del manhwalist[1]
#TypeError: 'tuple' object doesn't support item deletion
print(manhwalist[1] * 2)
mangalist=("Haikyu","One Piece","Berserk")
print(manhwalist + mangalist )
#mangalist.append="Demon Slayer"
#AttributeError: 'tuple' object has no attribute 'append'
fulllist=manhwalist + mangalist
#print(fulllist + "HB")
#TypeError: can only concatenate tuple (not "str") to tuple
print(fulllist)
