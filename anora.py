#import sqlite3
#conn=sqlite3.connect("mydb.db")
#cursor=conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS cedvel VALUES(id  PRIMARY KEY, ad text , yas integer )''')

#cursor.execute (''' UPDATE cedvel SET ad='pirveli' WHERE id=7''')
#conn.commit()



#import sqlite3
#conn=sqlite.connect("mydb.db")
#cursor=conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS cedvel (id PRIVACY KEY,ad text, yas integer)''')
#cursor.execute('''SELECT ad FROM cedvel WHERE id =5''')
#k=cursor.fetchall()

#cursor.execute(''' ''')


#a=int(input("a ededini daxil edin:"))
#s=0
#for i in range(1,a+1):
#    s+=i
#print(s)

#import sqlite3
#conn=sqlite3.connect("mydb1.db")
#cursor=conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS cedvel VALUES(id PRIMARY KEY,ad text,yas integer)''')
#cursor.execute('''INSERT INTO cedvel (ad,yas) VALUES('Anora',17)''')
#cursor.execute('''UPDATE cedvel SET ad='Anora' WHERE id=2''')
#conn.commit()


#TEKRAR

#a=546
#a=str(a)
#for i in a:
#    print(i)


#a=input("string daxil edin:")
#for i in a:
#    print(i)


#a=345
#a=str(a)
#for i in a:
#    print(i)


#list1=["alma","armud","heyva"]
#for i in list1:
#    for k in i:
#        print(k)




#list1=["salam","necesen","sagol"]
#for i in list1:
#    for j in i:
#        print("{}-in icinde {} -ni cap etdik".format(i,j))
#print()


#FAKTORIAL(range ve while)




#CLASS

#class Insan:
#    def __init__(self,ad,soyad,yash):
#        self.ad=ad
#        self.soyad=soyad
#        self.yas=yash
#Anora=Insan("Anora","Gaflanova",17)
#print(Anora)



#list1=['salam']
#list2=list1
#list2.append('sagol')
#print(list1)


#list1=['salam']
#list2=list1.copy()
#list2.append('sagol')
#print(list1)


#a=int(input("eded daxil edinn:"))
#hasil=1
#for i in range(1,a+1):
#    hasil=hasil*i
#    print(hasil)


"""a=int(input("eded daxil edin:"))
hasil=1
b=1
while b<=a:
    hasil*=b
    b+=1
print(hasil)"""



"""insan={"ad":"Anora","yash":"17"}
for k,v in insan.items():
    print(k,v)"""


'''list=[1,4,6,3]
list2=[for x**2 in list:]
print(list2)'''



'''import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a)'''





'''import array as arr
list1=[1,2,3,4,5]
list1=[int(x) for x in list1]
a=arr.array('i',list1)
for i in a:
    print(a)'''


'''list2=[1,2,3,4,5]
list3=[x**3 for x in list2]
list3=[]
for x in list2: 
    list3.append(x**3)
print(list3)'''



'''list1=[]
a=int(input("elementlerin sayini daxil edin:"))
for i in range(a):
    list1.append(input())
print(list1)'''

# def getStr():
#         list=[]
#         for i in range(n):
#         text=input("stringi daxil edin:")
#         list.append(text)
#         print(list)
# getStr(n)





# def hesabla(n):
#     sum=0
#     for i in range(n):
#         num=int(input("ededi daxil edin:"))
#         sum+=num
#     print(sum)
# hesabla(6)





# def sum():
#     k=list([1,2,3,4,5])
#     sum=0
#     for i in range(len(k)):
#         if i%==1:
#             sum+=k[i]
#     print(sum)
# sum()





# def tekcut():
#     k=list([1,2,3,4,5,6])
#     sumcut=0
#     sumtek=0
#     for i in range(len(k)):
#         if%2==1:
#             sumtek+=k[i]

#     for i in range(len(k)):
#         if%2==0:
#             sumcut+=k[i]
#     print(sumcut-sumtek)
# tekcut()







































































