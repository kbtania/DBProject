import tkinter as tk
import middleware

def load_teachers():
    print('Loading list of teachers...')
win = tk.Tk()
win.title("Розподіл навантаження")
win.geometry("700x600+100+30")

teachers = middleware.get_all_teachers()
subjects1 = middleware.get_all_subjects1()
subjects2 = middleware.get_all_subjects2()



l1 = tk.Label(win, text='Оберіть викладача')
l1.place(relx=0.2, rely=0.2, anchor='sw')


teachers_listbox = tk.Listbox(win, width=50, height=20)
for i in range(len(teachers)):
    teachers_listbox.insert(i, teachers[i])

teachers_listbox.pack()

teachers_listbox.place(relx=0.1, rely=0.75, anchor='sw')

subjects1_listbox = tk.Listbox(win, width=50, height=20)
for i in range(len(subjects1)):
    subjects1_listbox.insert(i, subjects1[i])

subjects1_listbox.pack()

subjects1_listbox.place(relx=0.6, rely=0.75, anchor='sw')


OptionList = [
"1",
"2"
]
variable = tk.StringVar(win)
variable.set(OptionList[0])

def callback(selection):

    if variable.get() == '2':
        subjects1_listbox = tk.Listbox(win, width=50, height=20)
        for i in range(len(subjects2)):
            subjects1_listbox.insert(i, subjects2[i])

        subjects1_listbox.pack()

        subjects1_listbox.place(relx=0.6, rely=0.75, anchor='sw')

    print(variable.get())


opt = tk.OptionMenu(win, variable, *OptionList, command=callback)
opt.config(width=6)

opt.pack()
opt.place(relx=0.5, rely=0.15, anchor='sw')



l2 = tk.Label(win, text='Оберіть семестр')
l2.place(relx=0.5, rely=0.1, anchor='sw')

l3 = tk.Label(win, text='Оберіть предмет')
l3.place(relx=0.7, rely=0.2, anchor='sw')
win.mainloop()


