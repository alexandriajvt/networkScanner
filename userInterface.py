import tkinter as tk
from tkinter import*
from findNetworks import networkScanner
from scanner import*
import time

frame=Tk()
frame.title("SEARCH MY NETWORK")
frame.geometry('750x600')
var1=IntVar(frame)
var2=IntVar(frame)

var=[]

def getIP():#OPENS TEXTBOX
    startButton.config(state=DISABLED)
    global entry
    entry = Entry()#creates a one-line textbox called entry
    entry.config(font=('Courier',10), bg='black',fg='#F81894', width=50)#change font to 'Ink Free'
    entry.insert(0,'Enter IP Address: ')
    submit.pack(side= BOTTOM)#submit button pops up for user to press
    entry.pack()

def submitIP():
    submit.destroy()#remove submit button
    global givenIP
    givenIP= entry.get()
    networkScanner(givenIP)#writes to a file
    a= open("devices.txt" , "r+")
    deviceOutput = a.read()
    a.close()
    lbl=Label(frame,text="")
    lbl.pack()
    deviceLabel = Label(frame , text = str(deviceOutput),justify=LEFT)
    deviceLabel.pack()
    openCheckboxes.pack()

def clearFrame(win):
     for widgets in win.winfo_children():
          widgets.destroy()
          
def selectDevices():
    clearFrame(frame)
    deviceList=open("specifics.txt").readlines()#creates a list of host ip addresses
    #prints checkboxes

    index=0
    for x in range(12):
        for y in range(3):
                if((x+y+index)>=len(deviceList)):
                     break
                var.append(IntVar(frame))
                Checkbutton(frame,text=deviceList[x+y+index],variable=var[x+y+index]).grid(row=x,column=y) #x+y+index keeps sequential order of deviceList
        index=index+2
    
    Button(frame, text="Run Scan Now",command=runPortScan, width=20, height=2,bg='#B8B8B8',fg='#F81894').grid(row=5,column=5)#15,12
    
 
def runPortScan():
    file_obj = open("specifics.txt","r")
    file_data = file_obj.read()
    deviceList = file_data.splitlines()
    file_obj.close()

    for checkbox in range(len(var)):
        if(var[checkbox].get()==1):
             scanningPorts(deviceList[checkbox])
    printResults()


    lab= open("openPorts.txt","r")
    portOutput=lab.read()
    clearFrame(frame)
    portLabel=Label(frame,text=str(portOutput),font=('Courier',12), width=48, height=16,bg='#B8B8B8',fg='#F81894')
    time.sleep(3)
    portLabel.pack(anchor=CENTER)


startButton=Button(frame,text="Search for Devices",command=getIP,width=20,height=2,bg='#B8B8B8',fg='#F81894') #
startButton.pack()#start button appears and is pressed at start of program

submit=Button(frame,text="Search Now",command=submitIP,width=20,height=2,bg='#B8B8B8',fg='#F81894')
openCheckboxes=Button(frame,text="Check for Open Ports",command=selectDevices,width=20,height=2,bg='#B8B8B8',fg='#F81894')


frame.mainloop()