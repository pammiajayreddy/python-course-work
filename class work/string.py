s=''
s=""
s=''' '''
s="' '"
name='Ajay'
name1="Suni"
name + name1
'AjaySuni'
name+ ' '+ name1
'Ajay Suni'
name
'Ajay'
name * 10
'AjayAjayAjayAjayAjayAjayAjayAjayAjayAjay'
'*'*100
'****************************************************************************************************'
'-'*10
'----------'
name='Ajay Kumar'
name[3]
'y'
name[-2]
'a'
name[-5]
'K'
name[1]
'j'
names='AjaySuniNaviSaiKrishKalyan'
names
'AjaySuniNaviKrishKalyan'
names[0:4]
'Ajay'
names[:4]
'Ajay'
names[4:8]
'Suni'
names[8:12]
'Navi'
names[12:17]
'Krish'
names[17:23]
'Kalyan'
names[23:]
'Kalyan'
names[0:4:2]
'Aa'
names[::3]
'AynaKsaa'
names[-6:]
'Kalyan'
names
'AjaySuniNaviSaiKrishKalyan'
'Ajay' in names
True
'nithin' in names
False
'priya' in names
False
'sahithi' not in names
True
names
'AjaySuniNaviSaiKrishKalyan'
names.upper()
'AJAYSUNINAVIKRISHKALYAN'
names.lower()
'ajaysuninavikrishkalyan'
names.swapcase()
'aJAYsUNInAVIkRISHkALYAN'
l='python programming language'
l.capitalize()
'Python programming language'
l.title()
'Python Programming Language'
"ß".casefold()
'ss'
'priya' in names
False

l
'python programming language'
l.center(100,'*')
'************************************python programming language*************************************'
l.center(50,'*')
'***********python programming language************'
l.center(50,'-')
'-----------python programming language------------'
l.center(50,'_')
'___________python programming language____________'
l.ljust(50,'-')
'python programming language-----------------------'
l.ljust(50,' ')+':'

'python programming language                       :'
l.rjust(50,'-')
'-----------------------python programming language'
'2'.zfill(6)
'000002'
>>> '202'.zfill(6)
'000202'
>>> '202123'.zfill(6)
'202123'
>>> names
'AjaySuniNaviSaiKrishKalyan'
>>> names.find('j')
1
>>> names.find('a')
2
>>> names.find('Ajay')
0
>>> names.find('z')
-1
>>> names.rfind('a')
21
>>> names.index('K')
12
names.index('a')
2
names.rindex('a')
21
names
'AjaySuniNaviSaiKrishKalyan'
names.count('a')
4
names.count('e')
0
names.count('i')
3
names
'AjaySuniNaviSaiKrishKalyan'
names.replace('a','*')
'Aj*ySuniN*viKrishK*ly*n'
names.replace('s','')
'AjaySuniNaviKri hKalyan'
names.replace('Ajay','Reddy')
'ReddySuniNaviSaiKrishKalyan'
names
'AjaySuniNaviSaiKrishKalyan'
names.maketrans('aeiou','*****')
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
names.translate(names.maketrans('aeiou','*****'))
'Aj*yS*n*N*v*Kr*shK*ly*n'
names.translate(names.maketrans('AEIOUaeiou','1234500000'))
'1j0yS0n0N0v0Kr0shK0ly0n'
names.translate(str.maketrans('AEIOUaeiou','1234500000'))
'1j0yS0n0N0v0Kr0shK0ly0n'

