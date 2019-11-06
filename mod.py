from datetime import *
import pymysql
def connect():
    mydb = pymysql.connect("localhost","root","kkp1219980","test")
    return mydb.cursor()
    print ("Connected")
    return mydb
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
    t=t.split(":")
    t[0]=int(t[0])+24
    return str(t[0])+":"+str(t[1])

def dif_Time(t1,t2):#under testing
    if("PM" in t1):t1=add12H(t1)
    else: t1=t1[:-2]
    if("PM" in t2):t2=add12H(t2)
    else: t2=t2[:-2]
    if("+" in t1):t1=add24H(t1)
    if("+" in t2):t2=add24H(t2)
    print(str(t1)+"   "+str(t2))


def diff_Time(t1,t2):
    dt=t2-t1
    if (dt.total_seconds()>7800):
        return True
    else:
        return False

def hour(t1,t2):
    if t1.hour<t2.hour:
        if t1.date<t2.date:
            return("+"+str(t2.hour))
