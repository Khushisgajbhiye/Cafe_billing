import sqlite3
from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox
connection = sqlite3.connect('Bills.db')
cursor = connection.cursor()
root = Tk()

root.title("Cafe Billing System")

Tops = Frame(root, width=1350, height=50, bd=8,relief="ridge")
Tops.pack(side=TOP)


f1 = Frame(root, width=1000, height=600, bd=6)
f1.pack(side=RIGHT)
f1a = Frame(f1, width=1000, height=300, bd=8, bg="Grey")
f1a.pack(side=TOP)
f2a = Frame(f1, width=1000, height=300, bd=8, bg="Red")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=500, height=450, bd=8, bg="magenta")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=500, height=450, bd=8, bg="magenta")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=400, height=350, bd=8, bg="Cyan")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=400, height=350, bd=8, bg="Cyan")
f2ab.pack(side=LEFT)

lblInfo = Label(Tops, font=('Monospaced', 24, 'bold'), fg="violet",text="CAFE GREEN", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
#==============================Variables=====================
PaymentRef=StringVar()
delightBurger=StringVar()
paneerBurgers=StringVar()
sweetcornSandwich=StringVar()
nsweetcornSandwich=StringVar()
frenchFries=StringVar()
Coffee=StringVar()
vegPizza=StringVar()
peppy_paneer_Pizza=StringVar()
costvegBurgers=StringVar()
costpaneerBurgers=StringVar()
costsweetcornSandwich=StringVar()
costnsweetcornSandwich=StringVar()
costfrenchFries=StringVar()
costCoffee=StringVar()
costvegPizza=StringVar()
costpeppy_paneer_Pizza=StringVar()
dateRef=StringVar()
subTotal=StringVar()
vat=StringVar()
totalPrice=StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y %H:%M:%S"))
operator = ""
vat.set(0)
PaymentRef.set(0)
delightBurger.set(0)
paneerBurgers.set(0)
sweetcornSandwich.set(0)
nsweetcornSandwich.set(0)
frenchFries.set(0)
Coffee.set(0)
vegPizza.set(0)
peppy_paneer_Pizza.set(0)
subTotal.set(0)
totalPrice.set(0)
costvegBurgers.set(200)
costpaneerBurgers.set(250)
costsweetcornSandwich.set(100)
costnsweetcornSandwich.set(120)
costCoffee.set(70)
costfrenchFries.set(110)
costpeppy_paneer_Pizza.set(250)
costvegPizza.set(150)

#=============================Functions==================
def tPrice():
    vBprice=int(costvegBurgers.get())
    cBprice=int(costpaneerBurgers.get())
    vSprice=int(costsweetcornSandwich.get())
    nSprice=int(costnsweetcornSandwich.get())
    fFprice=int(costfrenchFries.get())
    sDprice=int(costCoffee.get())
    vPprice=int(costvegPizza.get())
    nPprice=int(costpeppy_paneer_Pizza.get())

    vBno=int(delightBurger.get())
    cBno=int(paneerBurgers.get())
    vSno=int(sweetcornSandwich.get())
    nSno=int(nsweetcornSandwich.get())
    fFno=int(frenchFries.get())
    sDno=int(Coffee.get())
    vPno=int(vegPizza.get())
    nPno=int(peppy_paneer_Pizza.get())
    tempVat=int(vat.get())
    subPrice=(vBprice*vBno+cBprice*cBno+vSprice*vSno+nSprice*nSno+vPprice*vPno+nPprice*nPno+fFprice*fFno+sDprice*sDno)
    totalCost=str('%d'%subPrice),"Rs"
    totalCostwithVat=str('%d'%(subPrice +(subPrice*tempVat)/100)),"Rs"
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)
    
    


def iExit():
    qexit= messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit>0:
        root.destroy()
        return

def reset():
    PaymentRef.set(0)
    delightBurger.set(0)
    paneerBurgers.set(0)
    sweetcornSandwich.set(0)
    nsweetcornSandwich.set(0)
    vegPizza.set(0)
    peppy_paneer_Pizza.set(0)
    frenchFries.set(0)
    Coffee.set(0)
    subTotal.set(0)
    totalPrice.set(0)

def refNo():
   refno=int(PaymentRef.get())

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

    
    


#==================================Order Info===========================
lblRef=Label(f1aa,font=('Tahoma',12,'bold'),fg="blue",text="Reference No", bd=16, justify='left', bg="Magenta")
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=PaymentRef, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtRef.grid(row=0,column=1)

ref_no=txtRef.get();
# --------------
lblVb=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="delightBurger", bd=16, justify='left', bg="Magenta")
lblVb.grid(row=1,column=0)
txtVb=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=delightBurger, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtVb.grid(row=1,column=1)
# --------------
lblCb=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="paneerBurgers", bd=16, justify='left', bg="Magenta")
lblCb.grid(row=2,column=0)
txtCb=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=paneerBurgers, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtCb.grid(row=2,column=1)
# --------------
lblVs=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="sweetcornSandwich", bd=16, justify='left', bg="Magenta")
lblVs.grid(row=3,column=0)
txtVs=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=sweetcornSandwich, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtVs.grid(row=3,column=1)
# --------------
lblCs=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="Veggie Affair Sandwich", bd=16, justify='left', bg="Magenta")
lblCs.grid(row=4,column=0)
txtCs=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=nsweetcornSandwich, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCs.grid(row=4,column=1)
# --------------
lblVp=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="vegPizza", bd=16, justify='left', bg="Magenta")
lblVp.grid(row=5,column=0)
txtVp=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=vegPizza, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtVp.grid(row=5,column=1)
# --------------
lblCp=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="peppy_paneer_Pizza", bd=16, justify='left', bg="Magenta")
lblCp.grid(row=6,column=0)
txtCp=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=peppy_paneer_Pizza, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCp.grid(row=6,column=1)
# --------------
lblFf=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="French Fries", bd=16, justify='left', bg="Magenta")
lblFf.grid(row=7,column=0)
txtFf=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=frenchFries, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtFf.grid(row=7,column=1)
# --------------
lblSd=Label(f1aa,font=('Tahoma',12,'bold'),fg="Navy",text="Coffee", bd=16, justify='left', bg="Magenta")
lblSd.grid(row=8,column=0)
txtSd=Entry(f1aa,font=('Tahoma',12,'bold'),textvariable=Coffee, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtSd.grid(row=8,column=1)

#===================================Payment Info==========================
lbldate=Label(f1ab,font=('Tahoma',12,'bold'),fg="blue",text="Date", bd=16, justify='left', bg="Magenta")
lbldate.grid(row=0,column=0)
txtdate=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=dateRef, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtdate.grid(row=0,column=1)

date=txtdate.get()
# --------------
lblCvb=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of delightBurger", bd=16, justify='left', bg="Magenta")
lblCvb.grid(row=1,column=0)
txtCvb=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costvegBurgers, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCvb.grid(row=1,column=1)
# --------------
lblCsd=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of Coffee", bd=16, justify='left', bg="Magenta")
lblCsd.grid(row=8,column=0)
txtCsd=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costCoffee, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCsd.grid(row=8,column=1)
# --------------
lblCvs=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of sweetcornSandwich", bd=16, justify='left', bg="Magenta")
lblCvs.grid(row=3,column=0)
txtCvs=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costsweetcornSandwich, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCvs.grid(row=3,column=1)
# --------------
lblCcs=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of Veggie Affair Sandwich", bd=16, justify='left', bg="Magenta")
lblCcs.grid(row=4,column=0)
txtCcs=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costnsweetcornSandwich, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCcs.grid(row=4,column=1)
# --------------
lblCvp=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of vegPizza", bd=16, justify='left', bg="Magenta")
lblCvp.grid(row=5,column=0)
txtCvp=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costvegPizza, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCvp.grid(row=5,column=1)
# --------------
lblCcp=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of peppy_paneer_Pizza", bd=16, justify='left', bg="Magenta")
lblCcp.grid(row=6,column=0)
txtCcp=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costpeppy_paneer_Pizza, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCcp.grid(row=6,column=1)
# --------------
lblCcb=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of paneerBurgers", bd=16, justify='left', bg="Magenta")
lblCcb.grid(row=2,column=0)
txtCcb=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costpaneerBurgers, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCcb.grid(row=2,column=1)
# --------------
lblCff=Label(f1ab,font=('Tahoma',12,'bold'),fg="Navy",text="Price of French Fries", bd=16, justify='left', bg="Magenta")
lblCff.grid(row=7,column=0)
txtCff=Entry(f1ab,font=('Tahoma',12,'bold'),textvariable=costfrenchFries, bd=10,insertwidth=2, justify='left', bg="Lightyellow")
txtCff.grid(row=7,column=1)
#==========================Total Payment Info======
lblPrice=Label(f2aa,font=('Tahoma',8,'bold'),fg="blue",text="Price", bd=16, justify='left', bg="Cyan")
lblPrice.grid(row=0,column=0)
txtPrice=Entry(f2aa,font=('Tahoma',8,'bold'),textvariable=subTotal, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtPrice.grid(row=0,column=1)
# --------------
lblVat=Label(f2aa,font=('Tahoma',8,'bold'),fg="blue",text="TAX", bd=16, justify='left', bg="Cyan")
lblVat.grid(row=1,column=0)
txtVat=Entry(f2aa,font=('Tahoma',8,'bold'),textvariable=vat, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtVat.grid(row=1,column=1)
# --------------
lblTp=Label(f2aa,font=('Tahoma',8,'bold'),fg="blue",text="Total Price", bd=16, justify='left', bg="Cyan")
lblTp.grid(row=2,column=0)
txtTp=Entry(f2aa,font=('Tahoma',8,'bold'),textvariable=totalPrice, bd=10,insertwidth=2, justify='left', bg="LightYellow")
txtTp.grid(row=2,column=1)
total_price=txtTp.get()
#==============Buttons==========

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Bills(Ref No INTEGER,Date TEXT,Total Price INTEGER)')
    connection.commit()
create_table();


def entries():
    cursor.execute("INSERT INTO Bills VALUES(?,?,?)",(txtRef.get(),txtdate.get(),txtTp.get()))
    connection.commit()



btnTotal=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Total Price",command=tPrice).grid(row=0,column=0)
btnBill=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Create Bill",command=entries).grid(row=0,column=1)
btnReset=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Reset",command=reset).grid(row=1,column=0)
btnExit=Button(f2ab,padx=16,pady=16,bd=8, fg="brown",font=('arial',8,'bold'),width=15,
                text="Exit",command=iExit).grid(row=1,column=1)



root.mainloop()