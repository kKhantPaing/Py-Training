import mod
from datetime import *
def dataEntryMenu():
    DEM=["1-Shift Master Maintenance","2-Roster Code Maintenance","3-Roster Line Maintenance","4-Roster Employee Maintenance"]
    for i in DEM:
        print(i)
    p=input("\nProcess No: ")
    print("-"*50)
    if p=="1":
        shiftMasterMaintenance()
    elif p=="2":
        rosterCodeMaintenance()
def shiftMasterMaintenance():
    li=[input("1- Payroll Type : ")]
    li.append(input("2- Cost Centre : "))
    li.append(input("3- Sched No : "))
    effectDate=input("4- Effect Date : ")
    effectDate=datetime.strptime(effectDate,'%Y/%m/%d')
    if not effectDate>datetime.now():
        print("Effect Date must be future date")
        shiftMasterMaintenance()
    else:
        li.append(effectDate)  
        print("Sign On/Off Time")
        signOnOff_1_StartTime=input("5- Start Time: ")
        li.append(signOnOff_1_StartTime)
        signOnOff_1_FinishTime=input("6- Finish Time: ")
        ss=mod.dif_Time(signOnOff_1_StartTime,signOnOff_1_FinishTime,'s1')
        if ss[1]=='y':signOnOff_1_FinishTime="+"+signOnOff_1_FinishTime
        li.append(signOnOff_1_FinishTime)
        if str(ss[0])!="m":
            print("Sign On/Off Time(2)")
            signOnOff_2_StartTime=input("7- Start Time(2) : ")
            flag=mod.dif_Time(signOnOff_1_FinishTime,signOnOff_2_StartTime,"s2")
            if flag[0]:#NEED MORE TESTING
                if flag[1]=='y':signOnOff_2_StartTime="+"+signOnOff_2_StartTime
                li.append(signOnOff_2_StartTime)
                signOnOff_2_FinishTime=input("8- Finish Time(2): ")
                flag1=mod.dif_Time(signOnOff_2_StartTime,signOnOff_2_FinishTime,ss[0])
                if flag1[0]:
                    if flag1[1]=='y':signOnOff_2_FinishTime="+"+signOnOff_2_FinishTime
                    li.append(signOnOff_2_FinishTime)
                    li.append("0")
                    li.append("0")
                else:
                    print("Invalid Shift Time. Back to Shift Master Maintenace.")
                    shiftMasterMaintenance()
            else:
                print("Second Shift must be at least 2 hours different form First Shift!\nReturn back to Shift Master Maintenace.")
                shiftMasterMaintenance()
        else:
            print("Meal Time")
            li.append("0")
            li.append("0")
            mealTime_Start=input("7- Start Time: ")
            li.append(mealTime_Start)
            mealTime_Finish=input("8- Finish Time: ")
            li.append(mealTime_Finish)
            flag=mod.dif_Time(mealTime_Start,mealTime_Finish,"m")
            if not flag:
                print("Meal time must be between 30 minutes or 2 hours !\nReturn back to Shift Master Maintenace.")
                shiftMasterMaintenance()        
        li.append(input("9- ActiveInd(y,n): ").lower())
        print("Allowance Detail")
        li.append(input("12- Code Description Type Hrs/Amt  : "))
        flag=input("Are you sure want to save?(y,n): ").lower()
        if flag=='y':
            mod.insertschem(*li)
        else:
            print("Back to new Shift Master Maintenace.")
            shiftMasterMaintenance()

def rosterCodeMaintenance():
    li=[input("1- Payroll Type : ")]
    li.append(input("2- Cost Centre : "))
    li.append(input("3- Roster Code : "))
    li.append(int(input("4- No. of Lines: ")))
    li.append(int(input("5- Days in Cycle: "))) 
    flag=input("Are you sure want to save?(y,n): ").lower()
    for i in li:
        print(type(i),i)
    if flag=='y':
        mod.insertroscm(*li)
    else:
        print("Back to new Roster Code Maintenace.")
        rosterCodeMaintenance()


def main():
    mm=["1-Data Entry Menu","2-Process Menu","3-Reports Menu"]
    for i in mm:
        print(i)
    p=input("\nProcess No: ")
    print("-"*50)
    if p=="1":
        dataEntryMenu()
__name__==main()
