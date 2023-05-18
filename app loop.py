import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("loop")

# label draw using loop
labels=['Name :','Fname :','Age :','City :','Country :','Education']
for i in range(len(labels)):
    Cur_Label=ttk.Label(window,text=labels[i])
    Cur_Label.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)

#entry text draw using loop
user_info={
    'Name':tk.StringVar(),
    'Fname':tk.StringVar(),
    'Age':tk.StringVar(),
    'City':tk.StringVar(),
    'Country':tk.StringVar(),
    'Education':tk.StringVar()
}
counter=0
for i in user_info:
    Cur_entry='entry'+i
    Cur_entry=ttk.Entry(window,width=16,textvariable=user_info[i])
    Cur_entry.grid(column=1,row=counter)
    counter=counter+1
#Button 
def action():
    print(user_info.get("Name").get())
    print(user_info.get("Fname").get())
    print(user_info.get("Age").get())
    print(user_info.get("City").get())
    print(user_info.get("Country").get())
    print(user_info.get("Education").get())
app_button=ttk.Button(window,text="Submit",command=action)
app_button.grid(row=6,columnspan=2,padx=2,pady=2)
window.mainloop()