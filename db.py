import sqlite3
from tkinter import *
import time
import datetime
    
def read_data(event):
    d = ent3.get()
    cur.execute('SELECT * FROM members WHERE name=? OR name=?',(d, d) )
    data = cur.fetchall()
    for row in data:
        txt.config(state=NORMAL)
        txt.insert(INSERT, str(data) + '\n')
        txt.config(state=DISABLED)
    
    

def data_entry():
    cur.execute('CREATE TABLE IF NOT EXISTS Members(date TEXT, number NUMERICAL, name TEXT, age NUMERICAL)')
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    n = ent.get()
    ne = ent1.get()
    ag = ent2.get()
    cur.execute("INSERT INTO members (date, number, name, age) VALUES (?, ?, ?, ?)",
               (date, n, ne, ag))
    con.commit()
    
    
    
def add():
    global ent, ent1, ent2
    root2 = Tk()
    root2.title("Editeur de base de données v1.0")

    root.destroy()

    lbl = Label(root2, text="ID : ")
    lbl.place(x=10, y=10)
    ent = Entry(root2, width=40)
    ent.place(x=60, y=10)

    lbl1 = Label(root2, text="Name : ")
    lbl1.place(x=10, y=50)
    ent1 = Entry(root2, width=40)
    ent1.place(x=60, y=50)

    lbl2 = Label(root2, text="Age : ")
    lbl2.place(x=10, y=90)
    ent2 = Entry(root2, width=40)
    ent2.place(x=60, y=90)

    btn = Button(root2, text="Ajouter", width=34, command=data_entry)
    btn.place(x=60, y=130)

    btn1 = Button(root2, text="Exit", width=34, command=quit)
    btn1.place(x=60, y=170)

    root2.geometry("350x210")
    root2.mainloop()

def read():
    global txt, ent3
    root1 = Tk()
    root1.title("Editeur de base de données v1.0")

    root.destroy()

    lbl = Label(root1, text="Name : ")
    lbl.place(x=10, y=10)
    ent3 = Entry(root1, width=46)
    ent3.bind("<Return>",read_data)
    ent3.place(x=60, y=10)

    txt = Text(root1, width=50)
    txt.place(y=50)
    txt.config(state=NORMAL)
    txt.insert(INSERT, str("Date                     ID  Name     Age") + '\n')
    txt.config(state=DISABLED)

    root1.geometry("400x300")
    root1.mainloop()

def make_connection():
    global cur, con
    try:
        con = sqlite3.connect('amine.db')
        cur = con.cursor()
        btn1.config(state=NORMAL)
        btn2.config(state=NORMAL)
        label.config(text="Connecté")
    except:
        label.config(text="Erreur...")
    
def main():
    global root, btn1, btn2, label
    root = Tk()
    root.title("Editeur de base de données v1.0")

    btn = Button(root, text="Connéctez", command=make_connection, width=20)
    btn.place(x=10, y=30)

    btn1 = Button(root, text="Récuperez", width=20, command=read, state=DISABLED)
    btn1.place(x=10, y=80)

    btn2 = Button(root, text="Ajoutez", width=20, command=add, state=DISABLED)
    btn2.place(x=10, y=130)

    label = Label(root, text="")
    label.place(x=10, y=170)
    
    root.geometry("200x200")
    root.mainloop()
    
main() 
