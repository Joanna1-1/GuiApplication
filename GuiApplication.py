from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Joanna's Lab2")	   #title of the window

frame = ttk.Frame(                         #create a Frame (container in this case)
  window,                                  #parent of this widget
  width=450,                               #width
  height=360)                              #height

frame.grid()                               #row=0, column=0

frame['padding'] = (5,10)                  
frame['borderwidth'] = 10                  
frame['relief'] = 'sunken'                 


#row 0
lbl_feather = ttk.Label(frame)         #the parent of this widget
image = PhotoImage(file='feather.png') #create a PhotoImage
lbl_feather['image'] = image           #put the above image on label
lbl_feather.grid(                      #positionsing the label
  column=1,                            #column=1
  row=0,                               #row=0
  sticky=(W, E))                       #where to anchor in the cell

#row 1
lblFullName = ttk.Label(              #creates a Label
  frame,                              #parent
  text='Full name:').grid(            #sets the text
  column=0,                           #column=0
  row=1,                              #row=1
  sticky=(W, E))                      #align center

fullname = StringVar()                #variable for full name

txtFullName = ttk.Entry(              #creates an Entry
  frame,                              
  textvariable=fullname).grid(        #the variable to bind to
  column=1,                           #column=1
  row=1,                              #row=1
  sticky=(W))                         #align left

#row 2
ttk.Label( frame, text='Residency:').grid( column=0, row=2, sticky=(W, E))

panel = ttk.Frame(frame)            #this will be the container for the two radion buttons
panel.grid(column=1, row=2, sticky=(W, E))
panel['borderwidth'] = 3
panel['relief'] = 'ridge'

residency = StringVar()

ttk.Radiobutton(panel, text='Domestic', variable=residency, value='dom').grid(
  column=0, row=0, sticky=(W))      
ttk.Radiobutton(panel, text='International', variable=residency, value='intl').grid(
  column=0, row=1, sticky=(W))

#row 3
ttk.Label( frame, text='Program:').grid( column=0, row=3, sticky=(W, E))

panel = ttk.Frame(frame)            #this will be the container for the combobox
panel.grid(column=1, row=3, sticky=(W, E))

program = StringVar()

ttk.Combobox(panel,  textvariable=program, values=["Graming","Health","Software"]).grid(
  column=0, row=0, sticky=(W))     

#row 4
ttk.Label( frame, text='Courses:').grid( column=0, row=4, sticky=(W, E))

panel = ttk.Frame(frame)			 #this will be the container for the three checkbuttoms
panel.grid( column=1, row=4, columnspan=4, sticky=(W, E))
panel['borderwidth'] = 3
panel['relief'] = 'ridge'

comp100 = StringVar()
comp213 = StringVar()
comp120 = StringVar()


ttk.Checkbutton( panel, text='Programming I',
  variable=comp100, onvalue='comp100').grid( 
  column=0, row=0, sticky=(W))

ttk.Checkbutton( panel, text='Web Page Design',
  variable=comp213, onvalue='comp213').grid( 
  column=0, row=1, sticky=(W))

ttk.Checkbutton( panel, text='Software Engineering Fundamentals', 
  variable=comp120, onvalue='comp129').grid( 
  column=0, row=2, sticky=(W)) 

#row 5
def exited():
    window.destroy()

def resetted():
	fullname.set("");
	residency.set("dom")
	program.set("Gaming")
	comp100.set(False);
	comp120.set(False);
	comp213.set(False);

def read_form(*args):
  messagebox.showinfo(                            
    title='Form Information', 
    message=f'Username: {fullname.get()} \nResidency: {residency.get()}\nCourses: {comp100.get()} {comp120.get()} {comp213.get()}\nProgram: {program.get()}')

btnReset = Button(frame, text="Reset", command=resetted)
btnReset.grid(column=0, row=5, sticky=(W, E))

btnOk = Button(frame, text="Ok", command=read_form)
btnOk.grid(column=1, row=5)

btnExit = Button(frame, text="Exit", command=exited )
btnExit.grid(column=2, row=5)

window.mainloop()