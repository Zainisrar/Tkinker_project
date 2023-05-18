import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
window=tk.Tk()
window.title("Application")
# create labels
# for name
labels_name=ttk.Label(window,text="Enter your Name :")
labels_name.grid(row=0,column=0,sticky=tk.W)
# for age 
labels_age=ttk.Label(window,text="Enter your Age :")
labels_age.grid(row=1,column=0,sticky=tk.W)        
# for Email
labels_email=ttk.Label(window,text="Enter your Email :")
labels_email.grid(row=2,column=0,sticky=tk.W)  
# for selection of gender
labels_email=ttk.Label(window,text="Select your Gender :")
labels_email.grid(row=3,column=0,sticky=tk.W) 
# Text entry box name
var_name=tk.StringVar()
entry_name=ttk.Entry(window,width=16,textvariable=var_name)
entry_name.grid(row=0,column=1)  
entry_name.focus()#cursor automatically start in box
# Text entry box age
var_age=tk.StringVar()
entry_age=ttk.Entry(window,width=16,textvariable=var_age)
entry_age.grid(row=1,column=1)  
# Text entry box Email
var_email=tk.StringVar()
entry_email=ttk.Entry(window,width=16,textvariable=var_email)
entry_email.grid(row=2,column=1) 
# combobox creation
var_gender=tk.StringVar()
combobox_gender=ttk.Combobox(window,width=13,state='readonly',textvariable=var_gender)
combobox_gender['values']=('Male','Female','Others')
combobox_gender.grid(row=3,column=1) 
combobox_gender.current(0)#0 index data will be show
#Radio botton
user_type=tk.StringVar()
radio_student=ttk.Radiobutton(window,value='Student',text='Student',variable=user_type)
radio_student.grid(row=5,column=0) 

radio_teacher=ttk.Radiobutton(window,value='Teacher',text='Teacher',variable=user_type)
radio_teacher.grid(row=5,column=1)
#cheak botton
var_user_type_cheak=tk.IntVar()
cheak_button=ttk.Checkbutton(window,text='Are you Accept our privacy',variable=var_user_type_cheak)
cheak_button.grid(row=6,columnspan=3,sticky=tk.W) 
# create button
# ==========for normal text file===================
# def action():
#     user_name=entry_name.get()
#     user_age=entry_age.get()
#     user_email=entry_email.get()
#     user_gender=combobox_gender.get()
#     user_types=user_type.get()
#     if var_user_type_cheak.get()==0:
#         accept="No"
#     else:
#         accept="yes"
#     print(f"{user_name},{user_age},{user_email},{user_gender},{user_types},{accept}")
#     with open(r"app tkinter\appdata.txt",'a') as f:
#         f.write(f"{user_name},{user_age},{user_email},{user_gender},{user_types},{accept}\n")
#     entry_name.delete(0,tk.END)
#     entry_age.delete(0,tk.END)
#     entry_email.delete(0,tk.END)
#     # labels_name.configure(foreground='red')
#     submit_button.configure(foreground='red')
# ==================for csv files=================
def action():
    user_name=entry_name.get()
    user_age=entry_age.get()
    user_email=entry_email.get()
    user_gender=combobox_gender.get()
    user_types=user_type.get()
    if var_user_type_cheak.get()==0:
        accept="No"
    else:
        accept="yes"
    with open(r"app tkinter\apppdata.csv",'a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['User_name','User_Age','User_Email','User_Gender','User_Type','Subcribe'])
        if os.stat(r"app tkinter\apppdata.csv").st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User_name':user_name,
            'User_Age':user_age,
            'User_Email':user_email,
            'User_Gender':user_gender,
            'User_Type':user_types,
            'Subcribe':accept
            })
    entry_name.delete(0,tk.END)      
    entry_age.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    # labels_name.configure(foreground='red')
    submit_button.configure(foreground='red')
submit_button=tk.Button(window,text="Submit",command=action)
submit_button.grid(row=7,column=0)















window.mainloop()