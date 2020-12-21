from tkinter import *

# function


def click(event):
    global scval
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scval.get().isdigit():
            val=int(scval.get())
        else:
            val=eval(screen.get())

        scval.set(val)
        screen.update()


    elif text == "C":
        scval.set('')
        screen.update()

    else:
        scval.set(scval.get()+text)
        screen.update()


root = Tk()

root.geometry('644x700')
root.title('Calculator By Basavaraj')

root.wm_iconbitmap('calc.ico')

scval = StringVar()
scval.set('')

screen = Entry(root, textvariable=scval, font='Arial 30 bold',relief=SUNKEN,bg='white')
screen.pack(fill=X, padx=10, pady=10, ipadx=10, ipady=5)

# frame


for i in range(9, 0, -3):
    f1 = Frame(root, bg='gray')
    b = Button(f1, text=f'{i}', padx=20, font='Arial 25 bold')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind('<Button-1>', click)

    b = Button(f1, text=f'{i-1}', padx=20, font='Arial 25 bold')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind('<Button-1>', click)

    b = Button(f1, text=f'{i-2}', padx=20, font='Arial 25 bold')
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind('<Button-1>', click)
    f1.pack()

f1 = Frame(root, bg='gray')
b = Button(f1, text='0', padx=20, font='Arial 25 bold')
b.pack(side=LEFT, padx=11, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text='+', padx=18, font='Arial 25 bold')
b.pack(side=LEFT, padx=11, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text='-', padx=22, font='Arial 25 bold')
b.pack(side=LEFT, padx=11, pady=10)
b.bind('<Button-1>', click)
f1.pack()

f1 = Frame(root, bg='gray')
b = Button(f1, text='*', padx=21, font='Arial 25 bold')
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text='/', padx=20, font='Arial 25 bold')
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text='=', padx=18, font='Arial 25 bold')
b.pack(side=LEFT, padx=13, pady=10)
b.bind('<Button-1>', click)
f1.pack()

f1 = Frame(root, bg='gray')
b = Button(f1, text=f'%', padx=18, font='Arial 25 bold')
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text=f'C', padx=18, font='Arial 25 bold')
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)

b = Button(f1, text=f'', padx=20, font='Arial 25 bold')
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)
f1.pack()


root.mainloop()
