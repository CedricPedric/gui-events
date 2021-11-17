import tkinter
import random


a = 21
score = 0

def randomLabel():
    randomNumber = random.randint(1,8)
    if randomNumber == 1:
        clickOnce()
    elif randomNumber == 2:
        clickTwice()
    elif randomNumber == 3:
        clickTrice()
    elif randomNumber == 4:
        clickW()
    elif randomNumber == 5:
        clickA()
    elif randomNumber == 6:
        clickS()
    elif randomNumber == 7:
        clickD()
    elif randomNumber == 8:
        clickSpace()






    
def MouseScorePlus(event):
    global score
    score += 2
    scoreLabel['text'] = f"Score: {score}"
def KeyBoardPlus(event):
    global score
    score += 1
    scoreLabel['text'] = f"Score: {score}"

def CountDown():
    global a
    global score
    if a  <= 0:
        return
    a -= 1
    stringVar.set(f"Time remaining {a}")
    timeLabel.after(1000,CountDown)

def clickOnce():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Once!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '50', y='50')
    clickWindow.bind("<Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Button-1>"),clickWindow.destroy(),randomLabel()])
    
    
def clickTwice():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Twice!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '50', y='150')
    window.bind("<Double-Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Double-Button-1>"),clickWindow.destroy(),randomLabel()])

def clickTrice():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Click Trice!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '150', y='150')
    window.bind("<Triple-Button-1>",lambda event:[MouseScorePlus(event),window.unbind("<Triple-Button-1>"),clickWindow.destroy(),randomLabel()])

def clickW():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press W!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '250', y='150')
    window.bind("w",lambda event:[KeyBoardPlus(event),clickWindow.destroy(),window.unbind("w"),randomLabel()]) and window.bind("W",lambda event:[KeyBoardPlus(event),clickWindow.destroy(),window.unbind("W"),randomLabel()])

def clickA():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press A!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '30', y='60')
    window.bind("a",lambda event:[KeyBoardPlus(event),window.unbind("a"),clickWindow.destroy(),randomLabel()]) and window.bind("A",lambda event:[KeyBoardPlus(event),window.unbind("A"),clickWindow.destroy(),randomLabel()])


def clickS():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press S!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '80', y='60')
    window.bind("s",lambda event:[KeyBoardPlus(event),window.unbind("s"),clickWindow.destroy(),randomLabel()]) and window.bind("S",lambda event:[KeyBoardPlus(event),window.unbind("S"),clickWindow.destroy(),randomLabel()])
    

def clickD():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press D!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '80', y='60')
    window.bind("d",lambda event:[KeyBoardPlus(event),window.unbind("d"),clickWindow.destroy(),randomLabel()]) and window.bind("D",lambda event:[KeyBoardPlus(event),window.unbind("D"),clickWindow.destroy(),randomLabel()])

def clickSpace():
    clickWindow = tkinter.Label(window)
    clickWindow.config(text = 'Press Space!')
    clickWindow.config(bg='red',fg='black')
    clickWindow.pack(ipady= '20',ipadx='20')
    clickWindow.place(x= '80', y='60')
    window.bind("<space>",lambda event:[KeyBoardPlus(event),window.unbind("<space>"),clickWindow.destroy(),randomLabel()])

def BeginFPS():
    CountDown()
    randomLabel()

window = tkinter.Tk()
window.geometry('300x300')
stringVar = tkinter.StringVar(value=f"Time remaining {a}")

timeLabel = tkinter.Label(window)
timeLabel.config(textvariable=stringVar)
timeLabel.config(bg='black',fg='white')
timeLabel.pack(ipadx= '0',fill='x',expand=True,side='left',anchor='nw')


scoreLabel = tkinter.Label(window)
scoreLabel.config(text=f"Score: {score}")
scoreLabel.config(bg='red',fg='black')
scoreLabel.pack(ipadx= '0',fill='x',expand=True,side='right',anchor='ne')

beginButton = tkinter.Button(window,text='Begin The Shit',command=lambda:[BeginFPS,beginButton.destroy()])
beginButton.place(x= '150', y= '150', anchor='center')




window.mainloop()