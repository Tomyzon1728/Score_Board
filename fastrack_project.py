from tkinter import *
import sqlite3
from tkinter import messagebox
'''
please copy this code below and run it separate first before running the main code in order to create a table since its not in your pc already

import sqlite3
db = sqlite3.connect('SDC Participants.db')
c = db.cursor()
c.execute("""CREATE TABLE test_score (name text, score integer)""")
c.execute("""CREATE TABLE Participants (name text, score integer)""")
'''


def submit():
    db = sqlite3.connect('SDC Participants.db')
    c = db.cursor()
    c.execute("INSERT INTO Participants VALUES (:name, :score)",
              {'name': name.get(),
               'score': int(score.get())
               })

    db.commit()
    db.close()
    messagebox.showinfo("Success", "The Score has been added to the database")
    name.delete(0, END)
    score.delete(0, END)


def view():
    top = Toplevel()
    top.title('fastrack SDC Project')
    top.geometry('540x680')
    top.minsize(540, 680)
    top.maxsize(540, 680)
    bg = Label(top, bg='black', width=560, height=680)
    bg.place(x=0, y=0)
    head = LabelFrame(top, bg='white', width=540, height=50)
    head.place(x=60, y=10)
    title = Label(head, text='Standings', bg='navy blue', fg='orange', font=('courier', 12, 'bold'))
    title.pack()
    label = Label(top, text='Names\t\tScores', bg='black', fg='orange', font=('courier', 12, 'bold'))
    label.place(x=20, y=50)

    db = sqlite3.connect('SDC Participants.db')
    c = db.cursor()
    c.execute('SELECT * FROM Participants')
    results = c.fetchall()
    scores = {}
    for i in results:
        d = list(map(str, i))
        res = [int(i) for i in d if i.isdigit()] + [str(i) for i in d if not i.isdigit()]
        if res[-1] in scores:
            scores[res[-1]] += res[-2]
        else:
            scores[res[-1]] = res[-2]
    dif = 0
    scores = sorted(scores.items(), key=lambda num: num[1], reverse=True)
    for i, j in scores:
        label = Label(top, text='{0:14s} :{1:11d}'.format(i, j), bg='black', fg='White', font=('courier', 9, 'bold'))
        label.place(x=20, y=80 + dif)
        dif += 40

    for nm, sc in scores:
        f = LabelFrame(top, bg='navy blue', width=220, height=260)
        f.place(x=300, y=150)
        w = Label(f, text='Top Score', bg='navy blue', fg='red', font=('courier', 13, 'bold'))
        w.place(x=55, y=70)
        winner = Label(f, text='{0:5s}:{1:5d}/70'.format(nm, sc), bg='navy blue', fg='white', font=('courier', 12,))
        winner.place(x=8, y=130)
        bg = Label(f, text='Congratulations!', bg='navy blue', fg='Green', font=('courier', 13, 'bold'))
        bg.place(x=25, y=200)
        break
    db.commit()
    db.close()
    back_label = LabelFrame(top, width=80, height=10, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    back_label.place(x=375, y=450)
    Button(back_label, text='Back', fg='red', bg='navy blue', padx=10, font=('verdana', 9, 'bold'), relief='raised', command=lambda: top.destroy()).pack()


def start():
    win = Tk()
    win.title('fastrack SDC Project')
    win.geometry('440x520')
    win.minsize(440, 520)
    win.maxsize(440, 520)
    bg = Label(win, bg='black', width=440, height=560)
    bg.place(x=0, y=0)

    head = LabelFrame(win, bg='black', width=440, height=50)
    head.place(x=70, y=3)
    title = Label(head, text='fastrack Seven Days of Code', bg='navy blue', fg='orange', font=('courier', 11, 'bold'))
    title.pack()

    name_label = LabelFrame(win, width=80, height=50, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    name_label.place(x=113, y=100)
    Label(name_label, text='Name', bg='navy blue', fg='orange').pack()
    global name
    name = Entry(name_label, width=23, bg='white', fg='black', font=('courier', 10, 'bold'))
    name.pack()

    score_label = LabelFrame(win, width=80, height=50, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    score_label.place(x=113, y=200)
    Label(score_label, text='Score', bg='navy blue', fg='orange').pack()
    global score
    score = Entry(score_label, width=23, bg='white', fg='black', font=('courier', 10, 'bold'))
    score.pack()

    submit_label = LabelFrame(win, width=80, height=20, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    submit_label.place(x=173, y=280)
    Button(submit_label, text='Submit', fg='green', bg='navy blue', font=('courier', 10, 'bold'), command=submit).pack()

    view_label = LabelFrame(win, width=80, height=20, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    view_label.place(x=100, y=355)
    Button(view_label, text='View scores', fg='Orange', padx=10, bg='navy blue', font=('verdana', 10, 'bold'),relief='raised', command=view).pack()

    exit_label = LabelFrame(win, width=80, height=20, font=('courier', 12, 'bold'), bg='navy blue', fg='orange')
    exit_label.place(x=250, y=355)
    Button(exit_label, text='Exit', fg='red', bg='navy blue', padx=10, font=('verdana', 10, 'bold'), relief='raised', command=lambda: sys.exit()).pack()

    footer= LabelFrame(win,bg='orange',width=440, height=50)
    footer.place(x=0, y=470)
    win.mainloop()


start()
