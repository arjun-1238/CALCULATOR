import tkinter as tk
from tkinter import*
import random
import re
import math

root=tk.Tk()
root.title("Calculator")
root.geometry("460x690")
root.configure(bg="lightblue")
root.resizable(False, False)

scvalue=StringVar()
scvalue.set("")
ans=0
memory=0
entry=Entry(root,textvariable=scvalue,width=20,font='Arial 28 bold', fg="black",justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=20, pady=25, ipady=15)

def sin_deg(text1):
    text1 = text1.replace("sin", "math.sin(math.radians")
    text1 = text1.replace(")","))")
    return eval(text1)


def click(event):
    global ans,memory
    try:
        text=event.widget.cget("text")

        if text == "AC":
            scvalue.set("")

        elif text == "Back":
            scvalue.set(scvalue.get()[:-1])

        elif text == "%":
            if scvalue.get():
                scvalue.set(scvalue.get() + "/100")

        elif text == "1/x":
            scvalue.set(scvalue.get() + "^(-1)")

        elif text == "√x":
            scvalue.set(scvalue.get() + "**0.5")

        elif text == "³√x":
            scvalue.set(scvalue.get() + "**(1/3)")

        elif text == "ʸ√x":
            scvalue.set(scvalue.get() + "**(1/")

        elif text == "x²":
            if scvalue.get()=="":
                scvalue.set("0"+"²")

            else: scvalue.set(scvalue.get() + "²")

        elif text == "x³":
            if scvalue.get()=="":
                scvalue.set("0"+"³")

            else : scvalue.set(scvalue.get() + "³")

        elif text == "xʸ":
            if scvalue.get() == "":
                scvalue.set("0" + "^")
            else:scvalue.set(scvalue.get() + "^")

        elif text == "π":
            if scvalue.get()=="" :
                scvalue.set("π")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + text)
            elif scvalue.get()[-1] not in ("+","-","*","/","^"):
                scvalue.set(scvalue.get() + "*" + text)
            else : scvalue.set(scvalue.get() + text)


        elif text == "e":
            if scvalue.get()=="":
                scvalue.set("e")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + text)
            elif scvalue.get()[-1] not in ("+","-","*","/","^"):
                scvalue.set(scvalue.get() + "*" + text)
            else:
                scvalue.set(scvalue.get() + text)

        elif text == "eˣ":
            if scvalue.get()=="":
                scvalue.set("e"+"^")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + "e^")
            elif scvalue.get()[-1]  not in ("+","-","*","/","^") :
                scvalue.set(scvalue.get()  + "*e" +"^")
            else:
                scvalue.set(scvalue.get()+"e"+"^")


        elif text in ("sin", "cos", "tan"):
            scvalue.set(scvalue.get() + text + "(")

        elif text == "log":
            if scvalue.get() == "":
                scvalue.set(text + "(")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + "log(")
            elif scvalue.get()[-1] not in ("+","-","*","/","^") :
                scvalue.set(scvalue.get() + "*log(")
            else:
                scvalue.set(scvalue.get()  + text + "(")

        elif text == "ln":
            if scvalue.get() == "":
                scvalue.set(text + "(")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + "ln(")
            elif scvalue.get()[-1] not in ("+","-","*","/","^") :
                scvalue.set(scvalue.get() + "*ln(")
            else:
                scvalue.set(scvalue.get()  + text + "(")

        elif text == "n!":
            scvalue.set(scvalue.get() + "!")


        elif text == "RND":
            if scvalue.get() == "" or scvalue.get()[-1] in ("(","+","-","*"):
                scvalue.set(scvalue.get() + str(round(random.random(), 4)))

            else:
                scvalue.set(scvalue.get()+ "*" + str(round(random.random(),4)))

        elif text == "EXP":
            if scvalue.get() == "":
                scvalue.set("10^(")
            elif scvalue.get()[-1] == "(":
                scvalue.set(scvalue.get() + "10^")
            elif scvalue.get()[-1]  in ("+","-","*","/") or  scvalue.get()[-1]=="^":
                scvalue.set(scvalue.get()  + "10^")
            else:
                scvalue.set(scvalue.get() +  "*" + "10^")

        elif text == "MC":
            memory = 0
            scvalue.set("Clear Memory")

        elif text == "MR":
            scvalue.set(str(memory))

        elif text == "M+":
            if scvalue.get():
                memory += float(scvalue.get())

        elif text == "M-":
            if scvalue.get():
                memory -= float(scvalue.get())

        elif text in ("1","2","3","4","5","6",'7',"8","9","0"):
            if scvalue.get()!="" and scvalue.get()[-1] in (")","e","π","10ˣ"):
                scvalue.set(scvalue.get()+"*"+text)
            else:
                scvalue.set(scvalue.get()+text)

        elif text == "=":

            text1 = scvalue.get()

            text1 = text1.replace("π", "math.pi")
            text1 = text1.replace("log", "math.log10")
            text1 = text1.replace("ln", "math.log")
            text1 = text1.replace("²", "**2")
            text1 = text1.replace("³", "**3")
            text1 = text1.replace("^", "**")
            text1 = text1.replace("e","math.e")


            if v.get() == 2:
                text1 = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', text1)
                text1 = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', text1)
                text1 = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', text1)


            else:
                text1 = re.sub(r'sin\((.*?)\)', r'math.sin(\1)', text1)
                text1 = re.sub(r'cos\((.*?)\)', r'math.cos(\1)', text1)
                text1 = re.sub(r'tan\((.*?)\)', r'math.tan(\1)', text1)


            while "!" in text1:
                idx = text1.index("!")
                j = idx - 1
                if text1[j] == ")":
                    count = 1
                    j -= 1
                    while j >= 0:
                        if text1[j] == ")":
                            count += 1
                        elif text1[j] == "(":
                            count -= 1
                            if count == 0:
                                break
                        j -= 1
                else:
                    while j >= 0 and text1[j].isdigit():
                        j -= 1
                    j += 1

                expr = text1[j:idx]
                value = eval(expr)

                if value < 0 or int(value) != value:
                    raise ValueError("Invalid factorial")

                fact = math.factorial(int(value))
                text1 = text1[:j] + str(fact) + text1[idx + 1:]

            ans = eval(text1)
            scvalue.set(ans)

        else:
            scvalue.set(scvalue.get() + text)

    except:
        scvalue.set("Error")

buttons=[ ["sin", 'cos' ,"tan" ] , ["xʸ", "x³", "x²", "π" , "e" ],
         ["ʸ√x","1/x" , "√x", "eˣ", "log"],["(",")","%" , "ln", "Back"],
         ['7','8','9',"MR","AC"],['4','5','6','+',"M+"],['1','2','3',"-","M-"],
         ['0',".","EXP","*","M-"],["n!","RND","=","/","MC"]]

v = tk.IntVar()
v.set(1)
tk.Radiobutton(root, text="Rad",font="seoge 8 bold", variable=v, value=1,width=6,height=2,
               bg="Yellow",fg="black",activebackground="white").grid(row=1,column=3)
tk.Radiobutton(root, text="Deg",font="seoge 8 bold", variable=v, value=2,width=6,height=2,
               bg="yellow",fg="black",activebackground="white").grid(row=1,column=4)

for i,row in enumerate(buttons):
    for j,btn in enumerate(row):
        bg = "black"
        if btn=="":
            bg="lightblue"

        if btn in ("+", "-", "*", "/","MR"):
            bg = "orange"
        elif btn == "=":
            bg = "green"
        elif btn in ("AC","Back","MC"):
            bg = "red"
        elif btn in ("sin", "cos", "tan", "ln", "log",
                     "xʸ", "x²", "x³", "eˣ",
                     "ʸ√x", "³√x", "1/x","√x", "π", "e"):
            bg = "blue"

        b = Button(root,text=btn,font=("Segoe UI", 12, "bold"),width=6,height=2,bg=bg,fg="white",
            activebackground="lightgrey",activeforeground="black")
        b.grid(row=i+1, column=j)
        b.bind("<Button-1>", click)
root.mainloop()
