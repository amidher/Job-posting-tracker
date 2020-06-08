# -*- coding: utf-8 -*-
"""
Created on Fri May 29 05:52:09 2020

@author: Alawi Midher
"""

import pandas as pd
import webbrowser
from tkinter import *
from datetime import date

head=['University Name','Location','Type','Last_job_vacancy','Applocation_Status','Last_check','Recruitment_Page']
df=pd.read_csv('Academic.csv',delimiter = ',',names = head, header=0)
print(df.shape)
listsize=df.shape[0]

#Drop rows if University name is null
dll=df['University Name'].isnull()
#dll=df['University Name'].index[dll]
#df=df.drop(dll)
        

##################################################################
def SaveB():
    global df,CheckVar1,CheckVar2,appLink,label3
    is_posted=CheckVar1.get()
    is_applied=CheckVar2.get()
    label3.config(text='Save done!')
    
    if is_posted:
        if is_applied:
            df.loc[i, 'Applocation_Status']=appLink.get()
            df.loc[i, 'Last_job_vacancy']=date.today()
        else:
            df.loc[i, 'Applocation_Status']="APPLY"
################################################################## 
def NextB():
    global link,i,u_nmae,df,label1,master,label3
    label3.config(text='')

    if i<listsize-1:  
        df.loc[i, 'Last_check']= date.today() #Update the "last Check" date to the last check date
        i+=1
        linktemp=next(link)
        webbrowser.open(linktemp, new=2)
        
        u_nmae=df.loc[i, 'University Name']
        label1.config(text="University Name: {}".format(u_nmae))
    else:
        master.destroy()
        
##################################################################
def SkipB():
    global link,i,u_nmae,df,label1,master,label3
    label3.config(text='')
    
    if i<listsize-1:  
        i+=1
        linktemp=next(link)
        webbrowser.open(linktemp, new=2)
        u_nmae=df.loc[i, 'University Name']
        label1.config(text="University Name: {}".format(u_nmae))
    else:
        master.destroy()
##################################################################

links=df['Recruitment_Page']
i=0
link=iter(links)
u_nmae=df.loc[i, 'University Name']
webbrowser.open(next(link), new=2)

#Create Gui
master = Tk() 
master.title('Academic Jobs Check') 

#Create Label
label1=Label(master, text="University Name: {}".format(u_nmae))
label1.grid(row=0,column=0,sticky=W)
label2=Label(master, text="Application Link: ").grid(row=3,column=0,sticky=W)
label3=Label(master, text="",fg="green")
label3.grid(row=0,column=2,sticky=E)

#create buttons
button1 = Button(master, text='Save', width=25, command=SaveB).grid(row=4,column=0,columnspan=3,sticky=W)
button2 = Button(master, text='Next', width=25, command=NextB).grid(row=4,column=1,columnspan=3,sticky=W)
button3 = Button(master, text='Skip', width=25, command=SkipB).grid(row=4,column=2,columnspan=3,sticky=W)

#create check boxes
CheckVar1 = IntVar()
CheckVar2 = IntVar()
c1=Checkbutton(master,text='Is there a job posted?',variable=CheckVar1).grid(row=1,columnspan=2,sticky=W)
c2=Checkbutton(master,text='Did you apply?',variable=CheckVar2).grid(row=2,columnspan=2,sticky=W)

#create text entry
appLink = StringVar()
textbox = Entry(master,textvariable=appLink,width=70).grid(row=3,column=1,sticky=W)


master.mainloop()