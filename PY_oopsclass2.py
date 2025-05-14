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
#2
class Person:
    def __init__(self,place,grade):
        self.place=place
        self.grade=grade
    def getplace(self):
        return self.grade
    def getgrade(self):
        return self.grade

print("Its a Start")
pl=Person("bkl",93)
p2=Person("kpr",94)
p3=Person("mgl",60)
print(pl.grade)
print(p2.grade)

#3
class Stu_grade:
    def __init__(self,Name,marks1,marks2,marks3,marks4):
        self.Name=Name
        self.marks=[marks1,marks2,marks3,marks4]
    def Name(self):
        return Name
    def markstotal(self):
        return sum(self.marks)
    def percentage(self):
        return self.markstotal * 100/400
    def has_passed(self):
       return self.percentage() > 35
       
print("Its the beginning")
#students=[
s1=Stu_grade("Vivi",99,98,94,94),
#Stu_grade("Luffy",50,30,35,20),
#Stu_grade("Light",99,97,96,98)
#]
if s1.has_passed
#for student in students:
#    print(f"{student.Name}: {Stu_grade.percentage():.2f}% - {'Pass' if Stu_grade.has_passed() else 'Fail'}")
