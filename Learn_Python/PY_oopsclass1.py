#OOPs
#class
class hobby:
    def __init__(self,manga,anime):
        self.manga=manga
        self.anime=anime
    def getmanga(self):
        return self.manga
    def getanime(self):
        return self.anime
    
h=hobby("ORV","AOT")
print(h.getanime())
'''
AOT
'''
