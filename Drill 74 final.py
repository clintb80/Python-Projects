from tkinter import *
from tkinter import ttk
import webbrowser
import sqlite3

w = Tk()
w.title("Webpage Generator")
w.geometry("750x450")

#Create database
conn = sqlite3.connect('webpage.db')
c = conn.cursor()
c.execute('create table if not exists webpage_content (body INT)')
conn.commit()
conn.close()

#Make the list box
list = Listbox(w, width=40)
list.grid(row=4, column=2)

a = StringVar()
body_data = []

#Uploads data to a database
def upload():

    body = a.get()
    conn = sqlite3.connect('webpage.db')

    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO webpage_content(body) VALUES(?)', (body,))
        conn.commit()
        
    conn.close()
    e.delete(0, 'end')

#Loads data into the list box
def load_data():
    global body_data
    cont = sqlite3.connect('webpage.db')

    with cont:
        cursort = cont.cursor()
        list_loadr = cursort.execute('SELECT * FROM webpage_content')
        list_load = list_loadr.fetchall()
        body_data = list_load
         
        for item in list_load:
            list.insert(END, " ".join(item))

    cont.close()

#Creates a webpage with selection from list box
def webpage():
    index = list.curselection()
    
    if index != ():
        f = open('helloworld.html','w')
    
        message = "<html><head></head><body>"+body_data[index[0]][0]+"</body></html>"
        
        f.write(message)
        f.close()

        webbrowser.open_new_tab('helloworld.html')

#Closes window
def close_window():
    w.destroy()

        
#Labels
l = Label(w, text="Enter Text for Web Page")
l.grid(column=0, row=0)

l = Label(w, text="Choose a Selection")
l.grid(row=3, column=2)

#Entry
e = Entry(w, width=40, textvariable = a)
e.grid(row=1,column=0, padx=(25,25))


#Buttons
b1 = Button(w, text="Upload", width=10, command=upload)
b1.grid(row=2, column=0, sticky=N)

b2 = Button(w, text="Load Data", width=10, command=load_data)
b2.grid(row=4, column=1, sticky=E)

b3 = Button(w, text="Generate Webpage", command=webpage)
b3.grid(row=5, column=2, sticky=W)
#w.bind('<Return>', webpage)

b4 = Button(w, text="Quit", width=10, command=close_window)
b4.grid(row=5, column=2, sticky=E)

#Padding around all buttons, labels, entries
for child in w.winfo_children(): child.grid_configure(padx=20, pady=5)



#w.bind('<Return>', webpage)


w.mainloop()
