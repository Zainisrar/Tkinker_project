import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from csv import DictWriter
import os
window=tk.Tk()
#label frame
label_frame=ttk.LabelFrame(window,text='Contact Detail')
label_frame.grid(row=0,column=0,padx=40,pady=20)
#entry box variable
name_var=tk.StringVar()
age_var=tk.StringVar()
var_gender=tk.StringVar()
#labels
labels_name=ttk.Label(label_frame,text="Enter your Name :")
labels_age=ttk.Label(label_frame,text="Enter your Age :")
combobox_gender=ttk.Combobox(label_frame,width=13,state='readonly',textvariable=var_gender)
#entry boxes
name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=36,textvariable=age_var)
combobox_gender['values']=('Male','Female','Others')
#Grid
labels_name.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
labels_age.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)
combobox_gender.grid(row=3,column=0,padx=0,pady=0,sticky=tk.W) 
combobox_gender.current(0)
#Button
def submit():
    # mb.showerror('title','Content of this message Box!!!')
    # mb.showwarning('title','Content of this message Box!!!')
    # mb.showinfo('title','Content of this message Box!!!')
    name=name_var.get()
    age=age_var.get()
    user_gender=combobox_gender.get()
    def filling():
        with open(r"data.csv",'a',newline='') as f:
            dict_writer=DictWriter(f,fieldnames=['User_name','User_Age','gender'])
            if os.stat(r"data.csv").st_size==0:
                dict_writer.writeheader()
            dict_writer.writerow({
                    'User_name':name,
                    'User_Age':age,
                    'gender':user_gender
                })
        name_entry.delete(0,tk.END)      
        age_entry.delete(0,tk.END)
    if name=='' or age=='':
        mb.showerror('error','Name and Age must be Enter')
    else:
        try:
            age=int(age)
        except ValueError:
            mb.showerror('error','Age must be Digits')
        else:
            if age<18:
                mb.showwarning('warning','This app is 18+.If you visit this app its your own risk')
            else:
                filling()
                
           


submit_button=ttk.Button(window,text='Submit',command=submit)
submit_button.grid(row=1,columnspan=2,padx=40)



window.mainloop()