import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import main
from main import path
import webbrowser

root = Tk()
root.geometry('600x670')
root.resizable(False, False)
root.title('ERC Daily Report')
root.configure(bg='white')

image = Image.open(path('data/ERCLogo.png'))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.config(background='white')
image_label.pack()


# Labels
lab1 = Label(root, text='عدد القادة')
lab1.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab1.config(fg="black")
lab1.config(background='white')
lab1.place(relx = 1, x =-2, y = 100, anchor = NE)

lab2 = Label(root, text='عدد المتطوعين')
lab2.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab2.config(fg="black")
lab2.config(background='white')
lab2.place(relx = 1, x =-170, y = 100, anchor = NE)

lab3 = Label(root, text='عدد ساعات العمل')
lab3.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab3.config(fg="black")
lab3.config(background='white')
lab3.place(relx = 1, x =-370, y = 100, anchor = NE)

line1 = Image.open(path('data/red line.png'))
line1 = ImageTk.PhotoImage(line1)
line1_label = tk.Label(root, image=line1)
line1_label.config(background='white')
line1_label.place(x = 300, y = 145, anchor = CENTER)

lab4 = Label(root, text='عدد أكياس السحور')
lab4.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab4.config(fg="black")
lab4.config(background='white')
lab4.place(relx = 1, x =-2, y = 160, anchor = NE)

lab5 = Label(root, text='إجمالي عدد أكياس السحور')
lab5.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab5.config(fg="black")
lab5.config(background='white')
lab5.place(relx = 1, x =-270, y = 160, anchor = NE)

line2 = Image.open(path('data/red line.png'))
line2 = ImageTk.PhotoImage(line2)
line2_label = tk.Label(root, image=line2)
line2_label.config(background='white')
line2_label.place(x = 300, y = 210, anchor = CENTER)

lab6 = Label(root, text='عدد كراتين المواد الغذائية')
lab6.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab6.config(fg="black")
lab6.config(background='white')
lab6.place(relx = 1, x =-2, y = 225, anchor = NE)

lab7 = Label(root, text='إجمالي عدد الكراتين')
lab7.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab7.config(fg="black")
lab7.config(background='white')
lab7.place(relx = 1, x =-310, y = 225, anchor = NE)

line3 = Image.open(path('data/red line.png'))
line3 = ImageTk.PhotoImage(line3)
line3_label = tk.Label(root, image=line3)
line3_label.config(background='white')
line3_label.place(x = 300, y = 275, anchor = CENTER)

lab8 = Label(root, text='عدد سيارات تم تنزيلها')
lab8.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab8.config(fg="black")
lab8.config(background='white')
lab8.place(relx = 1, x =-2, y = 290, anchor = NE)

lab9 = Label(root, text='تفاصيل')
lab9.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab9.config(fg="black")
lab9.config(background='white')
lab9.place(relx = 1, x =-305, y = 290, anchor = NE)

line4 = Image.open(path('data/red line.png'))
line4 = ImageTk.PhotoImage(line4)
line4_label = tk.Label(root, image=line4)
line4_label.config(background='white')
line4_label.place(x = 300, y = 340, anchor = CENTER)

lab10 = Label(root, text='عدد سيارات تم تحميلها')
lab10.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab10.config(fg="black")
lab10.config(background='white')
lab10.place(relx = 1, x =-2, y = 360, anchor = NE)

lab11 = Label(root, text='تفاصيل')
lab11.config(font=(path("fonts/HONORSansArabicUI-H.ttf"), 20))
lab11.config(fg="black")
lab11.config(background='white')
lab11.place(relx = 1, x =-305, y = 360, anchor = NE)


# Radio Btns
lab12 = Label(root, text='Shift Manager')
lab12.config(font=(path("fonts/LeagueSpartan-Bold.otf"), 20))
lab12.config(fg="black")
lab12.config(background='white')
lab12.place(x =70, y = 480, anchor = CENTER)

manager = IntVar(value=1)

R1 = Radiobutton(
    root, text="Mahmoud Awad",
    font='fonts/LeagueSpartan-Bold.otf', fg="black",
    variable=manager, value=1, background='white'
)
R1.place(x =210, y = 480, anchor = CENTER)
R2 = Radiobutton(
    root, text="Mohamed Abdeljelel",
    font='fonts/LeagueSpartan-Bold.otf', fg="black",
    variable=manager, value=2, background='white'
)
R2.place(x =350, y = 480, anchor = CENTER)

lab14 = Label(root, text='الفترة')
lab14.config(font=(path("fonts/LeagueSpartan-Bold.otf"), 20))
lab14.config(fg="black")
lab14.config(background='white')
lab14.place(relx = 1, x =-2, y = 420, anchor = NE)

period = IntVar(value=1)

R3 = Radiobutton(
    root, text="صباحي",
    font='fonts/LeagueSpartan-Bold.otf', fg="black",
    variable=period, value=1, background='white'
)
R3.place(relx = 1, x =-100, y = 435, anchor = CENTER)
R3.config(compound='right')
R4 = Radiobutton(
    root, text="مسائي",
    font='fonts/LeagueSpartan-Bold.otf', fg="black",
    variable=period, value=2, background='white'
)
R4.place(relx = 1, x =-200, y = 435, anchor = CENTER)
R4.config(compound='right')

lab13 = Label(root, text='Leaders')
lab13.config(font=(path("fonts/LeagueSpartan-Bold.otf"), 20))
lab13.config(fg="black")
lab13.config(background='white')
lab13.place(x =44, y = 530, anchor = CENTER)



#Data Entry
entry1 = Entry(root, width=7, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry1.place(relx = 1, x =-98, y = 103, anchor = NE)

entry2 = Entry(root, width=7, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry2.place(relx = 1, x =-300, y = 103, anchor = NE)

entry3 = Entry(root, width=7, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry3.place(relx = 1, x =-520, y = 103, anchor = NE)

entry4 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry4.place(relx = 1, x =-160, y = 165, anchor = NE)

entry5 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry5.place(relx = 1, x =-490, y = 165, anchor = NE)

entry7 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry7.place(relx = 1, x =-490, y = 228, anchor = NE)

entry6 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry6.place(relx = 1, x =-210, y = 228, anchor = NE)

entry8 = Entry(root, width=13, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry8.place(relx = 1, x =-184, y = 293, anchor = NE)

entry10 = Entry(root, width=15, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry10.place(relx = 1, x =-390, y = 293, anchor = NE)

entry9 = Entry(root, width=12, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry9.place(relx = 1, x =-193, y = 364, anchor = NE)

entry11 = Entry(root, width=15, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry11.place(relx = 1, x =-390, y = 364, anchor = NE)

entry13 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry13.place(x =200, y = 520, anchor = NE)
entry14 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry14.place(x =300, y = 520, anchor = NE)
entry15 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry15.place(x =400, y = 520, anchor = NE)
entry16 = Entry(root, width=10, bg='white', fg='black', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
entry16.place(x =500, y = 520, anchor = NE)

btn = Button(root, text = 'Export', font=(path("fonts/LeagueSpartan-Bold.otf"), 40), fg='#972323', command = main.export)
btn.place(x=230, y=569)

qbtn = Button(root, text = 'Quit', font=(path("fonts/LeagueSpartan-Bold.otf"), 20), fg='Black', command = root.quit)
qbtn.place(x=510, y=600)


#dev
def callback(url):
    webbrowser.open_new_tab(url)


devlab = Label(root, text='© Developed By Moaz7assan', background='white', fg='Gray', font=(path("fonts/LeagueSpartan-Bold.otf"), 12))
devlab.place(x=215, y=640)
devlab.bind('<Button-1>', lambda e: (callback('https://www.linktr.ee/moaz7assan')))


root.mainloop()