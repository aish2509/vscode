from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("project name")

'''
headframe=Frame(root,bg="orange",highlightbackground='white',highlightthickness=1)
togglebutton=Button(head_frame,text="☰",bg='orange',fg='white',font=('Bold',20))
headframe.pack(side=TOP,fill=X)
headframe.pack_propagate(False)
headframe.configure(height=50)
'''
#create menus
my_menu=Menu(root)
root.config(menu=my_menu)

def allweb():
    pass
def amaz():
    pass
def flip():
    pass
def ebay():
    pass

filtermenu=Menu(my_menu)
my_menu.add_cascade(Label="Filter",menu=filtermenu)
filtermenu.add_command(Label="All Websites",command=allweb)
filtermenu.add_separator()
filtermenu.add_command(Label=" Amazon",command=amaz)
filtermenu.add_separator()
filtermenu.add_command(Label=" Flipkart",command=flip)
filtermenu.add_separator()
filtermenu.add_command(Label=" Ebay",command=ebay)

#create menuitem


# Create an icon
# icon = PhotoImage(file="path_to_your_icon_file.png")
# root.iconphoto(False, icon)

mylabel1 = Label(root, text="filter").grid(row=6, column=0)

# textbox
e = Entry(root, width=50)
e.grid(row=0, column=1)

# search button
def searchbutton():
    info = e.get()
    label1 = Label(root, text="santhosh job")
    label1.grid(row=1, column=0)

searchb = Button(root, text="search", command=searchbutton)
searchb.grid(row=0, column=2)

# dropdown menu
def dmshow():
    dmlabel = Label(root, text=clicked.get())
    dmlabel.pack()

clicked = StringVar()
options = ["Relevance",
           "price:High to Low",
           "price:Low to High",
           "AI powered rating",
           "Website Rating"]
clicked.set(options[0])



sort = OptionMenu(root, clicked, *options)
sort.grid(row=1, column=2)

dmsort = Button(root, text="show ", command=dmshow)
dmsort.grid(row=2, column=2)

l = Label(root, text="Sort")
l.grid(row=1, column=1)

# checkboxes

wvar = StringVar()

w = Checkbutton(root, text="All websites", variable=wvar, onvalue="url", offvalue="nothing")
w.deselect()
w.grid(row=7, column=0)

avar = IntVar()

a = Checkbutton(root, text="Amazon", variable=avar, onvalue="url", offvalue="nothing")
a.deselect()
a.grid(row=8, column=0)

fvar = IntVar()
f = Checkbutton(root, text="Flipkart", variable=fvar, onvalue="url", offvalue="nothing")
f.deselect()
f.grid(row=9, column=0)

ebvar = IntVar()
eb = Checkbutton(root, text="Ebay", variable=ebvar, onvalue="url", offvalue="nothing")
eb.deselect()
eb.grid(row=10, column=0)

def show():
    wlbl = Label(root, text=wvar.get())
    wlbl.grid(row=12, column=0)

wbutton = Button(root, text="Show selection", command=show)
wbutton.grid(row=11, column=0)

root.mainloop()
