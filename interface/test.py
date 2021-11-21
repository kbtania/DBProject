import tkinter as tk
import middleware


win = tk.Tk()
win.title("Розподіл навантаження")
win.geometry("700x600+100+30")
win.minsize(750, 600)

# ----- Data area -----
teachers = middleware.get_all_teachers()
subjects1 = middleware.get_all_subjects1()  # list of subjects for semester 1
subjects2 = middleware.get_all_subjects2()  # list of subjects for semester 2

# ----- Labels area -----
l1 = tk.Label(win, text='Оберіть викладача')
l1.place(relx=0.2, rely=0.2, anchor='sw')

l2 = tk.Label(win, text='Оберіть семестр')
l2.place(relx=0.5, rely=0.1, anchor='sw')

l3 = tk.Label(win, text='Оберіть предмет')
l3.place(relx=0.7, rely=0.2, anchor='sw')

# ----- Listbox area -----
# Listbox with teachers
teachers_listbox = tk.Listbox(win, width=35, height=20, font=12, exportselection=0)
for i in range(len(teachers)):
    teachers_listbox.insert(i, teachers[i])
teachers_listbox.pack()
teachers_listbox.place(relx=0.1, rely=0.85, anchor='sw')

# Listbox wit subjects1 (by default)
subjects1_listbox = tk.Listbox(win, width=45, height=20, font=12, exportselection=0)
for i in range(len(subjects1)):
    subjects1_listbox.insert(i, subjects1[i])
subjects1_listbox.pack()
subjects1_listbox.place(relx=0.6, rely=0.85, anchor='sw')

# ----- Option Menu area -----
option_list = ['1', '2']
variable = tk.StringVar(win)
variable.set(option_list[0])


def on_change_optionMenu(selection):  # detects when optionMenu is changed
    if variable.get() == '1':
        for i in range(len(subjects1)):
            subjects1_listbox.insert(i, subjects1[i])
    if variable.get() == '2':
        for i in range(len(subjects2)):
            subjects1_listbox.insert(i, subjects2[i])


opt = tk.OptionMenu(win, variable, *option_list, command=on_change_optionMenu)
opt.config(width=6)
opt.pack()
opt.place(relx=0.5, rely=0.15, anchor='sw')

# ----- Button area -----


def selected_item():  # just for testing purpose
    for i in teachers_listbox.curselection():
        print(teachers_listbox.get(i))
    for i in subjects1_listbox.curselection():
        print(subjects1_listbox.get(i))


btn1 = tk.Button(win, text='Вибрати', command=selected_item)
btn1.pack()
btn1.place(relx=0.5, rely=0.9)


win.mainloop()
