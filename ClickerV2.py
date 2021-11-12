import tkinter


Number = 0
OrginColor = 'gray'
def Add():
    global OrginColor
    global Number
    Number += 1
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

root.mainloop()