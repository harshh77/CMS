#frontend
from tkinter import *
import tkinter.messagebox
import back1
import os




class cust:

    def __init__(self,root):

        self.root = root
        self.root.title("CMS")
        self.root.geometry("700x700")
        self.root.configure(bg="black")

        self.id = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.mob = StringVar()
        self.address = StringVar()
        self.salary = StringVar()
        self.gender = StringVar()
        self.doj = StringVar()
        self.x=StringVar()
        self.y=0

        btn = Button(root, text="ADD CUSTOMER", font=12, command=self.add)
        btn.place(x=230, y=50)

        btn1 = Button(root, text="SEARCH CUSTOMER", font=12, command=self.search)
        btn1.place(x=230, y=150)
        #
        btn2 = Button(root, text="MODIFY CUSTOMER", font=12, command=self.modify)
        btn2.place(x=230, y=250)
        #
        btn3 = Button(root, text="DELETE CUSTOMER", font=12, command=self.delete)
        btn3.place(x=230, y=350)
        #
        btn4 = Button(root, text="SHOW CUSTOMERS", font=12, command=self.show)
        btn4.place(x=230, y=450)

        btn5 = Button(root, text="EXIT", font=12, command=self.iexit)
        btn5.place(x=230, y=550)

    def iexit(self):
            iexit = tkinter.messagebox.askyesno("CMS", "Do you want to exit?")
            if iexit > 0:
                root.destroy()
                return



    def adata(self):

               x = self.entr1.get()
               for ro in back1.count():

                 y = ''.join(ro)

                 if y == x:
                     print("hmmm")
                     tkinter.messagebox.showinfo("error","enter a unique id")

               back1.addrec(self.entr1.get(), self.entr2.get(), self.entr3.get(), self.entr4.get(), self.entr5.get(), self.entr6.get(),self.entr7.get(), self.entr8.get())


    def deli(self):
            back1.deltrec(self.entr12.get())



    def modi(self):
            back1.modirec(self.entr11.get(), self.entr22.get(), self.entr33.get(), self.entr44.get(), self.entr55.get(), self.entr66.get(),self.entr77.get(), self.entr88.get())

    def add(self):
            win = Tk()
            win.geometry("800x800")
            win.title("add")

            def clr():
                self.entr1.delete(0, END)
                self.entr2.delete(0, END)
                self.entr3.delete(0, END)
                self.entr4.delete(0, END)
                self.entr5.delete(0, END)
                self.entr6.delete(0, END)
                self.entr7.delete(0, END)
                self.entr8.delete(0, END)

            lb = Label(win, text="ID", bg="yellow", font=32)
            lb.grid(row=0, column=0, pady=40)

            lb2 = Label(win, text="NAME", bg="yellow", font=32)
            lb2.grid(row=1, column=0, pady=10)

            lb3 = Label(win, text="AGE", bg="yellow", font=32)
            lb3.grid(row=2, column=0, pady=40)

            lb4 = Label(win, text="MOBILE NO", bg="yellow", font=32)
            lb4.grid(row=3, column=0, pady=40)

            lb5 = Label(win, text="ADDRESS", bg="yellow", font=32)
            lb5.grid(row=4, column=0, pady=40)

            lb6 = Label(win, text="SALARY", bg="yellow", font=32)
            lb6.grid(row=5, column=0, pady=40)

            lb7 = Label(win, text="GENDER", bg="yellow", font=32)
            lb7.grid(row=6, column=0, pady=40)

            lb8 = Label(win, text="DATE OF JOINING", bg="yellow", font=32)
            lb8.grid(row=7, column=0, pady=40)

            self.entr1 = Entry(win, font=32,textvariable=self.id)
            self.entr1.grid(row=0, column=1)

            self.entr2 = Entry(win, font=32,textvariable=self.name)
            self.entr2.grid(row=1, column=1)

            self.entr3 = Entry(win, font=32,textvariable=self.age)
            self.entr3.grid(row=2, column=1)

            self.entr4 = Entry(win, font=32,textvariable=self.mob)
            self.entr4.grid(row=3, column=1)

            self.entr5 = Entry(win, font=32,textvariable=self.address)
            self.entr5.grid(row=4, column=1)

            self.entr6 = Entry(win, font=32,textvariable=self.salary)
            self.entr6.grid(row=5, column=1)

            self.entr7 = Entry(win, font=32,textvariable=self.gender)
            self.entr7.grid(row=6, column=1)

            self.entr8 = Entry(win, font=32,textvariable=self.doj)
            self.entr8.grid(row=7, column=1)

            btn1 = Button(win, text="ADD", font=12, command=self.adata)
            btn1.place(x=600, y=300)

            btn2  =Button(win, text="CLEAR", font=12, command=clr)
            btn2.place(x=600, y=400)

            # win.mainloop()

    def modify(self):
            win = Tk()
            win.geometry("800x800")
            win.title("modify")

            lb = Label(win, text="ID", bg="yellow", font=32)
            lb.grid(row=0, column=0, pady=40)

            lb2 = Label(win, text="NAME", bg="yellow", font=32)
            lb2.grid(row=1, column=0, pady=10)

            lb3 = Label(win, text="AGE", bg="yellow", font=32)
            lb3.grid(row=2, column=0, pady=40)

            lb4 = Label(win, text="MOBILE NO", bg="yellow", font=32)
            lb4.grid(row=3, column=0, pady=40)

            lb5 = Label(win, text="ADDRESS", bg="yellow", font=32)
            lb5.grid(row=4, column=0, pady=40)

            lb6 = Label(win, text="SALARY", bg="yellow", font=32)
            lb6.grid(row=5, column=0, pady=40)

            lb7 = Label(win, text="GENDER", bg="yellow", font=32)
            lb7.grid(row=6, column=0, pady=40)

            lb8 = Label(win, text="DATE OF JOINING", bg="yellow", font=32)
            lb8.grid(row=7, column=0, pady=40)

            self.entr11 = Entry(win, font=32, textvariable=self.id)
            self.entr11.grid(row=0, column=1)

            self.entr22 = Entry(win, font=32, textvariable=self.name)
            self.entr22.grid(row=1, column=1)

            self.entr33 = Entry(win, font=32, textvariable=self.age)
            self.entr33.grid(row=2, column=1)

            self.entr44 = Entry(win, font=32, textvariable=self.mob)
            self.entr44.grid(row=3, column=1)

            self.entr55 = Entry(win, font=32, textvariable=self.address)
            self.entr55.grid(row=4, column=1)

            self.entr66 = Entry(win, font=32, textvariable=self.salary)
            self.entr66.grid(row=5, column=1)

            self.entr77 = Entry(win, font=32, textvariable=self.gender)
            self.entr77.grid(row=6, column=1)

            self.entr88 = Entry(win, font=32, textvariable=self.doj)
            self.entr88.grid(row=7, column=1)

            btn0 = Button(win, text="MODIFY", font=12, command=self.modi)
            btn0.place(x=500, y=400)

            # win.mainloop()
        #
    def search(self):
            win = Tk()
            win.geometry("800x800")
            win.title("search")

            def sir():
                labe.delete(0, END)
                for row in back1.srchrec(self.entr10.get(),self.entr11.get(),self.entr12.get(),self.entr13.get(),self.entr14.get(),self.entr15.get(),self.entr16.get(),self.entr17.get()):
                    labe.insert(END, row, str(""))

            labe = Listbox(win, width=45, height=30, bg="white")
            labe.place(x=500, y=10)

            lb = Label(win, text="ID", bg="yellow", font=32)
            lb.place(x=10, y=30)

            lb2 = Label(win, text="NAME", bg="yellow", font=32)
            lb2.place(x=10, y=90)

            lb3 = Label(win, text="AGE", bg="yellow", font=32)
            lb3.place(x=10, y=150)

            lb4 = Label(win, text="MOBILE NO", bg="yellow", font=32)
            lb4.place(x=10, y=210)

            lb5 = Label(win, text="ADDRESS", bg="yellow", font=32)
            lb5.place(x=10, y=270)

            lb6 = Label(win, text="SALARY", bg="yellow", font=32)
            lb6.place(x=10, y=330)

            lb7 = Label(win, text="GENDER", bg="yellow", font=32)
            lb7.place(x=10, y=390)

            lb8 = Label(win, text="DATE OF JOINING", bg="yellow", font=32)
            lb8.place(x=10, y=450)

            self.entr10 = Entry(win, font=32)
            self.entr10.place(x= 200, y=30)

            self.entr11 = Entry(win, font=32)
            self.entr11.place(x=200, y=90)

            self.entr12 = Entry(win, font=32)
            self.entr12.place(x=200, y=150)

            self.entr13 = Entry(win, font=32)
            self.entr13.place(x=200, y=210)

            self.entr14 = Entry(win, font=32)
            self.entr14.place(x=200, y=270)

            self.entr15 = Entry(win, font=32)
            self.entr15.place(x=200, y=330)

            self.entr16 = Entry(win, font=32)
            self.entr16.place(x=200, y=390)

            self.entr17 = Entry(win, font=32)
            self.entr17.place(x=200, y=450)

            btn = Button(win, text="SEARCH", font=12, command=sir)
            btn.place(x=370, y=700)



            # win.mainloop()
        #
        #
        #
    def delete(self):
            win = Tk()
            win.geometry("800x800")
            win.title("delete")

            lb = Label(win, text="ID", bg="yellow", font=32)
            lb.grid(row=0, column=0, pady=40)

            self.entr12 = Entry(win, font=32)
            self.entr12.grid(row=0, column=1)

            btn = Button(win, text="DELETE", font=12, command=self.deli)
            btn.place(x=370, y=200)

            # win.mainloop()
        #

    def show(self):
            win = Tk()
            win.geometry("800x800")
            win.title("show")
            win.configure(bg="black")

            lab = Listbox(win, width=45, height=30, bg="white")
            lab.pack()

            def disp():
                lab.delete(0, END)

                for row in back1.view():
                    lab.insert(END, row, str(""))

            btn = Button(win, text="show", font=12, command=disp)
            btn.place(x=370, y=500)






def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


if __name__ == '__main__':
    main_account_screen()
    root = Tk()
    application = cust(root)
    root.mainloop()
