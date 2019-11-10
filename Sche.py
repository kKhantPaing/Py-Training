import mod
import time
def dataEntryMenu():
    DEM=["1-Shift Master Maintenace","2-Roster Code Maintenace"]
    for i in DEM:
        print(i)
    p=input("\nProcess No: ")
    print("-"*50)
    if p=="1":
        shiftMasterMaintenace()
def shiftMasterMaintenace():
    li=[input("1- Payroll Type : ")]
    li.append(input("2- Cost Centre : "))
    li.append(input("3- Sched No : "))
    li.append(input("4- Effect Date : "))
    print("Sign On/Off Time")
    signOnOff_1_StartTime=input("5- Start Time: ")
    li.append(signOnOff_1_StartTime)
    signOnOff_1_FinishTime=input("6- Finish Time: ")
    li.append(signOnOff_1_FinishTime)
    ss=mod.dif_Time(signOnOff_1_StartTime,signOnOff_1_FinishTime,'s1')
    if ss[1]=='y':signOnOff_1_FinishTime="+"+signOnOff_1_FinishTime
    if str(ss[0])!="m":
        print("Sign On/Off Time(2)")
        signOnOff_2_StartTime=input("7- Start Time(2) : ")
        li.append(signOnOff_2_StartTime)
        flag=mod.dif_Time(signOnOff_1_FinishTime,signOnOff_2_StartTime,"s2")
        if flag:#NEED MORE TESTING
            signOnOff_2_FinishTime=input("8- Finish Time(2): ")
            flag1=mod.dif_Time(signOnOff_2_StartTime,signOnOff_2_FinishTime,ss[0])
            if flag1:
                li.append(signOnOff_2_FinishTime)
                li.append("0")
                li.append("0")
            else:
                print("Invalid Shift Time. Back to Shift Master Maintenace.")
                shiftMasterMaintenace()
        else:
            print("Second Shift must be at least 2 hours different form First Shift!\nReturn back to Shift Master Maintenace.")
            shiftMasterMaintenace()
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
            shiftMasterMaintenace()        
    li.append(input("9- ActiveInd(y,n): ").lower())
    print("Allowance Detail")
    li.append(input("12- Code Description Type Hrs/Amt  : "))
    flag=input("Are you sure want to save?(y,n): ").lower()
    if flag=='y':
        mod.insert(*li)
    else:
        print("Back to new Shift Master Maintenace.")
        mod.rollback()
        shiftMasterMaintenace()
        

def main():
    mm=["1-Data Entry Menu","2-Process Menu","3-Reports Menu"]
    for i in mm:
        print(i)
    p=input("\nProcess No: ")
    print("-"*50)
    if p=="1":
        dataEntryMenu()
__name__==main()
