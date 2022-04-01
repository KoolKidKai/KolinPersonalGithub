#Written in Imperative here
print(" ")
print("\nStart of Imperative Programming of GCD Function")
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

ans = findgcd(20, 60)
print("\nThe greatest common denominator of 20 and 60 is ",ans)



#Writing in OOP here
print("\nStart of OOP Programming of math function: Greatest Common Denominator")
class gcd:
  def __init__(self, num1, num2):
    self.num1 = 20
    self.num2 = 60
    

  def gcdfunc(self, num1, num2):
    if self.num1 == 0:
        return self.num1
    while self.num2 != 0:
        if self.num1 > self.num2:
            self.num1 = self.num1 - self.num2
        else:
            self.num2 = self.num2 - self.num1
    return self.num1

oop = gcd(20, 60)
print("\nFinding the greatest common denominator of 20 and 60... : ")
print(oop.gcdfunc(18, 200))
print(" ")