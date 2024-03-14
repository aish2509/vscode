from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('600x400')
root.title('SmartChoice AI')

optionsframe=Frame(root)#,bg="orchid2")





#menus

my_menu = Menu(root)
my_menu.configure(bg='skyblue')
root.config(menu=my_menu)



'''
def pref():
    pass'''

helpmenu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=helpmenu)

'''premenu.add_command(label="Preferences", command=pref)
premenu.add_separator()'''
def helpfunc():
    pass
#e = Entry(mainframe,bd=0)
#e.place(x=170,y=58))
helpmenu.add_command(label="send your queries at connectwithsanthoshmk@gmail.com or aishwaryaadalin687@gmail.com",command=helpfunc)
helpmenu.add_separator()

optionsframe.pack(side=LEFT)
optionsframe.pack_propagate(False)
optionsframe.configure(width=120,height=400,bg='bisque')#150,1000

mainframe=Frame(root,highlightbackground='black',highlightthickness=2)

mainframe.pack(side=LEFT)
mainframe.pack_propagate(False)
mainframe.configure(height=400,width=500)#1000,1000



#Heading
hl=Label(mainframe,text="SmartChoice AI",font=('bold',18),fg='coral1',bg='bisque')
hl.place(x=150,y=10)

#labeltext
l=Label(mainframe,text="Enter the product name:",font=('bold',13))
l.place(x=10,y=80)
#textbox
e = Entry(mainframe,bd=0)
e.place(x=194,y=86)

#searchbutton
def searchbutton():
    info = e.get()
    label1 = Label(mainframe, text="santhosh job")
    label1.place(x=150, y=200)

searchb = Button(mainframe, text="search",font=('Bold',10),bg='#c3c3c3', bd=5,command=searchbutton)
searchb.place(x=150, y=160)


#aisuggestion
def aisuggest():
    messagebox.showinfo('AI suggestion','helloworld')
aibutton=Button(optionsframe,text="AI suggestion",bg='sky blue',command=aisuggest)
aibutton.place(x=10,y=300)

#specificationsbutton
def specifications():
    slabel=Label(mainframe,text="specifications")
    slabel.place(x=280, y=200)
specib = Button(mainframe, text="specifications",font=('Bold',10),bg='#c3c3c3', bd=5,command=specifications)
specib.place(x=250, y=160)

#droppedmenu
def dmshow():
    dmlabel = Label(optionsframe, text=clicked.get())
    dmlabel.place()

clicked = StringVar()
options = ["Relevance",
           "price:High to Low",
           "price:Low to High",
           "AI powered rating",
           "Website Rating"]
clicked.set(options[0])

l = Label(optionsframe, text="Sort",padx=10,bg='sky blue')
l.place(x=10,y=50)

sort = OptionMenu(optionsframe,clicked, *options, command=dmshow)
sort.place(x=10, y=80)

#checkboxes

lbl=Label(optionsframe,text="Filter",bg='sky blue')
lbl.place(x=10,y=140)

wvar = StringVar()

w = Checkbutton(optionsframe, text="All websites",bg='sky blue', variable=wvar, onvalue="url", offvalue="nothing")
w.deselect()
w.place(x=10, y=160)

avar = IntVar()

a = Checkbutton(optionsframe, text="Amazon",bg='sky blue', variable=avar, onvalue="url", offvalue="nothing")
a.deselect()
a.place(x=10, y=180)

fvar = IntVar()
f = Checkbutton(optionsframe, text="Flipkart",bg='sky blue', variable=fvar, onvalue="url", offvalue="nothing")
f.deselect()
f.place(x=10, y=200)


def wshow():
    wlbl = Label(optionsframe, text=wvar.get())
    wlbl.place(x=10, y=260)


def ashow():
    albl = Label(optionsframe, text=avar.get())
    albl.place(x=10,y=260)



def fshow():
    flbl = Label(optionsframe, text=fvar.get())
    flbl.place(x=10,y=260)   


def run_all():
    wvar.set()
    avar.set()
    fvar.set()
    wshow()
    ashow()
    fshow()
    optionsframe.destroy()
wbutton = Button(optionsframe, text="Show selection", command=run_all,bg='sky blue')
wbutton.place(x=10, y=240)

    

root.mainloop()

