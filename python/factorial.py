a=int(input("enter the fact number"))
fact=1
if a<0:
    print("no fact")
elif a==0 and a==1:
    print("fact is 1")
else:
     for i in range(2,a+1):  
         fact=i*fact
     print(fact)

#palidrome
a=input("enter the string: ")
a=a.lower()
b=a[::-1]
if a==b:
    print("PALINDROME")
else:
    print("NOT PALINDROME")    

            


    