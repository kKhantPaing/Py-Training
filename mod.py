from datetime import *
import pymysql
def connect():
    mydb = pymysql.connect("localhost","tester","123","test")
    return mydb
def insertschem(*li):
    mydb=connect()
    mycursor=mydb.cursor()
    sql="insert into shiftMasterMaintenance values\
    (%s,%s,'AA',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[10],li[11])
    mycursor.execute(sql,val)
    mydb.commit()
    print("Saved!")
    mycursor.close()

def insertroscm(*li):
    mydb1=connect()
    mycursor1=mydb1.cursor()
    sql1="insert into rosterMaintenance values (%s,%s,%s,%s,%s)"
    val1=(li[0],li[1],li[2],li[3],li[4])
    mycursor1.execute(sql1,val1)
    mydb1.commit()
    print("Saved!")
    mycursor1.close()

def select(tb):
    mydb=connect()
    mycursor=mydb.cursor()
    mycursor.execute("Select * from %s"%tb)
    return mycursor.fetchall()
    mycursor.close()

def fdy(t):
    amfd={+12:"24",+1:"25",+2:"26",+3:"27",+4:"28",+5:"29",+6:"30",+7:"31",+8:"32",+9:"33",+10:"34",+11:"35"}
    pmfd={+12:"36",+1:"37",+2:"38",+3:"39",+4:"40",+5:"41",+6:"42",+7:"43",+8:"44",+9:"45",+10:"46",+11:"47"}
    t1=t[1:].split(":")
    if "AM" in t1[1]:
        return str(amfd[int(t1[0])])+":"+str(t1[1][:-2])
    else:
        return str(pmfd[int(t1[0])])+":"+str(t1[1][:-2])

def td(t):
    am={12:"0",1:"1",2:"2",3:"3",4:"4",5:"4",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11"}
    pm={12:"12",1:"13",2:"14",3:"15",4:"16",5:"17",6:"18",7:"19",8:"20",9:"21",10:"22",11:"23"}
    t1=t.split(":")
    if "AM" in t1[1]:
        return str(am[int(t1[0])])+":"+str(t1[1][:-2])
    else:
        return str(pm[int(t1[0])])+":"+str(t1[1][:-2])
    
def dif_Time(t1,t2,ss='s1'):#under testing
    if("+" in t1):t1=fdy(t1)
    else:t1=td(t1)
    if("+" in t2):t2=fdy(t2)
    else:t2=td(t2)
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
            return (t2-t1,fd)
    elif ss=='m':
        if (t2-t1) in range(1800,7201):
            return (True,fd)
        else:
            return (False,fd)
    
    elif ss=="s2":
        if t2-t1>=7200:
            return (True,fd)
        else:
            return (False,fd)    
    else:
        if t2-t1<ss:
            return (False,fd)
        else:
            return (True,fd)

