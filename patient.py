from datetime import datetime
from tkinter import messagebox
import tkinter as tk
import sqlite3


def get_connection():
    return sqlite3.connect('a.db')
# function to configure database connection and add patient to hospital database
def patient_insert():

    # entered patient data
    patient_last = patientInfo1.get()
    patient_first = patientInfo2.get()
    patient_depart = patientInfo3.get()
    patient_room = patientInfo4.get()
    patient_doctor = int(patientInfo5.get()[1])
    patient_intime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # connect to SQL database
    connection = get_connection()
    # sqlite3.connect(
    #     host="localhost",
    #     user="root",
    #     password="password",
    #     database="hospitalDBMS"
    # )
    cursor = connection.cursor()

    patient_info = (patient_last, patient_first, patient_depart, patient_room, patient_doctor, patient_intime)


    # SQL insert statement for patients
    patient_insert = ("INSERT INTO patients"
                      "(last_name, first_name, department, room, doctorid, checkin_date)"
                      "VALUES (?,?,?,?,?,?)")

    # insert patient data
    try:
        cursor.execute(patient_insert, patient_info)
        connection.commit()
        tk.messagebox.showinfo(title="Checked-in", message="Patient has been checked in successfully.")
    except sqlite3.Error as err:
        tk.messagebox.showerror(title="Error", message= f"An error has occurred. {err}.")

    root.destroy()

# function to configure tkinter window & canvas, prompt user input for patient information
def add_patient():

    global patientInfo1, patientInfo2, patientInfo3, patientInfo4, patientInfo5, root

    # configure tkinter window
    root = tk.Tk()
    root.title("Patient Check-In")
    root.minsize(400, 400)
    root.geometry("600x500")

    # connection for doctor query
    connection_doc = get_connection()
    cursor_doc = connection_doc.cursor()

    # configure canvas
    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame and label
    headingFrame = tk.Frame(root, bg="black", bd=5)#bd?
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text="Check-In Patient", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # label frame for entries
    labelFrame = tk.Frame(root, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # patient last name entry
    label1 = tk.Label(labelFrame, text="Last Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label1.place(relx=0.0, rely=0.15, relwidth=0.30, relheight=0.05)
    patientInfo1 = tk.Entry(labelFrame)
    patientInfo1.place(relx=0.27, rely=0.15, relwidth=0.6, relheight=0.05)

    # patient first name entry
    label2 = tk.Label(labelFrame, text="First Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label2.place(relx=0.0, rely=0.35, relwidth=0.30, relheight=0.05)
    patientInfo2 = tk.Entry(labelFrame)
    patientInfo2.place(relx=0.27, rely=0.35, relwidth=0.6, relheight=0.05)

    # patient department entry (drop down menu)
    label3 = tk.Label(labelFrame, text="Department : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label3.place(relx=0.0, rely=0.55, relwidth=0.30, relheight=0.05)
    options_depart = ["ER", "ICU", "Neurology", "Oncology", "Cardiology"]
    patientInfo3 = tk.StringVar(root)
    patientInfo3.set("Select")
    menu = tk.OptionMenu(labelFrame, patientInfo3, *options_depart)
    menu.place(relx=0.28, rely=0.54, relwidth=0.32, relheight=0.08)

    # patient room entry
    label4 = tk.Label(labelFrame, text="Room : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label4.place(relx=0.63, rely=0.55, relwidth=0.12, relheight=0.05)
    patientInfo4 = tk.Entry(labelFrame)
    patientInfo4.place(relx=0.77, rely=0.55, relwidth=0.10, relheight=0.05)

    # patient doctor entry (drop down menu)
    label5 = tk.Label(labelFrame, text="Primary Doctor : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label5.place(relx=0.0, rely=0.75, relwidth=0.30, relheight=0.05)

    # query for previously added doctors to select from in drop down menu
    doctor_SQL = "SELECT employeeid, first_name || ', ' || last_name FROM employees WHERE position = 'Doctor'"
    cursor_doc.execute(doctor_SQL)
    connection_doc.commit()

    options_doc = [doctor for doctor in cursor_doc.fetchall()]
    patientInfo5 = tk.StringVar(root)
    patientInfo5.set("Select")
    menu2 = tk.OptionMenu(labelFrame, patientInfo5,*options_doc)
    menu2.place(relx=0.28, rely=0.75, relwidth=0.6, relheight=0.1)


    checkin_button = tk.Button(root, text=" Check-In Patient ", font=("Arial Black", 10), command=patient_insert)
    checkin_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)
def patient_remove():

    patient_ID = patientInfo.get()

    patient_removeSQL = ("DELETE FROM patients WHERE patientid = " + patient_ID)

    try:
        connection = get_connection()
        cursor=connection.cursor()
        cursor.execute(patient_removeSQL)
        connection.commit()
        tk.messagebox.showinfo(title="Patient Check-out", message="Patient has succesfully been checked-out.")
    except sqlite3.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error occurred. {err}")

    patientInfo.delete(0, "end")
    root.destroy()


def delete_patient():

    global root, patientInfo

    root = tk.Tk()
    root.title("Check-out Patient")
    root.minsize(400, 400)
    root.geometry("600x500")

    canvas = tk.Canvas(root)#canvas k ho?
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Patient Check-out ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Label(root, bg='#cccaca')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    label_entry = tk.Label(labelFrame, text="Patient ID : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label_entry.place(relx=0.05, rely=0.5)

    patientInfo = tk.Entry(labelFrame)
    patientInfo.place(relx=0.3, rely=0.5, relwidth=0.62)

    checkout_button = tk.Button(root, text=" Check-out Patient ", font=("Arial Black", 10), command=patient_remove)
    checkout_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)
def selection_to_SQL(arg):
    switcher = {
        "Patient ID": "patientid",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Position": "position",
        "Department": "department",
        "Doctor ID": "doctorid"
    }
    return switcher[arg]

def patient_SQLsearch():

    searchSelection = clicked.get()
    searchInput = patientInfo.get()
    SQLvar = selection_to_SQL(searchSelection)


    SQL = "SELECT * FROM patients WHERE " + SQLvar + " = '" + searchInput +"'"

    root2 = tk.Tk()
    root2.title("View Patients")
    root2.minsize(400, 400)
    root2.geometry("600x500")

    # configure canvas
    canvas = tk.Canvas(root2)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root2, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Employees ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # frame for employee data
    labelFrame = tk.Frame(root2, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheigh=0.5)
    tk.Label(labelFrame,
             text="{:^10}{:^15}{:^25}{:^25}{:^10}".format('ID', 'Last Name', 'First Name', 'Position', 'Department'),
             bg="black", fg="white").place(relx=0.07, rely=0.1)

    y = 0.25

    try:
        connection = get_connection()
        cursor=connection.cursor()
        cursor.execute(SQL)
        connection.commit()
        for patient in cursor:
            tk.Label(labelFrame, text="{:^10}{:^15}{:^25}{:^25}{:^10}".format(patient[0], patient[1], patient[2], patient[4], patient[3]),
                  bg='black', fg="white").place(relx=0.07, rely=y)
            y += 0.1
    except sqlite3.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error has occurred. {err}.")

    return_button = tk.Button(root2, text=" Return to Menu ", font=("Arial Black", 10), command=root2.destroy)
    return_button.place(relx=0.4, rely=0.9, relwidth=0.25, relheight=0.08)

    root2.mainloop()


def patient_search():

    global patientInfo, label, clicked, root

    root = tk.Tk()
    root.title("Patient Search")
    root.minsize(400, 400)
    root.geometry("600x500")

    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Patient Search ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Label(root, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

    options = ["Patient ID", "Last Name", "First Name", "Department", "Doctor ID"]

    clicked = tk.StringVar(root)
    clicked.set("Select")

    menu = tk.OptionMenu(labelFrame, clicked, *options)
    tk.Label(labelFrame, text=' Search Criteria : ', bg="#cccaca", fg="black", font=("Arial Black", 9)).place(relx=0.05, rely=0.30, relheight=0.1)
    menu.place(relx=0.3, rely=0.30, relwidth=0.62, relheight=0.1)

    label_entry = tk.Label(labelFrame, text=" Search Field : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label_entry.place(relx=0.05, rely=0.55)

    patientInfo = tk.Entry(labelFrame)
    patientInfo.place(relx=0.3, rely=0.55, relwidth=0.62)

    search_button = tk.Button(root, text=" Search Patients ", font=("Arial Black", 10), command=patient_SQLsearch)
    search_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)

    root.mainloop()
