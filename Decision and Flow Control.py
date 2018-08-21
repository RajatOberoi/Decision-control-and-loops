#Ques1
x=int(input("enter any year"))
if x%400==0:
    print("leap year",x)
elif x%100==0:
    print("not a leap year",x)
elif x%4==0:
    print("leap year",x)
else:
    print("not a leap year")

#Ques2
a=int(input("enter length"))
b=int(input("enter breadth"))
if a==b:
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")

#Ques3
z=int(input("enter age of first person"))
c=int(input("enter age of second person"))
v=int(input("enter age of third person"))
if z>c and z>v:
    print("first person is the oldest")
    if c>v:
        print("third person is the youngest")
    else:
        print("second person is the youngest")
elif c>z and c>v:
    print("second person is the oldest")
    if z>v:
        print("third person is the youngest")
    else:
        print("first person is the youngest")
else:
    print("third person is the oldest")
    if z>c:
        print("second person is the youngest")
    else:
        print("first person is the youngest")

#Ques4
q=int(input("enter age of person"))
w=input("enter sex as M for Male and F for female")
e=input("enter Y if married and N for not")
if w=="F":
    if e=="Y":
        print("person is female and will only work in urban areas and is married and her age is",q)
    else:
        print("person is female and will only work in urban areas and is not married and her age is",q)
elif w=="M":
    if q>=20 and q<40:
        if e=="Y":
            print("person is male and can work anywhere and the person is married and his age is",q)
        else:
            print("person is male and can work anywhere and the person is not married and his age is",q)
    elif q>=40 and q<=60:
        if e=="Y":
            print("person is male and will only work in urban areas and is married and his age is",q)
        else:
            print("person is male and will only work in urban areas and is not married and his age is",q)
    else:
        print("ERROR")

#Ques5
r=int(input("enter no of items you want to purchase"))
l=r*100
if l>1000:
    l=l-(l*0.1)
    print("final cost",l)
else:
    print("final cost",l)

#************************************LOOPS***********************************************************************************
#Ques1
for i in range(10):
    x=int(input("enter no"))
    print(x)

#Ques2
while True:
    print("infinite loop")

#Ques3
h=[]
y=[]
o=int(input("enter no of element in list"))
for i in range(o):
    n=int(input("enter element in the list"))
    h.append(n)
    y.append(n*n)
print(h)
print(y)

#Ques4
r=[]
u=[]
p=[]
k=[5,5.2,6.3,44,"abcde","fgh","jkl",10]
print(k)
for i in k:
    if isinstance(i,int):
        r.append(i)
    elif isinstance(i,float):
        u.append(i)
    elif isinstance(i,str):
        p.append(i)
print(r)
print(u)
print(p)

#Ques5
prime=[]
for num in range(1,101):
    if num>1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
print(prime)
#Ques6
sy="*"
for i in range(5):
    print(i*sy)

#Ques7
d=[]    
f=int(input("enter no of element in the list"))
for i in range(f):
    t=int(input("enter no"))
    d.append(t)
print(d)
j=int(input("enter element you want to delete from list"))
for i in d:
    if i==j:
        d.remove(i)
print(d)        
           

    
        
            
    
        
    
