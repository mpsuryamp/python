# a=int(input("enter the limit"))
# count=1
# while (count<=a):
#     print(count)
#     count+=1

a=int(input("enter the limit: "))
count=0
while a!=0:
   a=a//10
   count+=1
print(count)