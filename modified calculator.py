from tkinter import*
root=Tk()
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
root.title("SIMPLE CALCULATOR")

#defining the buttons

def bclick(numbers):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(numbers))
    
def bclear():
    e.delete(0,END)

def badd():
    first_number=e.get()
    global f_num
    global check
    check="addition"
    f_num=float(first_number)
    e.delete(0,END)

def bsub():
    first_number=e.get()
    global f_num
    global check
    check="subtraction"
    f_num=float(first_number)
    e.delete(0,END)

def bmultiply():
    first_number=e.get()
    global f_num
    global check
    check="multiplication"
    f_num=float(first_number)
    e.delete(0,END)

def bdivide():
    first_number=e.get()
    global f_num
    global check
    check="division"
    f_num=float(first_number)
    e.delete(0,END)

def bequals():
    second_number=e.get()
    e.delete(0,END)
    if check=="addition":
        e.insert(0,f_num+float(second_number))
    if check=="subtraction":
        e.insert(0,f_num-float(second_number))
    if check=="multiplication":
        e.insert(0,f_num*float(second_number))
    if check=="division":
        e.insert(0,f_num/float(second_number))

#creating buttons

b1=Button(root,text="1",padx=39,pady=20,command=lambda:bclick(1))
b2=Button(root,text="2",padx=39,pady=20,command=lambda:bclick(2))
b3=Button(root,text="3",padx=39,pady=20,command=lambda:bclick(3))
b4=Button(root,text="4",padx=39,pady=20,command=lambda:bclick(4))
b5=Button(root,text="5",padx=39,pady=20,command=lambda:bclick(5))
b6=Button(root,text="6",padx=39,pady=20,command=lambda:bclick(6))
b7=Button(root,text="7",padx=39,pady=20,command=lambda:bclick(7))
b8=Button(root,text="8",padx=39,pady=20,command=lambda:bclick(8))
b9=Button(root,text="9",padx=39,pady=20,command=lambda:bclick(9))
b0=Button(root,text="0",padx=39,pady=20,command=lambda:bclick(0))
b_addition=Button(root,text="+",padx=39,pady=20,command=badd)
b_subtraction=Button(root,text="-",padx=39,pady=20,command=bsub)
b_multiplication=Button(root,text="*",padx=39,pady=20,command=bmultiply)
b_division=Button(root,text="/",padx=39,pady=20,command=bdivide)
b_clear=Button(root,text="clear",padx=29,pady=20,command=bclear)
b_equals=Button(root,text="=",padx=38,pady=20,command=bequals)

#positioning of buttons

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)

b_addition.grid(row=1,column=3)
b_subtraction.grid(row=2,column=3)
b_multiplication.grid(row=3,column=3)
b_division.grid(row=4,column=3)
b_clear.grid(row=4,column=1)
b_equals.grid(row=4,column=2)

root.mainloop()
