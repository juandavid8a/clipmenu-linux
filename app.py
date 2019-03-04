#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from Tkinter import *
import subprocess
import time

historicalList = ["pepe", "pepon"]

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def getHistoricalList():  
    i=0
    for x in historicalList:
      i=i+1
      print(x,i) 
      Label(miFrame, text=x).grid(row=i, column=0)
    root.mainloop()  

def hacer_click():
 try:
  _valor = int(entrada_texto.get())
  _valor = _valor * 5
  etiqueta.config(text=_valor)
 except ValueError:
  etiqueta.config(text="Introduce un numero!")
 
root = Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

clip_text = StringVar()
#clip_text = getClipboardData()
clip_text.set(getClipboardData())

etiqueta = Label(miFrame, text="Hola alumnos")
etiqueta.grid(row=0, column=0)
#etiqueta.config(text="Introduce un numero!")
Entry(miFrame, textvariable=clip_text).grid(row=0, column=1)

recent_value = ""
while True:
    tmp_value = getClipboardData()
    if tmp_value != recent_value:
        recent_value = tmp_value
        #print("Value changed: %s" % str(recent_value)[:20])
        historicalList.append(recent_value)
        getHistoricalList()
    time.sleep(0.1)




