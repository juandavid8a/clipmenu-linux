from Tkinter import *
import pyperclip

master = Tk()
miFrame=Frame(master, width=500, height=400)
miFrame.pack()
#text = Text(miFrame)
#text.pack()

#label = Label(miFrame)
#label.pack()

history = []

def createButton(itemText):
    global history
    
    try:
        history.index(recent_value) >= 0
    except:
        history.append(recent_value)
        Button(miFrame, text=itemText, width=25, command=lambda:setClipboardData(itemText)).pack()
    else:
        print(history)

def getClipboardData():
    data = pyperclip.paste()
    return data

def setClipboardData(thedata):
    print(thedata)
    pyperclip.copy(thedata)

def my_mainloop():
    global recent_value      
    tmp_value = getClipboardData()

    if tmp_value != recent_value:
       recent_value = tmp_value 
       createButton(recent_value)
     #   print("Value changed: %s" % str(recent_value)[:20])
    master.after(1000, my_mainloop)    

recent_value = getClipboardData()

master.after(1000, my_mainloop)
master.mainloop()