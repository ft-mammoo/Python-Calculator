from tkinter import *
 
root = Tk()

root.title("Calculator")
root.geometry("320x540")
root.config(bg="gray")

entry=Entry(root, width=15, borderwidth=5, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20,sticky=NSEW)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_backspace():
    current = entry.get()
    new = current[:-1]
    entry.delete(0, END)
    entry.insert(0, new)

def button_percentage():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + "%")


button1=Button(root, text="1", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(1))
button2=Button(root, text="2", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(2))
button3=Button(root, text="3", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(3))

button4=Button(root, text="4", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(4))
button5=Button(root, text="5", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(5))
button6=Button(root, text="6", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(6))

button7=Button(root, text="7", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(7))
button8=Button(root, text="8", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(8))
button9=Button(root, text="9", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(9))

button0=Button(root, text="0", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click(0))
button_plus=Button(root, text="+", padx=17, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click("+"))
button_minus=Button(root, text="-", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click("-"))

button_mul=Button(root, text="*", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click("*"))
button_div=Button(root, text="/", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click("/"))
button_equal=Button(root, text="=", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=button_equal)

button_clear=Button(root, text="C", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=button_clear)
button_backspace=Button(root, text="<=", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=button_backspace)
button_decimal=Button(root, text=".", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=lambda: button_click("."))
button_percentage=Button(root, text="%", padx=20, pady=20,fg="#00FFA0",bg="black", font=('Arial', 18), command=button_percentage)

button1.grid(row=3,column=0,columnspan=1,sticky=NSEW,padx=2,pady=2)
button2.grid(row=3,column=1,columnspan=1,sticky=NSEW,padx=2,pady=2)
button3.grid(row=3,column=2,columnspan=1,sticky=NSEW,padx=2,pady=2)

button4.grid(row=2,column=0,columnspan=1,sticky=NSEW,padx=2,pady=2)
button5.grid(row=2,column=1,columnspan=1,sticky=NSEW,padx=2,pady=2)
button6.grid(row=2,column=2,columnspan=1,sticky=NSEW,padx=2,pady=2)

button7.grid(row=1,column=0,columnspan=1,sticky=NSEW,padx=2,pady=2)
button8.grid(row=1,column=1,columnspan=1,sticky=NSEW,padx=2,pady=2)
button9.grid(row=1,column=2,columnspan=1,sticky=NSEW,padx=2,pady=2)

button0.grid(row=4,column=1,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_plus.grid(row=5,column=1,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_minus.grid(row=5,column=0,columnspan=1,sticky=NSEW,padx=2,pady=2)

button_mul.grid(row=4,column=3,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_div.grid(row=3,column=3,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_equal.grid(row=5,column=2,columnspan=4,sticky=NSEW,padx=2,pady=2)

button_clear.grid(row=1,column=3,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_decimal.grid(row=4,column=2,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_backspace.grid(row=2,column=3,columnspan=1,sticky=NSEW,padx=2,pady=2)
button_percentage.grid(row=4,column=0,columnspan=1,sticky=NSEW,padx=2,pady=2)


root.mainloop()
