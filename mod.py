from datetime import *
import pymysql
def connect():
    mydb = pymysql.connect("localhost","root","passwd","aa")
    return mydb.cursor()
    print ("Connected")
def select(tb):
    mycursor=connect()
    mycursor.execute("Select * from %s"%tb)
    return mycursor.fetchall()
    mycursor.close()

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
    
