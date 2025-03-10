from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector
from govfund import Citizen

window = Tk()

window.title("SignUp")

window.geometry("1920x1080")
window.configure(bg="#fff")
window.resizable(False, False)

# Connect to MySQL database ------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="govfund"
)

# Create a cursor object
mycursor = mydb.cursor()

# SIGNUP FUNCTION ------------------


def signup():
    # Get user input from the entry widgets
    username = user.get()
    password = code.get()
    confirmCode = confirm_code.get()

    # Check if username already exists in database
    mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    temp = mycursor.fetchone()

    if temp:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new user into database
        if password == confirmCode:
            mycursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mydb.commit()
            messagebox.showinfo("Success", "User created successfully")
            Citizen(window)
        else:
            messagebox.showerror(
                "Error", "Password and Confirm Password doesn't match")


img = PhotoImage(file='images/login.png')
Label(window, image=img, border=0, bg='white').place(x=400, y=250)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=800, y=200)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white',
                font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


# username -------------------------------

def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user. insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)

user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# PASSWORD
# -------------------------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code. insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)

code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# PASSWORD
# -------------------------------


def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code. insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, fg='black', border=0,
                     bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=220)

confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# signinpage -------


def signinpage():
    window.destroy()
    import signin



# button  ---------------------------------------
print(user.get())
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8',
       fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text='I have an account', fg="black",
              bg='white', font=('Microsoft YaHei UI Light', 10))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0,
                bg='white', cursor='hand2', fg='#57a1f8', command=signinpage)
signin.place(x=200, y=343)





window.mainloop()
