import random
from tkcalendar import *
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import os
import datetime
from tkinter import messagebox
from PIL import ImageTk,Image
def detail_user_register():
    status='no'
    detail_name1=detail_name.get()
    detail_email1=detail_email.get()
    detail_phone1=detail_phone.get()
    detail_room1=detail_room.get()
    detail_cheakin1=detail_reg_cheakin.get_date()
    detail_cheakout1=detail_reg_cheakout.get_date()
    detail_reg_name.delete(0,END)
    detail_reg_email.delete(0,END)
    detail_reg_phone.delete(0,END)
    detail_reg_room.delete(0,END)
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute('insert into user_table values("'+detail_name1+'","'+detail_email1+'","'+detail_phone1+'","'+detail_room1+'","'+detail_cheakin1+'","'+detail_cheakout1+'")')
    curser.execute('commit')
    messagebox.showinfo('sucess','sucessfully submit')
    con.close()
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute("UPDATE roominfo SET availability ='" + status + "' WHERE room='" + detail_room1 + "'")

    curser.execute('commit')
    messagebox.showinfo('sucess', 'sucessfully submit')
    con.close()

def details_register():
    screen8 = Toplevel(screen)
    screen8.geometry('700x700')
    global detail_name,detail_email,detail_phone,detail_room, detail_cheakin, detail_cheakout
    global detail_reg_name,detail_reg_email,detail_reg_phone,detail_reg_room, detail_reg_cheakin, detail_reg_cheakout

    detail_name=StringVar()
    detail_email = StringVar()
    detail_phone = StringVar()
    detail_room = StringVar()
    detail_cheakin = StringVar()
    detail_cheakout = StringVar()
    Label(screen8,text='coustomer detail register').pack()
    Label(screen8,text='name').pack()
    detail_reg_name=Entry(screen8,textvariable=detail_name)
    detail_reg_name.pack()
    Label(screen8,text='email').pack()
    detail_reg_email=Entry(screen8, textvariable=detail_email)
    detail_reg_email.pack()
    Label(screen8,text='phone').pack()
    detail_reg_phone=Entry(screen8, textvariable=detail_phone)
    detail_reg_phone.pack()
    Label(screen8,text='room no').pack()
    detail_reg_room=Entry(screen8, textvariable=detail_room)
    detail_reg_room.pack()
    Label(screen8,text='cheakin date').pack()
    detail_reg_cheakin=Calendar(screen8,selectmode='day',year=2020,month=9,day=18)
    detail_reg_cheakin.pack()
    Label(screen8,text='cheakout date').pack()
    detail_reg_cheakout=Calendar(screen8,selectmode='day',year=2020,month=9,day=18)
    detail_reg_cheakout.pack()
    Button(screen8,text='submit',command=detail_user_register).pack()
def register_user():
    name_info=name.get()
    email_info=email.get()
    file=open(name_info,'w')
    file.write(name_info+'\n')
    file.write(email_info)
    file.close()
    details_register()
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    Label(screen1,text='registration successfull',bg='green').pack()
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title('register')
    screen1.geometry('300x300')
    global name,email,name_entry,email_entry
    name= StringVar()
    email= StringVar()
    Label(screen1,text='enter details to register').pack()
    Label(screen1,text='name').pack()
    name_entry=Entry(screen1,textvariable=name)
    name_entry.pack()
    Label(screen1,text='email').pack()
    email_entry=Entry(screen1,textvariable=email)
    email_entry.pack()
    Button(screen1,text='register',command=register_user).pack()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()

#showing user data.......
def login_success():
    screen6=Toplevel(screen)
    show_data=ttk.Treeview(screen6,show='headings',height='5')
    show_data.pack()
    show_data['columns']=('1','2','3','4','5','6')
    show_data.heading('1',text='name')
    show_data.heading('2',text='email')
    show_data.heading('3',text='phone')
    show_data.heading('4',text='room no')
    show_data.heading('5',text='cheakin date')
    show_data.heading('6',text='cheakout date')

    show_data.column('1',width=90)
    show_data.column('2',width=90)
    show_data.column('3',width=90)
    show_data.column('4',width=90)
    show_data.column('5',width=90)
    show_data.column('6',width=90)
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute('select * from user_table')
    for data in curser:
        if(data[1]==email1):
            show_data.insert('', 'end', values=data)
    con.close()


def email_wrong():
    global screen4
    screen4=Toplevel(screen)
    Label(screen4,text='email wrong',bg='red').pack()
    Button(text='ok', command=delete3).pack()
def name_notfound():
    global screen5
    screen5=Toplevel(screen)
    Label(screen5,text='name not found',bg='red').pack()
    Button(text='ok', command=delete4).pack()

def login_verify():
    global email1
    name1=name_entry1.get()
    email1=email_entry1.get()
    name_entry1.delete(0,END)
    email_entry1.delete(0,END)
    list_of_files=os.listdir()
    if name1 in list_of_files:
        file1=open(name1,'r')
        verify=file1.read().splitlines()
        if email1 in verify:
            login_success()
        else:
            email_wrong()
    else:
        name_notfound()


# pass three function email_wrong(line number 103) name_notfound(line number 108) login_success(line number 82)

def login():
    global screen2,name_entry1,email_entry1
    name_verify=StringVar()
    email_verify=StringVar()
    screen2=Toplevel(screen)
    Label(screen2,text='login here')
    screen2.geometry('300x300')
    Label(screen2, text='enter details to login').pack()
    Label(screen2,text='name').pack()
    name_entry1=Entry(screen2,textvariable=name_verify)
    name_entry1.pack()
    Label(screen2, text='email').pack()
    email_entry1=Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Button(screen2,text='submit',command=login_verify).pack()

#pass three function login verify(line number 114)
def room_submit():
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute(
        'insert into roominfo values("' + roomno1.get() + '","' + email1.get() + '","' + roomtype1.get() + '","' + price1.get() + '","' + avail1.get() + '")')
    curser.execute('commit')
    messagebox.showinfo('sucess', 'sucessfully submit')
    con.close()


def addroom():
    screen10=Toplevel(screen)
    global roomno1,email1,roomtype1,price1,avail1
    roomno=IntVar()
    email=StringVar()
    roomtype=StringVar()
    price=IntVar()
    avail=StringVar()
    Label(screen10,text='room no').pack()
    roomno1=Entry(screen10,textvariable=roomno)
    roomno1.pack()
    Label(screen10,text='countomer email').pack()
    email1=Entry(screen10, textvariable=email)

    Label(screen10,text='roomtype').pack()
    roomtype1=Entry(screen10, textvariable=roomtype)
    roomtype1.pack()
    Label(screen10,text='price').pack()
    price1=Entry(screen10, textvariable=price)
    price1.pack()
    Label(screen10,text='availability').pack()
    avail1=Entry(screen10, textvariable=avail)
    avail1.pack()
    Button(screen10,text='submit',command=room_submit).pack()
def update_room():
    entry3=entry1_.get()
    entry5=clicked.get()
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute("UPDATE roominfo SET availability ='"+entry5+"' WHERE room='"+entry3+"'")

    curser.execute('commit')
    messagebox.showinfo('sucess', 'sucessfully submit')
    con.close()

def update_room_status():
    global entry1_,entry2_,clicked
    update_data_room=IntVar()
    clicked=StringVar()
    update_room_status=StringVar()
    screen11=Toplevel(screen)
    screen11.geometry('200x200')
    Label(screen11,text='room no.').pack()
    entry1_=Entry(screen11,textvariable=update_data_room)
    entry1_.pack()
    Label(screen11, text='status').pack()
    entry2_=OptionMenu(screen11,clicked,'yes','no')
    entry2_.pack()
    Button(screen11, text='add room', command=update_room).pack()
def avail_room():
    screen12=Toplevel(screen)
    screen12.geometry('300x300')
    screen12.title('room_availability')
    show_avail_room = ttk.Treeview(screen12, show='headings', height='5')
    show_avail_room.pack()
    show_avail_room['columns'] = ('1', '2', '3')
    show_avail_room.heading('1', text='room')
    show_avail_room.heading('2', text='room type')
    show_avail_room.heading('3', text='price')
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute('select * from roominfo')
    for data in curser:
        if (data[4] =='yes'):
            show_avail_room.insert('', 'end', values=(data[0],data[2],data[3]))
    con.close()

    show_avail_room.column('1', width=100)
    show_avail_room.column('2', width=100)
    show_avail_room.column('3', width=100)

def admin_panel():
    screen9=Toplevel(screen)
    screen9.geometry('800x800')
    screen9.title('admin panel')
    Label(text='admin panel')
    show_data_all = ttk.Treeview(screen9, show='headings', height='5')
    show_data_all.pack()
    show_data_all['columns'] = ('1', '2', '3', '4', '5', '6')
    show_data_all.heading('1', text='name')
    show_data_all.heading('2', text='email')
    show_data_all.heading('3', text='phone')
    show_data_all.heading('4', text='room no')
    show_data_all.heading('5', text='cheakin date')
    show_data_all.heading('6', text='cheakout date')

    show_data_all.column('1', width=100)
    show_data_all.column('2', width=100)
    show_data_all.column('3', width=100)
    show_data_all.column('4', width=100)
    show_data_all.column('5', width=100)
    show_data_all.column('6', width=100)
    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute('select * from user_table')
    for data in curser:
        show_data_all.insert('','end',values=data)
    con.close()
    show_room_all = ttk.Treeview(screen9, show='headings', height='5')
    show_room_all.pack()
    show_room_all['columns'] = ('1', '2', '3', '4', '5', '6')
    show_room_all.heading('1', text='room no')
    show_room_all.heading('2', text='customer_email')
    show_room_all.heading('3', text='room type')
    show_room_all.heading('4', text='price')
    show_room_all.heading('5', text='availability')

    show_room_all.column('1', width=80)
    show_room_all.column('2', width=80)
    show_room_all.column('3', width=80)
    show_room_all.column('4', width=80)
    show_room_all.column('5', width=80)

    con = mysql.connect(host='localhost', user='root', password='1234', database='hotel_management')
    print('connected')
    curser = con.cursor()
    curser.execute('select * from roominfo')
    for data in curser:
        show_room_all.insert('', 'end', values=data)
    con.close()

    Button(screen9, text='update status', command=update_room_status).pack()
    Button(screen9, text='available room', command=avail_room).pack()
    Button(screen9,text='add room',command=addroom).pack()

def room_detail():
    today=datetime.datetime.now().day



#mail frame......

def main_screen():
    global screen
    screen=Tk()
    screen.geometry('500x500')
    screen.title('hotel reservation system')

    img=ImageTk.PhotoImage(Image.open('hotel.jpg'))
    Label(image=img).pack()
    Label(text="admin", bg='gray', width='300', height='2').pack()

    Label(text='').pack()
    Label(text='').pack()
    Button(text='admin', height='2', width='30', command=admin_panel).pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(text="customer",bg='gray',width='300',height='2').pack()
    Label(text='').pack()
    Button(text='login',height='2',width='30',command=login).pack()
    Label(text='').pack()
    Button(text='register', height='2', width='30',command=register).pack()
    Label(text='').pack()
    Button(text='register', height='2', width='30', command=room_detail).pack()



#pass two method login(line number 129) and register(line number 62)

    screen.mainloop()
main_screen()



