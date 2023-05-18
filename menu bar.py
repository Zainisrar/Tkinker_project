import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title('Menu')
# *********************Simple Menu***************************
#menu
# menubar=tk.Menu(window)
# def fuc():
#     pass
# menubar.add_command(label='File',command=fuc)
# menubar.add_command(label='Edit',command=fuc)
# menubar.add_command(label='Selection',command=fuc)
# menubar.add_command(label='View',command=fuc)
# menubar.add_command(label='Go',command=fuc)
# menubar.add_command(label='Run',command=fuc)
# menubar.add_command(label='Terminal',command=fuc)
# menubar.add_command(label='Help',command=fuc)
# menubar.add_command(label='Setting',command=fuc)
# *********************Main Menu***************************
# file menu
def fuc():
    pass
main_menubar=tk.Menu(window)
file_menu=tk.Menu(main_menubar,tearoff=0)
file_menu.add_command(label='Edit',command=fuc)
file_menu.add_command(label='Selection',command=fuc)
file_menu.add_command(label='View',command=fuc)
file_menu.add_separator()
file_menu.add_command(label='Go',command=fuc)
file_menu.add_command(label='Run',command=fuc)
file_menu.add_separator()
file_menu.add_command(label='Terminal',command=fuc)
file_menu.add_command(label='Help',command=fuc)
#Edit menu
edit_menu=tk.Menu(main_menubar,tearoff=0)
edit_menu.add_command(label='Edit',command=fuc)
edit_menu.add_command(label='Selection',command=fuc)
edit_menu.add_separator()
edit_menu.add_command(label='View',command=fuc)
edit_menu.add_command(label='Go',command=fuc)
edit_menu.add_separator()
edit_menu.add_command(label='Run',command=fuc)
edit_menu.add_command(label='Terminal',command=fuc)
edit_menu.add_separator()
edit_menu.add_command(label='Help',command=fuc)
main_menubar.add_cascade(label='File',menu=file_menu)
main_menubar.add_cascade(label='Edit',menu=edit_menu)
window.config(menu=main_menubar)
window.mainloop()