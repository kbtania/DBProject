import tkinter as tk
import middleware

def load_teachers():
    print('Loading list of teachers...')
win = tk.Tk()
win.title("Розподіл навантаження")
win.geometry("700x600+100+30")

teachers = middleware.get_all_teachers()



l1 = tk.Label(win, text='Оберіть викладача')
l1.place(relx=0.2, rely=0.2, anchor='sw')


teachers_listbox = tk.Listbox(win, width=50, height=20)
for i in range(len(teachers)):
    teachers_listbox.insert(i, teachers[i])

teachers_listbox.pack()

teachers_listbox.place(relx=0.1, rely=0.75, anchor='sw')

win.mainloop()


