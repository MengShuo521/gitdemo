# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:04:38 2019

@author: Sakura
"""

import tkinter as tk 
import tkinter.messagebox

def usr_login():

    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name in n and teacher_account[usr_name]==usr_pwd:
        tkinter.messagebox.showinfo('登录成功', "欢迎，教师%s"%usr_name.capitalize())
        king.destroy()
        nex()
    else:
        tkinter.messagebox.showerror('登录失败', "用户名或密码错误")

def tui():
    king.destroy()

def nex():
    global top
    top=tk.Tk()
    top.title("学生管理系统")
    top.geometry('375x250')
    b1 = tk.Button(top, text='添加成绩', width=10,
               height=2, command=tianjia)
    b1.pack()
    b2 = tk.Button(top, text='查看成绩', width=10,
               height=2, command=chengji)
    b2.pack()
    b3 = tk.Button(top, text='退出系统', width=10,
               height=2, command=tuichu)
    b3.pack()
    top.mainloop()

global student_list
student_list={"ZS":99,"ZMS":95,"LS":100}
name=student_list.keys()
global m
global n
teacher_account={"001001":"321321","002002":"456456"}
n=teacher_account.keys()
m=teacher_account.values()

def tuichu():
    top.destroy()

def tuichu1():
    window_sign_up.destroy()

def tuichu2():
    window.destroy()

def chengji():
    name=student_list.keys()
    for i in name:
        print("姓名："+i,"成绩："+str(student_list[i]))

def panduan():
    nn = new_name.get()
    tuichu1()
    if nn in name:
        tkinter.messagebox.showerror('错误', "该学生已存在！")
    else:
        xiefen()

def xiefen():
    global window
    global new_fen
    window= tk.Toplevel(top)
    window.geometry('300x200')
    window.title('提示')
    new_fen = tk.StringVar()
    new_fen.set('')  
    tk.Label(window, text='请输入学生成绩 ').place(x=10, y=10)
    entry_new_fen = tk.Entry(window, textvariable=new_fen)
    entry_new_fen.place(x=130, y=10) 
    btn_login = tk.Button(window, text='OK', command=jilu)
    btn_login.place(x=60, y=120)
    btn_login = tk.Button(window, text='CANCEL', command=tuichu2)
    btn_login.place(x=120, y=120)

def jilu():
    nn = new_name.get()
    np = new_fen.get()
    student_list[nn]=np
    tuichu2()
    tkinter.messagebox.showinfo('提示', "添加成功！")

def tianjia():
    global new_name
    global window_sign_up
    window_sign_up = tk.Toplevel(top)
    window_sign_up.geometry('300x200')
    window_sign_up.title('提示')
    new_name = tk.StringVar()  
    new_name.set('')  
    tk.Label(window_sign_up, text='请输入学生姓名 ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=130, y=10) 
    btn_login = tk.Button(window_sign_up, text='OK', command=panduan)
    btn_login.place(x=60, y=120)
    btn_login = tk.Button(window_sign_up, text='CANCEL', command=tuichu1)
    btn_login.place(x=120, y=120)

king=tk.Tk()
king.title('学生管理系统登录界面')

king.geometry('375x250')  
tk.Label(king, text='用户名:', font=('Arial', 14)).place(x=10, y=120)
tk.Label(king, text='用户密码:', font=('Arial', 14)).place(x=10, y=150)


global var_usr_name
global var_usr_pwd
var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(king, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=120)

var_usr_pwd = tk.StringVar()

entry_usr_pwd = tk.Entry(king, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=150)
btn_login = tk.Button(king, text='OK', command=usr_login)
btn_login.place(x=60, y=190)
btn_login = tk.Button(king, text='CANCEL', command=tui)
btn_login.place(x=120, y=190)
king.mainloop()