import tkinter as tk
from PIL import ImageTk, Image
from all import *
# connect to database using sqlite3
connection = sqlite3.connect('adb')




# configure main tkinter window
root = tk.Tk()
root.title("Swastha")
root.minsize(width=400, height=400)
root.geometry("600x500")

# function to resize background image
def image_resize(event):
    global background_image, resized, background_image2
    background_image = Image.open("main_background.jpg")
    resized = background_image.resize((event.width, event.height), Image.LANCZOS)

    background_image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=background_image2, anchor="nw")

# add background image to main application screen
background_image = ImageTk.PhotoImage(file="main_background.jpg")
canvas = tk.Canvas(root, width=700, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
# root.bind("<Configure>", image_resize)


# add heading frame
headingFrame1 = tk.Frame(root, bg="black", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = tk.Label(headingFrame1, text="Welcome to Swastha\n A Hospital Management System", bg="black", fg="white", font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# add main screen buttons
button1 = tk.Button(root, text="Check-in Patient", bg="black", fg="white", command=add_patient)
button1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

button2 = tk.Button(root, text="Check-out Patient", bg="black", fg="white", command=delete_patient)
button2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

button3 = tk.Button(root, text="View Patients", bg="black", fg="white", command=view_patients)
button3.place(relx=0.28, rely=0.5, relwidth=0.225, relheight=0.1)

button4 = tk.Button(root, text="Search Patients", bg="black", fg="white", command=patient_search)
button4.place(relx=0.505, rely=0.5, relwidth=0.225, relheight=0.1)

button5 = tk.Button(root, text="Add Employee", bg="black", fg="white",command=add_employee)
button5.place(relx=0.28, rely=0.6, relwidth=0.225, relheight=0.1)

button6 = tk.Button(root, text="Remove Employee", bg="black", fg="white", command=delete_employee)
button6.place(relx=0.505, rely=0.6, relwidth=0.225, relheight=0.1)

button7 = tk.Button(root, text="View Employees", bg="black", fg="white", command=view_employees)
button7.place(relx=0.28, rely=0.7, relwidth=0.225, relheight=0.1)

button8 = tk.Button(root, text="Search Employees", bg="black", fg="white",command=employee_search)
button8.place(relx=0.505, rely=0.7, relwidth=0.225, relheight=0.1)

button9 = tk.Button(root, text=" Exit ", bg="black", fg="white", command=root.destroy)
button9.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)



root.mainloop()



