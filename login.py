from tkinter import*
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")

        #login frame
        Frame_login=Frame(self.root,bg="Red")
        Frame_login.place(x=150,y=150,height=340,width=500)
                             

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77336").place(x=90,y=30)
        desc= Label(Frame_login, text="Accountant Employee Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17").place(x=90, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"),fg="grey").place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("time new roman",15))
        self.txt_user.place (x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("time new roman", 15))
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="Black",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)

        login_btn = Button(self.root,command=self.login_function,cursor="hand2", text="Login", bg="Black", fg="#d77337",font=("times new roman", 20)).place(x=300, y=470,width=180,height=40)

    def login_function(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required ",parent=self.root)
        elif self.txt_pass.get()!="123@aman" or self.txt_user.get()!="Aman":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root )
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.txt_user.get()}\nYour Password: {self.txt_pass.get}")



root=Tk()
obj=login(root)
root.mainloop()
