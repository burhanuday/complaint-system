#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listComp import ListComp

#Config
conn = DBConnect()
root = Tk()
root.geometry('800x800')
root.title('FIR Complaint System')
root.configure(background='#AEB6BF')

#Style
style = Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
	style.configure(elem, background='#AEB6BF')

#Entries

w1 = Label(root,text='Welcome To FIR Complaint System',font=("Helvetica",20)).grid(row=0,column=1,padx=10, pady=10)

logo1 = PhotoImage(file="logo.png")
Label(root,image=logo1).grid(row=0)

w2 = Label(root, text='Police Station:').grid(row=1, column=0, padx=10, pady=10)
ps = StringVar(root)
ps.set("-Select Type-")
OptionMenu(root, ps,"-Select Type-" ,"Aarey","Airport","Amboli","Andheri","Bandra","Bandra Kurla Complex","Borivali","Bhandup","Charkop","Chembur", "Chunabhatti","D. N. Nagar","Dahisar","Deonar","Dindoshi","Ghatkopar", 
"Gorai","Goregaon","Govandi","Jogeshwari","Juhu","Kandivali","Kanjurmarg","Kasturba","Khar","Kherwadi","Kurar","Kurla","M I D C","M.H.B. Colony","Malad","Malwani","Mankhurd","Meghwadi","Mulund","Mumbai Sagari-2","Navghar","Nehru Nagar", 
"Nirmal Nagar","Oshiwara","Pant Nagar","Parksite","Powai","R.C.F.","Sahar","Sakinaka","Samta Nagar","Santacruz","Shivaji Nagar","Tilak Nagar","Trombay","Vakola","Vanrai","Versova","Vikhroli","Vileparle","Vinoba Bhave Nagar" ).grid(row=1,column=1)

w3 = Label(root, text='Subject:').grid(row=2, column=0, padx=10, pady=10)
subject = Entry(root,width=40,font =('Arial', 14))
subject.grid(row=2, column=1, columnspan=2)

w4 = Label(root, text='Complaint Type:').grid(row=3, column=0, padx=10, pady=10)
com = StringVar(root)
com.set("-Select Type-")
OptionMenu(root, com,"-Select Type-" ,"FeedBack", "Complaint", "Minor Crime").grid(row=3,column=1)

w5 = Label(root, text='Full Name:').grid(row=4, column=0, padx=10, pady=10)
fullname = Entry(root, width=40, font=('Arial', 14))
fullname.grid(row=4, column=1, columnspan=2)

w6 = Label(root, text='Gender:').grid(row=5, column=0, padx=10, pady=10)
SpanGender = StringVar()
Radiobutton(root, text='Male', value='male', variable=SpanGender).grid(row=5, column=1)
Radiobutton(root, text='Female', value='female', variable=SpanGender).grid(row=5, column=2)

w7 = Label(root, text='Address:').grid(row=6, column=0, padx=10, pady=10)
ad = Text(root, width=40, height=3, font=('Arial', 14))
ad.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

w8 = Label(root, text='Phone Number:').grid(row=7, column=0, padx=10, pady=10)
ph = Entry(root, width=40, font=('Arial', 14))
ph.grid(row=7, column=1, columnspan=2)

w9 = Label(root, text='Comments:').grid(row=8, column=0, padx=10, pady=10)
comment = Text(root, width=40, height=3, font=('Arial', 14))
comment.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

BuList = Button(root, text='List Comp.')
BuList.grid(row=9, column=1)
BuSubmit = Button(root, text='Submit Now')
BuSubmit.grid(row=9, column=2)


def SaveData():
	msg = conn.Add(ps.get(), subject.get(), com.get(), fullname.get(), SpanGender.get(), ad.get(1.0, 'end'), ph.get(), comment.get(1.0, 'end'), 0)
	ps.set("-Select Type-")
	subject.delete(0, 'end')
	com.set("-Select Type-")
	fullname.delete(0, 'end')
	ad.delete(1.0, 'end')
	ph.delete(0, 'end')
	comment.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

def ShowList():
	listrequest = ListComp()

BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()
