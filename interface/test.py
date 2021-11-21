import tkinter as tk
import middleware

def load_teachers():
    print('Loading list of teachers...')
win = tk.Tk()
win.title("Розподіл навантаження")
win.geometry("700x600+100+30")

# btn1 = tk.Button(win, text='Завантажити', command=load_teachers)
# btn1.pack()
teachers = middleware.get_all_teachers()
teachers_listbox = tk.Listbox(win)


for i in range(len(teachers)):
    teachers_listbox.insert(i, teachers[i])

teachers_listbox.pack()
win.mainloop()


