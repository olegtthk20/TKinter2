from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput

def funktion(a):
    tabs.select(a)

def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0_0,text)

def save_():
    file=asksaveasfile(mode='w' ,deafultextension=(('.txt'),('.docx')),filetypes=(('Notepad','.txt'),('Word','.docx')))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno('Exit','Yes/No'):
        showinfo('Exit','Message:Yes')
        root.destroy()
    else:
        showinfo('No')

def image_illuminat(name):
    global img
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)

root=Tk()
root.geometry('400x300')
root.title('elemendid Tkineris')
tabs=ttk.Notebook(root)
texts=['Esimene','Teine','Kolmas','Neljas','Viies','Kuues','Seitsmes','Kaheksas']

tabs.pack()

M=Menu(root)
root.config(menu=M)

m1=Menu(M,tearoff=0)
M.add_cascade(label='Image',menu=m1)
m1.add_command(label='Tab1', accelerator='command+V',command=lambda:funktion(0))
m1.add.separator()
m1.add_command(label='Tab2',command=lambda:funktion(1))
m1.add_command(label='Tab3',command=lambda:funktion(2))
m1.add_command(label='Tab4',command=lambda:funktion(3))

m2=Menu(M,tearoff=0)
M.add_cascade(label='BG Colors',menu=m1)
m2.add_command(label='Purple',command=lambda:root.config(bg='purple'))
m2.add_command(label='White',command=lambda:root.config(bg='white'))
m2.add_command(label='Black',command=lambda:root.config(bg='black'))
m2.add_command(label='Blue',command=lambda:root.config(bg='blue'))

m3=Menu(M,tearoff=0)
M.add_cascade(label='Image',menu=m3)
m3.add_command(label='')
m3.add_command(label='')
m3.add_command(label='')
m3.add_command(label='')

btn_open=Button(tab1,text='Open')
btn_open=Button(tab1,text='Open')
btn_open=Button(tab1,text='Open')
txt_box=scrolledtext.ScrolledText(tab1, width=40,height=5)
txt_box.grid(row=0,column=0,columspan=3)
btn_open.gtid(row=1,column=0)
btn_open.gtid(row=1,column=1)
btn_open.gtid(row=1,column=2)

can=Canvas(tab2,width='300', height='200')
img=PhotoImage(file='DichTok.png')
can.create_image(10,10,image=img,anchor=NW)
can.pack()
root.mainloop()
