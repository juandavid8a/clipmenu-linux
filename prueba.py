from Tkinter import *
import subprocess

master = Tk()
miFrame=Frame(master, width=500, height=400)
miFrame.pack()
#text = Text(miFrame)
#text.pack()

#label = Label(miFrame)
#label.pack()

def elOk(item):
    print(item)

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def my_mainloop():
    global recent_value  
    global i    
    tmp_value = getClipboardData()
    if tmp_value != recent_value:
        i=i+1
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value)[:20]) 
        Button(miFrame, text=recent_value, width=25, command=elOk("pepe")).pack()
        #text.insert(END, recent_value +str(i))
    master.after(1000, my_mainloop)    

i=0
recent_value = getClipboardData()

master.after(1000, my_mainloop)
master.mainloop()