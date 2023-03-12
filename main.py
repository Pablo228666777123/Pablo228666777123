from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

dollar = 0
cent = 0
add = 1

def click():
    global dollar, cent, add
    cent += add
    counter['text'] = f'Your money: {dollar}.{cent}'
    if cent >= 100:
        cent -= 100
        dollar += 1
        counter['text'] = f'Your money: {dollar}.{cent}'
    if dollar >= 5000:
        messagebox.showinfo('Information', 'You have done the limit (4999 dollars)')
        add = 1

def upgrade():
    global dollar, cent, add
    if cent >= 10:
        add += 1
        cent -= 10
        counter['text'] = f'Your money: {dollar}.{cent}'
    elif dollar >= 1:
        dollar -= 1
        cent += 90
        counter['text'] = f'Your money: {dollar}.{cent}'
    else:
        messagebox.showerror('Error', "You haven't got any money")
    if add >= 100:
        messagebox.showinfo('Information', 'You have done the limit (99 upgrades)')
        add = 1

def reset():
    global dollar, cent, add
    messagebox.showwarning('Warning', "Your money is don't saved and your upgrades")
    dollar = 0
    cent = 0
    add = 1
    counter['text'] = f'Your money: {dollar}.{cent}'

def quit_program():
    yesno = messagebox.askyesnocancel('Quit', "Do yo want to quit?")
    if yesno:
        exit()

root = Tk()

root.title('Clicker')
root.geometry('500x800')
root.resizable(False, False)
root.iconbitmap("cursor.ico")
root['bg'] = '#a8dadc'

Climate_crisis = Font(family='Climate Crisis', size=15, weight='bold')
counter = Label(root, text=f'Your money: {dollar}.{cent}', font=Climate_crisis, bg='#a8dadc', fg='#fff')
counter.place(x=180, y=10)

Button(root, text='Click', width=30, height=5, font=Climate_crisis, command=click, relief=FLAT, bg='#61c9a8', activebackground='#72a596', fg='#fff', activeforeground='#fff').place(x=70, y=80)
Button(root, text='Upgrade Click + 1 (10 cents)', width=30, height=5, font=Climate_crisis, command=upgrade, relief=FLAT, bg='#fca311', activebackground='#fcbf49', fg='#fff', activeforeground='#fff').place(x=70, y=230)
Button(root, text='Reset', width=30, height=5, font=Climate_crisis, command=reset, relief=FLAT, bg='#0096c7', activebackground='#48cae4', fg='#fff', activeforeground='#fff').place(x=70, y=380)
Button(root, text='Quit', width=30, height=5, font=Climate_crisis, command=quit_program, relief=FLAT, bg='#dc493a', activebackground='#e29d9d', fg='#fff', activeforeground='#fff').place(x=70, y=530)

root.mainloop()