from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('600x400')
root.title('project name')

optionsframe=Frame(root,bg="orchid2")





optionsframe.pack(side=LEFT)
optionsframe.pack_propagate(False)
optionsframe.configure(width=120,height=400)#150,1000

mainframe=Frame(root,highlightbackground='black',highlightthickness=2)

mainframe.pack(side=LEFT)
mainframe.pack_propagate(False)
mainframe.configure(height=400,width=500)#1000,1000



#Heading
hl=Label(mainframe,text="title",font=('bold',15))
hl.place(x=150,y=20)

#labeltext
l=Label(mainframe,text="Enter the product name:",font=('bold',10))
l.place(x=10,y=50)
#textbox
e = Entry(mainframe,bd=0)
e.place(x=260,y=58)

#searchbutton
def searchbutton():
    info = e.get()
    label1 = Label(mainframe, text="santhosh job")
    label1.place(x=150, y=150)

searchb = Button(mainframe, text="search",font=('Bold',10),bg='#c3c3c3', bd=5,command=searchbutton)
searchb.place(x=150, y=100)


#aisuggestion
def aisuggest():
    messagebox.showinfo('AI suggestion','helloworld')
aibutton=Button(optionsframe,text="AI suggestion",command=aisuggest)
aibutton.place(x=10,y=300)
#specificationsbutton
def specifications():
    slabel=Label(mainframe,text="specifications")
    slabel.place(x=280, y=150)
specib = Button(mainframe, text="specifications",font=('Bold',10),bg='#c3c3c3', bd=5,command=specifications)
specib.place(x=250, y=100)

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

l = Label(optionsframe, text="Sort",padx=10)
l.place(x=10,y=50)

sort = OptionMenu(optionsframe,clicked, *options, command=dmshow)
sort.place(x=10, y=80)

#checkboxes

lbl=Label(optionsframe,text="Filter")
lbl.place(x=10,y=140)

wvar = StringVar()

w = Checkbutton(optionsframe, text="All websites", variable=wvar, onvalue="url", offvalue="nothing")
w.deselect()
w.place(x=10, y=160)

avar = IntVar()

a = Checkbutton(optionsframe, text="Amazon", variable=avar, onvalue="url", offvalue="nothing")
a.deselect()
a.place(x=10, y=180)

fvar = IntVar()
f = Checkbutton(optionsframe, text="Flipkart", variable=fvar, onvalue="url", offvalue="nothing")
f.deselect()
f.place(x=10, y=200)

'''ebvar = IntVar()
eb = Checkbutton(optionsframe, text="Ebay", variable=ebvar, onvalue="url", offvalue="nothing")
eb.deselect()
eb.grid(row=10, column=0)'''

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
wbutton = Button(optionsframe, text="Show selection", command=run_all)
wbutton.place(x=10, y=240)

    

root.mainloop()

