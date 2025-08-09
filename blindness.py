
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import mysql.connector as sk
from model import *

print('GUI SYSTEM STARTED...')

def LogIn():
    username = box1.get()

    u = 1

    if len(username) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter Username and Password")

    if u:
        password = box2.get()

        if len(password):
            query = "SELECT * FROM GREAT"

            sql.execute(query)

            data = sql.fetchall()

            g = 0
            b = 0

            for i in data:
                if i[0] == username:
                    g = 1
                if i[1] == password:
                    b = 1

            if g and b:
                messagebox.showinfo('Hello', 'Welcome to Diabetic Retinopathy Detection')
                open_new_tab()
            else:
                messagebox.showinfo('Sorry', 'Wrong Username or Password')

            global y
            y = True
        else:
            messagebox.showinfo("Error", "You must enter a password!")

def open_new_tab():
    global tab_control
    tab2 = Frame(tab_control)
    tab_control.add(tab2, text="Upload Image")
    tab_control.select(tab2)

    upload_button = Button(tab2, text="Upload Image", command=OpenFile)
    upload_button.place(relx=0.2, rely=0.5, anchor=W)

    global canvas, prediction_label, predict_button
    canvas = Canvas(tab2, width=400, height=400)
    canvas.place(relx=0.7, rely=0.4, anchor=CENTER)

    prediction_label = Label(tab2, font=('Arial', 14))
    prediction_label.place(relx=0.65, rely=0.7, anchor=CENTER)

    predict_button = Button(tab2, text="Predict", command=predict_image)
    predict_button.place(relx=0.65, rely=0.8, anchor=CENTER)
    predict_button.config(state=DISABLED)

def OpenFile():
    try:
        global image_path
        image_path = askopenfilename(initialdir='C:/Users/Dhanush/OneDrive/Desktop/Final year project/test_images',
                                     filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not image_path:
            messagebox.showinfo("Invalid Image", "No image selected.")
            return

        if not image_path.startswith('C:/Users/Dhanush/OneDrive/Desktop/Final year project/test_images'):
            messagebox.showinfo("Invalid Image", "Please select an eye image.")
            return

        image = Image.open(image_path)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.image = photo

        predict_button.config(state=NORMAL)
    except Exception as error:
        print("Error:", error)
        messagebox.showinfo("Error", "An error occurred while processing the image.")

def predict_image():
    try:
        if image_path:
            value, classes = main(image_path)
            prediction_label.config(text=f'Predicted Label: {value}\nPredicted Class: {classes}')
    except Exception as error:
        print("Error:", error)
        messagebox.showinfo("Error", "An error occurred while predicting the image.")

def Signup():
    username = box1.get()
    password = box2.get()

    u = 1

    if len(username) == 0 or len(password) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter Username and Password")

    if u:
        query1 = "SELECT * FROM GREAT"
        sql.execute(query1)

        data = sql.fetchall()

        z = 1

        for i in data:
            if i[0] == username:
                messagebox.showinfo("Sorry",
                                    "The username is already registered, try a new one or try login")
                z = 0

        if z:
            query = "INSERT INTO GREAT (USERNAME, PASSWORD) VALUES('%s', '%s')" % (username, password)
            messagebox.showinfo("signed up", ('Hi ', username, '\n Now you can login with your credentials'))
            sql.execute(query)
            connection.commit()

connection = sk.connect(
    host="localhost",
    user="root",
    password="dhanush@2003",
    database="batch_db_new"
)

sql = connection.cursor()

root = Tk()
root.geometry('800x500')
root.title("Diabetic Retinopathy")

tab_control = Notebook(root)
tab1 = Frame(tab_control)
tab_control.add(tab1, text="Login")
tab_control.pack(expand=1, fill="both")

bg_image = Image.open('C:/Users/Dhanush/OneDrive/Desktop/Final year project/Diabetic-Retinopathy-Detection/BG1.png')
bg_image = bg_image.resize((1500, 800))
background = ImageTk.PhotoImage(bg_image)
background_label = Label(tab1, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = Label(tab1, text="Diabetic Retinopathy Detection", font=('Arial', 30))
title_label.grid(row=1, column=0, columnspan=2, pady=20, sticky='n')

username_label = Label(tab1, text="Enter your username: ", font=('Arial', 20))
username_label.grid(row=2, column=0, pady=10, padx=20, sticky='e')

box1 = Entry(tab1)
box1.grid(row=2, column=1, pady=10, sticky='w')

password_label = Label(tab1, text="Enter your password: ", font=('Arial', 20))
password_label.grid(row=3, column=0, pady=10, padx=20, sticky='e')

box2 = Entry(tab1, show='*')
box2.grid(row=3, column=1, pady=10, sticky='w')

signup_button = Button(tab1, text="Signup", command=Signup)
signup_button.grid(row=4, column=0, pady=20, padx=20)

login_button = Button(tab1, text="LogIn", command=LogIn)
login_button.grid(row=4, column=1, pady=20, padx=20)

tab1.grid_rowconfigure(0, weight=1)
tab1.grid_rowconfigure(1, weight=1)
tab1.grid_rowconfigure(2, weight=1)
tab1.grid_rowconfigure(3, weight=1)
tab1.grid_rowconfigure(4, weight=1)
tab1.grid_rowconfigure(5, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

root.mainloop()
