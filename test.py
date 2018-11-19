"""import time
admin={'sofm','qtv','archie'}
mem = {'timus','currot','archie'}
allt = admin | mem
chuc2 = admin & mem
kq = admin & mem
for x  in  allt:
    if x in admin :
        if x in chuc2:
            print(x,"giu 2 vai tro")
        else:
             print(x,"la admin")
   
    else:
        print(x,"la member")
    time.sleep(1)"""
"""import time
a={'a','b','c'}
b=list(a)
for x in b:
    time.sleep(1)
    a.remove(x)
    print("da xoa",x)
"""
"""a = dict(a=1,b=2,c=3,d=4,e=5,f=6)
b = a.values()
c = a.keys()
print(b)
print(c)
for x in range(0,len(a)):
    print(list(c)[0+x],':',list(b)[0+x])
"""
"""a = input(" > ")
for x in range(0,len(a)):
    if a[x]=='<':
        print(a[x:])"""


"""nv ={'0001': {'tnv':'player1','cl':1234},
     '0002': {'tnv' :'player2','cl':1235}
     }
a = str(input(" id nguoi choi > "))
print(nv.get(a))"""

"""import random

number = random.randint(1,20)

for y in range(1,7):
    doan=int(input("> "))
    if doan < number:print("so nho hon")
    elif doan > number:print("so lon hon")
    else:break
if doan == number:
    print("ban da doan dung la so {0}".format(str(number)))
else:
    print("Nope, so la {0}".format(str(number)))"""


"""catname=[]
def nhapten():
    print('Enter the name cat of ')
    global name
    name = input()
while True:
    nhapten()
    if name == '':break
    if name in catname:
        print('trung ten')
        nhapten()
    catname+=[name]
print('the cat name are :')
for x in catname:print(x)"""

"""import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for y in message:
    count.setdefault(y,0)
    count[y]+=1
pprint.pprint(count)"""



"""bancaro = {'l1':'','m1':'','r1':'',
           'l2':'','m2':'','r2':'',
           'l3':'','m3':'','r3':''}
turn='X'
def prinboard():
    print('{0} | {1} | {2}'.format(bancaro['l1'],bancaro['l2'],bancaro['r1']))
    print('-'*10)
    print('{0} | {1} | {2}'.format(bancaro['m1'],bancaro['m2'],bancaro['r2']))
    print('-'*10)
    print('{0} | {1} | {2}'.format(bancaro['m1'],bancaro['m2'],bancaro['r3']))
for i in range(9):
    print('Turn',turn)
    move = input("> ")
    bancaro[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    prinboard()"""



"""danhs = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
def tongds(guest,item):
    flag = 0
    for k,v in guest.items():
        print(flag,':',v)
        flag += v.get(item,0)
    return flag
print('apple : {0}'.format(tongds(danhs,'apples')))"""

##a=[]
##for x in range(2000,3200):
##    if x%7==0 and x%5!=0:
##        a.append(str(x))
##print(','.join(a))
##import time
##start = time.time()
##a = int(input("số bất kì > "))
##flag = 1
##for x in range(1,a+1):
##    flag *= x
##print(flag)
##end = time.time()
##print('run time {0:.2f}'.format((end-start)))
##import time
##
##start = time.time()
##n = int(input('>'))
##a = {x:x*x for x in range(1,n+1)}
##end = time.time()
##print(a)
##print('{0:.2f}'.format((end-start)))
##import time
##
##start = time.time()
##b = []
##while True :
##    try:
##        a = input('> ')
##        b.append(a)
##    except KeyboardInterrupt:
##        break
##print(b)
##print(tuple(b))
##end = time.time()
##print('{0:.2f}'.format((end-start))) tu code
##values=input("Nhập vào các giá trị:")
##l=values.split(",")
##t=tuple(l)
##print (l)
##print (t) code web
##nao = ['a','b','c']
##kq =[]
##tb = input('> ')
##hientai = tb.split(',')
##for x in hientai:
##    if x in nao:
##        kq.append(x)
##    else:
##        print(x,'chua hoc')
##for x in kq:
##    if len(kq) == 1 :
##        print('day la chu {0}'.format(x))
##    else:
##        print(x,'day la chu {0}'.format(x))

#du lieu chinh
##nao={'lenh':['hoc','day','chi'],'nganh':['cntt','cong nghe thong tin','congnghethongtin','it']}
##
##
#### phu luc:
##-nao[0] = 
##-nao[1] = 
##################
#du lieu training

##################################
##try:
##    while True:
##        a = input('> ')
##        b = a.split(' ')
##        for x in b:
##            if x in nao['lenh']:
##                if x in nao['nganh']:
##                    nao.append('')
##            else :
##                if x not in nao[0]:
##                    nao[0].append(x)
##                else:
##                    print('> tao da hoc roi')
##            
##           
##            
####    for x in b:
####        if x not in nao[0]:
####            nao[0].append(x)
####        elif x in nao[0]:
####            print('chu {0}'.format(x))
####        elif x in nao[1]:
####            print('so {0}'.format(x))
##except KeyboardInterrupt:


""" web """
##import pymysql
##
##a =  pymysql.connect(host='localhost',
##                user ='root',
##                password='abc@123',
##                db='flask',
##                charset='utf8mb4',)
##
##sql = 'select * from user'
##
##b = a.cursor()
##print(b.execute(sql))
##a.close()
a=[1,2,3]
if type(a[0]) == type(1):
    print('so nguyen')
else:
    print('not')
    
    
