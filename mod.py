from datetime import *
import pymysql
def connect():
    mydb = pymysql.connect("localhost","root","kkp1219980","test")
    #return mydb.cursor()
    #print ("Connected")
    return mydb
def insert():
    mydb=connect()
    mycursor=mydb.cursor()
    sql="insert into shiftMasterMaintenace values\
    (%s,%s,'AA',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=('a', 'b', 'd', '2019/11/11', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')
    mycursor.execute(sql,val)
    mydb.commit()
    print("OK")
def select(tb):
    mycursor=connect()
    mycursor.execute("Select * from %s"%tb)
    return mycursor.fetchall()
    mycursor.close()
def add12H(t):
    t1=t.split(":")
    if "PM" in t:
        t1[0]=str(int(t1[0])+12)
    return str(t1[0])+":"+str(t1[1][:2])
def add24H(t):
    t=t[1:]
    t=am12(t)
   # print(t,"AAA")
    t1=t.split(":")
    t1[0]=int(t1[0])+24
    return str(t1[0])+":"+str(t1[1])
def am12(t):
    t1=t.split(":")
    if t1[0]=="12" and "AM" in t1[1]:
        return str(0)+":"+str(t1[1][:2])
    else:
        if "AM" in t1[1] or "PM" in t1[1]:
            return t[:-2]
        else:
            return t

def dif_Time(t1,t2,ss='s1'):#under testing
    if("+" in t1):t1=add24H(t1)
    if("+" in t2):t2=add24H(t2)
    if("PM" in t1):t1=add12H(t1)
    else: t1=am12(t1)
    if("PM" in t2):t2=add12H(t2)
    else: t2=am12(t2)
    #print(t1,t2)
    t1=t1.split(":")
    t2=t2.split(":")
    #print(t1,t2,"BBBB")
    t1=int(t1[0])*3600+int(t1[1])*60
    t2=int(t2[0])*3600+int(t2[1])*60
    fd='n'
    if t1>t2:
        x=input("Is the following day?(y,n): ").lower()
        if x=="y":
            t2+=86400
            fd='y'
    if ss=='s1':
        if t2-t1>=28800:
            return ('m',fd)
        else:
            return ('s2',fd)
    elif ss=='s2':
        if t2-t1<7200:
            return False
        else:
            return True
    elif ss=="ss":
        if t2>t1:
            return True
        else:
            return False        
    else:
        if 7200<t2-t1<1800:
            return True
        else:
            return False
