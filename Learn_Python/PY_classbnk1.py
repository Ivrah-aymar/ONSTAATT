#Class 
#Aim1: To get the total balance in the bank account at the end of the year
#input - total amount deposited and total amount withdrawed  at the end of month would be passed in the program
#Aim2: To include this too in above code --> To get the total balance in the bank account at the end of the month -- next code
class Bankaccount:
    def __init__(self,Name,month,tdeposit,twithdrawal):
        self.Name=Name
        self.month=month
        self.tdeposit=tdeposit
        self.twithdrawal=twithdrawal
   #     self.withdraw=withdraw
    #def Name(self):
     #   return Name
    def monthendbal(self):
        monbal=self.tdeposit-self.twithdrawal
     #   print("This is the end bal for the month",self.month," i.e ",monbal)
        return monbal
       

all_yr = [Bankaccount("Buggy","Jan",500,200),Bankaccount("Buggy","Feb",1000,200),Bankaccount("Buggy","Mar",300,700),Bankaccount("Buggy","Apr",500,400)]
yrendbal=0
for Bankaccount in all_yr:
    print("This is",Bankaccount.Name,"s' end bal for the month",Bankaccount.month," i.e ",Bankaccount.monthendbal())
    yrendbal=yrendbal+Bankaccount.monthendbal()
    
print("Total yrendbal=",yrendbal)
    
#for i in 
