import tkinter as tk

def load_teachers():
    print('Loading list of teachers...')
win = tk.Tk()
win.title("Розподіл навантаження")
win.geometry("700x600+100+30")

btn1 = tk.Button(win, text='Завантажити', command=load_teachers)
btn1.pack()

win.mainloop()