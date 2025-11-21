t=()
t=tuple()
t
()
t=(1,2,3,4,5,1,2,4)
t
(1, 2, 3, 4, 5, 1, 2, 4)
t=tuple((1,2,3,4,5))
t
(1, 2, 3, 4, 5)
t=1,2,3,4,5
t
(1, 2, 3, 4, 5)
t=(1)
t
1
t=[1]
t
[1]
t
[1]
t=(1)
t=(1,)
t
(1,)
t=('int','float','complex','bool','set','dict','list','tuple','string')

t[1]
'float'
t[-1]
'string'
t[-2]
'tuple'
t[-5]
'set'
t[2]
'complex'
t[3]
'bool'
t
('int', 'float', 'complex', 'bool', 'set', 'dict', 'list', 'tuple', 'string')
t[3:6]
('bool', 'set', 'dict')
t[-1:-4]
()
t[-1:-4:-1]
('string', 'tuple', 'list')
t[-1:-4:1]
()
t[-3:]
('list', 'tuple', 'string')
t[2::-1]
('complex', 'float', 'int')
t[::2]
('int', 'complex', 'set', 'list', 'string')
t[::-2]
('string', 'list', 'set', 'complex', 'int')
t1=(1,2,3)
t2=(7,8,9)
t1+t2
(1, 2, 3, 7, 8, 9)
t1*5
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t1
(1, 2, 3)
3 in t1
True
5 in t1
False
4 not in t1
True
1 not in t1
False
t=(10,20,30)
a,b,c=t
a
10
b
20
c
30
t=('Uname','mail@gmail.com','Pwd@123')
t[0]
'Uname'
t[1]
'mail@gmail.com'
t[2]
'Pwd@123'
uname,mail,pwd=t
uname
'Uname'
mail
'mail@gmail.com'
pwd
'Pwd@123'
t
('Uname', 'mail@gmail.com', 'Pwd@123')
t=(1, 2, 3, 1, 2, 3, 1, 2)
t.count(2)
3
t.count(3)
2
t.count(1)
3
t.index(2)
1
len(t)
8
max(t)
3
>>> min(t)
1
>>> sum(t)
15
>>> t
(1, 2, 3, 1, 2, 3, 1, 2)
