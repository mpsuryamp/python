# def fun(a):
#     print("hai "+a)
# fun("surya")

# def sum(a):
#     c=a*a
#     print(c)
# sum(2)    

# a=input("enter the string:")
# a=a.lower()
# b=a[::-1]
# def palindrome():
#     if a==b:
#       print("PALINDROME")
#     else:
#       print("NOT PALINDROME") 
# # palindrome()         

# limit=int(input("enter the limit :"))
# def fibo():
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,limit):

#          c=a+b
#          print(c)
#          a=b
#          b=c
# fibo() 


# mark=int(input("enter the mark"))
# def subject():
#     if mark>=90 and mark<=100:
#        print("A GRADE")
#     elif mark>=80 and mark<=90:
#        print("B GRADE")
#     elif mark>=70 and mark<=80:
#        print("C GRADE")
#     elif mark>=60 and mark<=70:
#        print("D GRADE")
#     else:
#        print("FAILED")
# subject()           


#counting digits
# def num():
#    a=int(input("enter the limit: "))
#    count=0
#    while a!=0:
#       a=a//10
#       count+=1
#    print(count)
# num()   


# a=int(input("enter the fact number"))
# fact=1
# def facto():
#   if a<0:
#      print("no fact")
#   elif a==0 and a==1:
#      print("fact is 1")
#   else:
#      for i in range(2,a+1):  
#          fact=i*fact
#      print(fact)
# facto() 


def multipli():
  a=int(input("enter the number:"))
  b=int(input("enter the limit :"))
  for i in range(1,b+1):
    c=i*a
    print(i,"*",a,"=",c)
multipli()   


