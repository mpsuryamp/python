# a=[1,2,3,3,3]
# for i in a:
#     print(i)
# for i in range(1,6):
#     print(i) 5

# a=[1,2,3,4,5,6]
# for i in range(2,7,2):        
#     print(i)

# a=[1,2,3,4]
# sum=0
# for i in a:
#     if i%2==0:
#         sum=sum+i
#         print
#         (sum)
# a=int(input("enter the number a:"))
# b=int(input("enter the limit b:"))
# for i in range(1,b+1):
#     c=i*a
#     print(i,"*",a,"=",c)

#fibonocci
limit=int(input("enter the limit :"))
a=0
b=1
print(a)
print(b)
for i in range(2,limit):
    c=a+b
    print(c)
    a=b
    b=c



