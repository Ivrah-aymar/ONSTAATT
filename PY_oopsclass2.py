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
####3
#class 
#input in main -- Student score
class Student:
    def __init__(self,Name,m1,m2,m3,m4):
        self.Name=Name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
    def Name(self):
        return Name
    def m1(self):
        return m1
    def m2(self):
        return m2
    def m3(self):
        return m3
    def m4(self):
        return m4
    def total(m1,m2,m3,m4):
        total1=m1+m2+m3+m4
        return total1
        

#main
print("Its the start")
Student1=Student("Vivi",90,60,80,79)
print(Student1.Name)
print(Student1.m1)
print(Student1.m2)
print(Student1.m3)
print(Student1.m4)
x1=Student1.m1
x2=Student1.m2
x3=Student1.m3
x4=Student1.m4
print(Student.total(x11,x2,x3,x4))
'''
Its the start
Vivi
90
60
80
79
309
'''
#3 -- reduce and table for one student
#class 
#input in main -- Student score
class Student:
    def __init__(self,Name,m1,m2,m3,m4):
        self.Name=Name
        self.marks=[m1,m2,m3,m4]
    def Name(self):
        return Name
    def marks(self):
        return marks
    def total(marks):
        total1=sum(marks)
        return total1
    def result(tot):
        if tot > 35:
            return 1
        else:
            return 0
            
        
#main
print("Its the start")
Student1=Student("Vivi",90,60,80,79)
print(Student1.Name)
print(Student1.marks)
x1=Student1.marks
x2=Student.total(x1)
print(Student.result(x2))
print(f"{Student1.Name}",x2,'Pass' if Student.result(x2) == 1 else 'Fail')
'''
Its the start
Vivi
[90, 60, 80, 79]
1
Vivi 309 Pass
'''
#The error "TypeError: 'Student' object is not iterable" arises in Python when you attempt to iterate over an instance of the Student class directly, but the class definition doesn't support iteration. Iteration, often done using a for loop, requires an object to be iterable, meaning it can return its elements one at a time. Standard objects, by default, are not iterable.
#To resolve this, you can implement the __iter__ method within the Student class. This method should return an iterator object. 4
#class 
#input in main -- Student score
class Student:
    def __init__(self,Name,m1,m2,m3,m4):
        self.Name=Name
        self.marks=[m1,m2,m3,m4]
    def Name(self):
        return Name
    def marks(self):
        return marks
    def total(marks):
        total1=sum(marks) * 100/400
        return float(total1)
    def result(tot):
        if tot > 35:
            return 1
        else:
            return 0
#main
print("Its the start")
#Student1=Student("Vivi",90,60,80,79)
#Student1=["Vivi",90,60,80,79]
Students=[Student("Sabo",90,60,80,79),Student("Luffy",2,10,10,3),Student("Zoro",10,2,1,21)]
#del len
length=len(Students)
print(length)
#print(Students[0].Name)
#for i in range(0,length):
for Student in Students:
    print(Student.Name)
    #print (Students[i].Name)
    tt1=Student.marks
    print(tt1)
    #----->  tt2=Students[i].(Student.total())
    #------>print(tt2)
   # tt1=Students[i].marks
    #print(tt1)
    #tt2 = Students[i].total()
    #print(tt2)
    #print ({'Pass' if Students[i].result(Students[i].total(Students[i].marks)) == 1 else 'Fail'})
#    x2=Student.total(x1)
#    print(Student.result(x2))
#    print(f"{Student1.Name}")
#,x2,'Pass' if Student.result(x2) == 1 else 'Fail')
    




