import tkinter
from tkinter.constants import TRUE


Number = 0
OrginColor = 'gray'
ClickedUp = False
ClickedDown = False

def Add():
    global OrginColor
    global Number
    global ClickedUp 
    global ClickedDown
    ClickedUp = True
    ClickedDown = False
    Number +=1 
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'

def Sub():
    global OrginColor
    global Number
    global ClickedDown
    global ClickedUp
    ClickedUp = False
    ClickedDown = True

    Number -= 1
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
        OrginColor = 'green'
    elif Number < 0:
        root['background'] = 'red'
        OrginColor = 'red'
    else:
        root['background'] = 'gray'
        OrginColor = 'gray'

def LabelClick(event):
    global ClickedDown
    global ClickedUp
    global Number

    if ClickedUp:
        Number = Number * 3
    else:
        Number = round((Number/3),2)
    numberLabel['text'] = Number

def ColorChange(event):
    global OrginColor
    root["background"] = 'yellow'
def ColorChange1(event):
    root["background"] = OrginColor

root = tkinter.Tk()
root.configure(bg='gray')
root.geometry('300x300')

buttonUp = tkinter.Button(root)
buttonUp.configure(text= 'Up', command=Add)
buttonUp.pack(padx=50,pady=50,expand=True)

buttonDown = tkinter.Button(root)
buttonDown.configure(text= 'Down', command=Sub)
buttonDown.pack(padx=50,pady=50,expand=True)

numberLabel = tkinter.Label(root, text = Number)
numberLabel.pack(ipadx=20,ipady=20)

root.bind("<Enter>",ColorChange)
root.bind("<Leave>",ColorChange1)
root.bind("+",Add)
root.bind("-",Sub)
root.bind("<Up>",Add)
root.bind("<Down>",Sub)
numberLabel.bind("<Double-Button-1>",LabelClick)

root.mainloop()