from tkinter import *
from tkinter import messagebox
#import mysql.connector
#from mysql.connector import Error
master = Tk()
master.geometry("300x300")
#connection = mysql.connector.connect(host='localhost',
                                        # database='payroll',
                                         #user='mary',
                                        # password='mary123')
#cursor = connection.cursor()
def shiftMasterMaintenance():
    master = Tk()
    master.geometry("800x500")
    def quitFun():
        mg = messagebox.askquestion("Quit", "Are you sure?")
        if mg == 'yes':
            master.destroy()
        else:
            messagebox.showinfo("Retrun", "you will now return to the application screen")

    w = Label(master, text='PAYROLL MASTER SYSTEM', pady=5).grid(row=0)
    w1 = Label(master, text='SHIFT MASTER MAINTENANCE (FIRRIES)', pady=10).grid(row=1)
    t1=StringVar()
    Label(master, text='1- Payrol Type :', anchor=W, pady=5).grid(row=2)
    Entry(master, textvariable=t1).grid(row=2, column=1, padx=10, pady=5)
    t2 = StringVar()
    Label(master, text='2- Cost Centre :', anchor=W, pady=5).grid(row=3)
    Entry(master, textvariable=t2).grid(row=3, column=1, padx=10, pady=5)
    t3 = StringVar()
    Label(master, text='   Sched Type :', anchor=W, pady=5).grid(row=4)
    Entry(master, textvariable=t3).grid(row=4, column=1, padx=10, pady=5)
    t4 = StringVar()
    Label(master, text='3- Sched No :', anchor=W, pady=5).grid(row=5)
    Entry(master, textvariable=t4).grid(row=5, column=1, padx=10, pady=5)
    t5 = StringVar()
    Label(master, text='4- Effect Date :', anchor=W, pady=5).grid(row=6)
    Entry(master, textvariable=t5).grid(row=6, column=1, padx=10, pady=5)
    #
    Label(master, text='SING ON\OFF TIME(1) :', padx=20, anchor=N, pady=5).grid(row=7, column=0)
    t6 = StringVar()
    t7 = StringVar()
    Label(master, text='5- Start Time :', pady=5).grid(row=8, column=0)
    Label(master, text='6- Finish Time:', pady=5).grid(row=9, column=0)
    Entry(master, textvariable=t6).grid(row=8, column=1, pady=5)
    Entry(master, textvariable=t7).grid(row=9, column=1, pady=5)
    #
    Label(master, text='SING ON\OFF TIME(2) :', padx=20, anchor=N, pady=5).grid(row=7, column=2, padx=10)
    t8 = StringVar()
    t9 = StringVar()
    Label(master, text='7- Start Time :', pady=5).grid(row=8, column=2)
    Label(master, text='8- Finish Time:', pady=5).grid(row=9, column=2)
    Entry(master, textvariable=t8).grid(row=8, column=3, pady=5)
    Entry(master, textvariable=t9).grid(row=9, column=3, pady=5)
    #
    Label(master, text=' MEAL TIMES :', padx=20, anchor=N, pady=5).grid(row=11)
    t10 = StringVar()
    t11 = StringVar()
    t12 = StringVar()
    Label(master, text='9- Start Time :', pady=5).grid(row=12)
    Label(master, text='10- Finish Time:', pady=5).grid(row=13)
    Label(master, text='11- Active Ind:', pady=5).grid(row=14)
    Entry(master, textvariable=t10).grid(row=12, column=1, pady=5)
    Entry(master, textvariable=t11).grid(row=13, column=1, pady=5)
    Entry(master, textvariable=t12).grid(row=14, column=1, pady=5)
    #
    Label(master, text='ALLOWANCE DETAILS :', padx=20, anchor=N, pady=5).grid(row=11, column=2)
    t13 = StringVar()
    Label(master, text='12- Code Description Type Hrs/Amt  :', pady=5).grid(row=12, column=2)
    Entry(master, textvariable=t13).grid(row=12, column=3, pady=5)
    frame = Frame(master)
    frame.grid(padx=10, pady=5)
    b1 = Button(frame, text='(Q)uit', padx=10, activeforeground='red', command=quitFun).grid(row=19, column=0)
    b2 = Button(frame, text='(F)ile', padx=10).grid(row=19, column=1)
    b2 = Button(frame, text='(D)elete', padx=10).grid(row=19, column=2)
    Label(master, text='(Q)uit,(F)ile,(D)elete or Number to Change:').grid(row=20)


def rosterCodeMaintenance():
    master = Tk()
    master.geometry("400x300")
    def quitFun():
        mg=messagebox.askquestion("Quit","Are you sure?")
        if mg=='yes' :
            master.destroy()
        else:
            messagebox.showinfo("Retrun","you will now return to the application screen")
    w = Label(master, text='PAYROLL MAS6TER SYSTEM',pady=5).grid(row=1)
    w1 = Label(master, text='Roster Code Maintenance (FIRRIES)',pady=5).grid(row=2)
    Label(master, text='1- Payrol Type :',padx=10,pady=5,anchor=W).grid(row=3)
    Label(master, text='2- Cost Centre',padx=0,pady=5,anchor=W).grid(row=4)
    Label(master, text='3- Roster Code :',padx=0,pady=5,anchor=W).grid(row=5)
    Label(master, text='4- No. of Lines :',padx=0,pady=5,anchor=W).grid(row=6)
    Label(master, text='5- Days in Cycle :',padx=0,pady=5,anchor=W).grid(row=7)
    Entry(master).grid(row=3, column=1,pady=5)
    Entry(master).grid(row=4, column=1,pady=5)
    Entry(master).grid(row=5, column=1,pady=5)
    Entry(master).grid(row=6, column=1,pady=5)
    Entry(master).grid(row=7, column=1,pady=5)
    frame = Frame(master)
    frame.grid(padx=10, pady=5)
    b1 = Button(frame, text='(Q)uit', padx=10,command=quitFun, activeforeground='red').grid(row=8, column=0)
    b2 = Button(frame, text='(F)ile', padx=10).grid(row=8, column=1)
    b2 = Button(frame, text='(D)elete', padx=10).grid(row=8, column=2)
    Label(master, text='(Q)uit,(F)ile,(D)elete or Number to Change:').grid(row=9)


def rosterLineMaintenance():
    master = Tk()
    master.geometry("400x600")
    def quitFun():
        mg=messagebox.askquestion("Quit","Are you sure?")
        if mg=='yes' :
            master.destroy()
        else:
            messagebox.showinfo("Retrun","you will now return to the application screen")

    w = Label(master, text='PAYROLL MASTER SYSTEM',padx=20,pady=5,anchor=W).grid(row=1)
    w1 = Label(master, text='Roster Line Maintenance (FIRRIES)',padx=20,pady=5,anchor=W).grid(row=2)
    Label(master, text='1- Payrol Type :',padx=10,pady=5).grid(row=3)
    Label(master, text='2- Cost Centre',padx=10,pady=5).grid(row=4)
    Label(master, text='3- Roster Code :',padx=10,pady=5).grid(row=5)
    Label(master, text='4- Roster Line :',padx=10,pady=5).grid(row=6)
    Entry(master).grid(row=3, column=1,pady=5)
    Entry(master).grid(row=4, column=1,pady=5)
    Entry(master).grid(row=5, column=1,pady=5)
    Entry(master).grid(row=6, column=1,pady=5)

    w = Label(master, text='Line No',padx=10,pady=5).grid(row=7)
    w = Label(master, text='Sched No',padx=10,pady=5).grid(row=8)
    w = Label(master, text='From Date',padx=10,pady=5).grid(row=9)
    w = Label(master, text='Sign On',padx=10,pady=5).grid(row=10)
    w = Label(master, text='Sign Off',padx=10,pady=5).grid(row=11)
    w = Label(master, text='Sign On',padx=10,pady=5).grid(row=12)
    w = Label(master, text='Sign Off',padx=10,pady=5).grid(row=13)
    w = Label(master, text='Meal Start',padx=10,pady=5).grid(row=14)
    w = Label(master, text='Meal Finish',padx=10,pady=5).grid(row=15)
    w = Label(master, text='Allow Code',padx=10,pady=5).grid(row=16)
    Entry(master).grid(row=7, column=1, pady=5)
    Entry(master).grid(row=8, column=1, pady=5)
    Entry(master).grid(row=9, column=1, pady=5)
    Entry(master).grid(row=10, column=1, pady=5)
    Entry(master).grid(row=11, column=1, pady=5)
    Entry(master).grid(row=12, column=1, pady=5)
    Entry(master).grid(row=13, column=1, pady=5)
    Entry(master).grid(row=14, column=1, pady=5)
    Entry(master).grid(row=15, column=1, pady=5)
    Entry(master).grid(row=16, column=1, pady=5)

    frame = Frame(master)
    frame.grid(padx=10, pady=5)
    b1 = Button(frame, text='(Q)uit', padx=10, activeforeground='red',command=quitFun).grid(row=17, column=0)
    b2 = Button(frame, text='(F)ile', padx=10).grid(row=17, column=1)
    b2 = Button(frame, text='(D)elete', padx=10).grid(row=17, column=2)
    Label(master, text='(Q)uit,(F)ile,(D)elete or Number to Change:').grid(row=18)


def rosterEmployeeMaintenance():
    master = Tk()
    master.geometry("400x400")
    def quitFun():
        mg=messagebox.askquestion("Quit","Are you sure?")
        if mg=='yes' :
            master.destroy()
        else:
            messagebox.showinfo("Retrun","you will now return to the application screen")

    w = Label(master, text='PAYROLL MASTER SYSTEM',padx=10,pady=5,anchor=W).grid(row=1)
    w1 = Label(master, text='Roster Employee Maintenance (FIRRIES)',padx=10,pady=5,anchor=W).grid(row=2)

    Label(master, text='1- Payroll Type :',padx=10,pady=5).grid(row=3)
    Label(master, text='2- Cost Centre:',padx=10,pady=5).grid(row=4)
    Label(master, text='3- Roster Code :',padx=10,pady=5).grid(row=5)
    Label(master, text='4- Roster Line :',padx=10,pady=5).grid(row=6)
    Label(master, text='5- Staff No:',padx=10,pady=5).grid(row=7)
    Label(master, text='6- Start Date :',padx=10,pady=5).grid(row=8)
    Label(master, text='7- Day No :',padx=10,pady=5).grid(row=9)
    Label(master, text='8- Finish Date:',padx=10,pady=5).grid(row=10)
    Entry(master).grid(row=3, column=1,pady=5)
    Entry(master).grid(row=4, column=1,pady=5)
    Entry(master).grid(row=5, column=1,pady=5)
    Entry(master).grid(row=6, column=1,pady=5)
    Entry(master).grid(row=7, column=1,pady=5)
    Entry(master).grid(row=8, column=1,pady=5)
    Entry(master).grid(row=9, column=1,pady=5)
    Entry(master).grid(row=10, column=1,pady=5)

    frame = Frame(master)
    frame.grid(padx=10, pady=5)
    b1 = Button(frame, text='(Q)uit', padx=10, activeforeground='red',command=quitFun).grid(row=11, column=0)
    b2 = Button(frame, text='(F)ile', padx=10).grid(row=11, column=1)
    b2 = Button(frame, text='(D)elete', padx=10).grid(row=11, column=2)
    Label(master, text='(Q)uit,(F)ile,(D)elete or Number to Change:').grid(row=12)

def dataEntryMenu():
    master = Tk()
    master.geometry("350x350")
    master.title("FERRIES SCHEDULE SYSTEM")
    w = Label(master, text='DATA ENTRY MENU',pady=20)
    w.pack()
    btn1 = Button(master, text='1- Shift Master Maintenance', width=25, command=shiftMasterMaintenance,padx=20,pady=20, anchor=W,activeforeground='green').pack()
    btn2 = Button(master, text='2- Roster Code Maintenance', width=25, command=rosterCodeMaintenance,padx=20,pady=20, anchor=W,activeforeground='blue').pack()
    btn3 = Button(master, text='3- Roster Line Maintenance', width=25, command=rosterLineMaintenance,padx=20,pady=20, anchor=W,activeforeground='orange').pack()
    btn4 = Button(master, text='4- Roster Employee Maintenance', width=25, command=rosterEmployeeMaintenance,padx=20,pady=20, anchor=W,activeforeground='cyan').pack()







master.title('FERRIES SCHEDULE SYSTEM')
w = Label(master, text='MAIN MENU',pady=20)
w.pack()
btn1 = Button(master, text='1- Data Entry Menu', width=25, command=dataEntryMenu,pady=10 ,padx=20,anchor=W, bg='#AF7AC5').pack()
btn2 = Button(master, text='2- Process Menu', width=25, pady=10 ,padx=20,anchor=W).pack()
btn3 = Button(master, text='3- Reports Menu', width=25,pady=10 ,padx=20,anchor=W).pack()
btn4 = Button(master, text='4- Enquiry Menu', width=25,pady=10 ,padx=20,anchor=W).pack()
btn5 = Button(master, text='5- System Menu', width=25,pady=10 ,padx=20,anchor=W).pack()
master.mainloop()

