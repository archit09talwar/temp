from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Hospital Management System")

        lbl_title = Label(self.root,relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", font=("times new roman", 50, "bold"), bg="white", fg="green",bd=20)
        lbl_title.pack(side=TOP, fill=X)

        data_frame = Frame(self.root, bg="white", bd=20, relief=RIDGE)
        data_frame.place(x=0, y=130, width=1280, height=350)

        data_frame_left = LabelFrame(data_frame,text="Patient Information",padx=10,bd=10,relief=RIDGE,font=("times new roman", 12, "bold"))
        data_frame_left.place(x=0, y=5, width=775, height=300)

        data_frame_right = LabelFrame(data_frame,text="Prescription",padx=10,bd=10,relief=RIDGE,font=("times new roman", 12, "bold"))
        data_frame_right.place(x=783, y=5, width=450, height=300)

        button_frame = Frame(self.root, bd=20, relief=RIDGE)
        button_frame.place(x=0, y=480, width=1280, height=70)

        details_frame = Frame(self.root, bd=20, relief=RIDGE)
        details_frame.place(x=0, y=550, width=1280, height=145)

        field_vars = {}

        # Fields for patient information
        fields = [
            ("Name of Tablets", "combo", ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Activan")),
            ("Reference No", "entry"),
            ("Dose", "entry"),
            ("No of Tablets", "entry"),
            ("Lot", "entry"),
            ("Issue Date", "entry"),
            ("Exp Date", "entry"),
            ("Daily Dose", "entry"),
            ("Side Effect", "entry"),
        ]


        for row, (label_text, widget_type, *options) in enumerate(fields):
            lbl = Label(data_frame_left, text=f"{label_text} :", font=("arial", 10, "bold"), padx=2, pady=5)
            lbl.grid(row=row, column=0, sticky=W)

            if widget_type == "entry":
                var = StringVar()
                field_vars[label_text] = var
                widget = Entry(data_frame_left, font=("arial", 13, "bold"), width=25,textvariable=var)
                widget.grid(row=row, column=1)
            elif widget_type == "combo":
                var = StringVar()
                field_vars[label_text] = var
                widget = ttk.Combobox(data_frame_left, state="readonly", font=("arial", 11), width=25,textvariable=var)
                widget['value'] = options[0] 
                widget.current(0)
                widget.grid(row=row, column=1)

        fields = [("Further Information","entry"),("Blood Pressure","entry"),("Strong Advise","entry"),("Medication","entry"),("Patient Id","entry"),("NHS Number","entry"),
                   ("Patient Name","entry"),("Date of Birth","entry"),("Patient Address","entry")]
        for row, (label_text, widget_type, *options) in enumerate(fields):
            lbl = Label(data_frame_left, text=f"{label_text} :", font=("arial", 10, "bold"), padx=2, pady=5)
            lbl.grid(row=row, column=2, sticky=W)

            if widget_type == "entry":
                widget = Entry(data_frame_left, font=("arial", 13, "bold"), width=25)
                widget.grid(row=row, column=3)

        self.txt_pres = Text(data_frame_right,bd=2,font=("arial", 12, "bold"),width=45,height=13,padx=2, pady=6)
        self.txt_pres.grid(row=0, column=0)

        btn_pres=Button(button_frame,text="Prescription",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6)
        btn_pres.grid(row=0, column=0)

        btn_pres_data=Button(button_frame,text="Prescription Data",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6,command=self.iPrescriptionData)
        btn_pres_data.grid(row=0, column=1)

        btn_pres_insert=Button(button_frame,text="Insert",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6,command=self.insertPrescriptionData)
        btn_pres_insert.grid(row=0, column=2)

        btn_pres_delete=Button(button_frame,text="Delete",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6)
        btn_pres_delete.grid(row=0, column=3)

        btn_pres_clear=Button(button_frame,text="Clear",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6)
        btn_pres_clear.grid(row=0, column=4)

        btn_pres_exit=Button(button_frame,text="Exit",bg="#90EE90",fg="black",font=("arial", 12, "bold"),width=20,padx=2, pady=6,command=root.quit)
        btn_pres_exit.grid(row=0, column=5)

        #style = ttk.Style()
        #style.configure("Treeview.Heading", font=("arial", 14, "bold"),width=100)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(details_frame,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,show="headings")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        columns = [
            ("nameoftablet", "Name of Tablet"),
            ("ref", "Reference No."),
            ("dose", "Dose"),
            ("nooftablets", "No of Tablets"),
            ("lot", "Lot"),
            ("issuedate", "Issue Date"),
            ("expdate", "Exp Date"),
            ("dailydose", "Daily Dose"),
            ("storage", "Storage"),
            ("nhsnumber", "NHS Number"),
            ("pname", "Patient Name"),
            ("dob", "DOB"),
            ("address", "Address"),
        ]

        for col_name, display_text in columns:
            self.hospital_table.heading(col_name, text=display_text)

        for col_name in self.hospital_table["columns"]:
            self.hospital_table.column(col_name, width=90, stretch=True)


        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill="both", expand=1)

    def iPrescriptionData(self):
        
    #if self.Nameoftablet.get()=="" or self.ref.get()=="":
           # messagebox.showerror("Error","All fields are required")
     

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="archit")
            my_cursor = conn.cursor()

            query = "SELECT * FROM hospital"
            print(f"Executing query: {query}")  # Debugging line to check the query
            my_cursor.execute(query)
            rows = my_cursor.fetchall()


                # Fetch data from the database
            #my_cursor.execute("SELECT * FROM hospital")
            #rows = my_cursor.fetchall()

            print("Fetched rows:", rows)

                # Clear the Treeview before inserting new data
            self.hospital_table.delete(*self.hospital_table.get_children())

                # Insert data into Treeview
            for row in rows:
                self.hospital_table.insert("", "end", values=row)

                # Close the connection
            conn.close()

                # Show success message
            messagebox.showinfo("Success", "Prescription data loaded successfully!")

        except Exception as e:
             messagebox.showerror("Error", f"Error while fetching data: {str(e)}")

    def insertPrescriptionData(self):
        try:
            values = [
                self.field_vars["Name of Tablets"].get(),
                self.field_vars["Reference No"].get(),
                self.field_vars["Dose"].get(),
                self.field_vars["No of Tablets"].get(),
                self.field_vars["Lot"].get(),
                self.field_vars["Issue Date"].get(),
                self.field_vars["Exp Date"].get(),
                self.field_vars["Daily Dose"].get(),
                self.field_vars["Side Effect"].get(),
                self.field_vars["NHS Number"].get(),
                self.field_vars["Patient Name"].get(),
                self.field_vars["Date of Birth"].get(),
                self.field_vars["Patient Address"].get(),
            ]

            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="archit")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(values))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Prescription data inserted successfully!")
            self.iPrescriptionData()  # Refresh the table
        except Exception as e:
            messagebox.showerror("Error", f"Error while inserting data: {str(e)}")

           

'''          
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
            my_cursor=conn.cursor()

            attribute_names=["Name of Tablet","ref","Dose","No of tablets","Lot","Issuedate","Expdate","Dailydose","StorageAdvice","Nhs Number","Patient Name","Date of Birth","Address"]

            values = [getattr(self,attr).get()for attr in attribute_names]

            my_cursor.execute("INSERT INTO hospital VALUES (" + ",".join(["%s"] * len(values)) + ")",tuple(values))

            conn.commit()
            conn.close()
'''


        
                        

root = Tk()
ob = Hospital(root)
root.mainloop()
