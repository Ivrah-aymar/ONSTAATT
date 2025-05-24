#reverse a string
string="Warrior"
print("fullreverse:",string[::-1])
#check if the string is palindrome , print True if is and false if not.
class ChkPalindrome:
  def revandchk(str1):
    if str1 == str1[::-1]:
       return 1    
print("True") if ChkPalindrome.revandchk("TOM") == 1 else print("False")
print("True") if ChkPalindrome.revandchk("RACECAR") == 1 else print("False")
#check if the given integer is palindrome
class ChkPalindrome:
  def revandchk(num):
      reversed=0
      while num>0:
        reversed=reversed*10 + num%10
        num=num//10
      return reversed  
num=int(1356)
print("reversed number:",ChkPalindrome.revandchk(num))
print("True") if ChkPalindrome.revandchk(num) == num else print("False")
num=int(12621)  
print("True") if ChkPalindrome.revandchk(num) == num else print("False")
