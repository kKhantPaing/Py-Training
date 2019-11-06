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
    payrolType=input("1- Payrol Type : ")
    costCentre=input("2- Cost Centre : ")
    schedNo=input("3- Sched No : ")
    effectDate=input("4- Effect Date : ")
    print("Sign On/Off Time")
    signOnOff_1_StartTime=input("Start Time: ")
    signOnOff_1_FinishTime=input("Finish Time: ")
    ss=input("Split Shitf? (y,n)").lower()
    if ss=="y":
        print("Sign On/Off Time(2)")
        signOnOff_2_StartTime=input("Start Time(2) : ")
        signOnOff_2_FinishTime=input("Finish Time(2): ")
    elif ss=="n":
        print("Meal Time")
        mealTime_Start=input("Start Time: ")
        mealTime_Finish=input("Finish Time: ")
    else:
        print("Invalid Input\nReturning to Shift Master Maintenace in 5 sec")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        print("-"*50)
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
