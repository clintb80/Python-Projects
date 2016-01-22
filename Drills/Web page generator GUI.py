from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import webbrowser

def generate():
    print (webdialog_entry.get())

def close_window():
    root.destroy()

def generate_html(event=None):
    f = open('helloworld.html','w')
    text=webdialog_entry.get()
    message = "<html><head></head><body>%s</body></html>"%text

    f.write(message)
    f.close()

    webbrowser.open_new_tab('helloworld.html')



root = Tk()
root.title("Webpage Generator")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))


#webdialog = StringVar()


webdialog_entry = ttk.Entry(mainframe, width=50)
webdialog_entry.grid(column=2, row=2, sticky=(W, E))


ttk.Button(mainframe, text="Generate", command=generate_html).grid(column=2, row=3)
ttk.Button(mainframe, text="Quit", command=close_window).grid(column=2, row=4)

ttk.Label(mainframe, text="Text for Web Page").grid(column=2, row=1, sticky=N)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)



root.bind('<Return>', generate_html)

root.geometry('320x150+400+200')
root.mainloop()
