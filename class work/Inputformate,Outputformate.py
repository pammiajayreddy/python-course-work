name=input("Enter the name: ")
Enter the name: Ajay
name
'Ajay'
age=int(input("Enter the age: "))
Enter the age: 23
age
23
discount=float
discount=float(input("Enter the discount: "))
Enter the discount: 2.1
discount
2.1
names=input()
ajay suni hyma
names
'ajay suni hyma'
names=input().split()
ajay suni hyma
names
['ajay', 'suni', 'hyma']
names=input().split()

12 23 45 65
names
['12', '23', '45', '65']
names=map(int,input().split())
12 32 4 6 
names
<map object at 0x0000021E48EABA90>
names=list(map(int,input().split()))
12 34 5 6
names
[12, 34, 5, 6]
names=list(map(float,input().split()))
3546.34 5678.23 56 234 12
names
[3546.34, 5678.23, 56.0, 234.0, 12.0]
names=tuple(input().split())
sfdgh rtyuio tryui 
names
('sfdgh', 'rtyuio', 'tryui')
names=tuple(map(int,input().split()))
1 2 3 4 5 7
names
(1, 2, 3, 4, 5, 7)
names=tuple(map(float,input().split()))
1 2  7 9 5 
names
(1.0, 2.0, 7.0, 9.0, 5.0)
names=set(map(int,input().split()))
1 2 3 4
names
{1, 2, 3, 4}
names=set(map(float,input().split()))
1 2 3 4 
names
{1.0, 2.0, 3.0, 4.0}
names=set(input().split())
fdghj dgfhjk gfhj kl
names
{'dgfhjk', 'fdghj', 'kl', 'gfhj'}
d=eval(input())
{'name':'xyz','age':21}
d
{'name': 'xyz', 'age': 21}
d=eval(input())

[1,2,3,4,5]
d
[1, 2, 3, 4, 5]
d=eval(input())

"python"
d
'python'
s=input().split()
xyz xyz@123
s
['xyz', 'xyz@123']
a,b=['xyz', 'xyz@123']
a
'xyz'
b
'xyz@123'
name,email=input("Enter the name and email: ").split()
Enter the name and email: ajay ajayreddy@gmail.com
name
'ajay'
email
'ajayreddy@gmail.com'
a,b=list(map(int,input().split()))
12 34
a
12
b
34
a,b,c=10,20,30
a
10
b
20
c
30
print("These are vari")
These are vari
print("a=",a,"b=",b,"c=",c)
a= 10 b= 20 c= 30
print("a=",a,"\nb=",b,"\nc=",c)
a= 10 
b= 20 
c= 30
print("a=",a,"\tb=",b,"\tc=",c)
a= 10 	b= 20 	c= 30
>>> print("a=",a,"\tb=",b,"\tc=",c,sep='')
a=10	b=20	c=30
>>> print("a=",a,"\tb=",b,"\tc=",c,sep='\t\t')
a=		10			b=		20			c=		30
>>> print("a=",a,"b=",b,"c=",c,end='\n\n\n')
a= 10 b= 20 c= 30


>>> print(f'a={a}\nb={b}\nc={c}')
a=10
b=20
c=30
>>> print(f'a={a}\tb={b}\tc={c}')
a=10	b=20	c=30
a=10
b=23.4
c="string"
print('a=%d\nb=%f\c=%s'%(a,b,c))
a=10
b=23.400000\c=string
print('a=%d\nb=%f\nc=%s'%(a,b,c))
a=10
b=23.400000
c=string
print('a=%d\nb=%.2f\nc=%s'%(a,b,c))
a=10
b=23.40
c=string
print('a={}\tb={}\tc={}'.format(a,b,c))
a=10	b=23.4	c=string
print('a={2}\tb={1}\tc={0}'.format(a,b,c))
a=string	b=23.4	c=10
