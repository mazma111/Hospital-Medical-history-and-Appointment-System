import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3

class AdminPage:
    def __init__(self, master, logout_callback):
        self.master = master
        self.logout_callback = logout_callback
        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        ttk.Button(self.frame, text="Add Doctor", command=self.add_doctor).grid(row=0, column=0, pady=5)
        ttk.Button(self.frame, text="Remove Doctor", command=self.remove_doctor).grid(row=1, column=0, pady=5)
        ttk.Button(self.frame, text="Add Clinic", command=self.add_clinic).grid(row=2, column=0, pady=5)
        ttk.Button(self.frame, text="Logout", command=self.logout).grid(row=3, column=0, pady=20)

    def add_doctor(self):
        add_doctor_window = tk.Toplevel(self.master)
        add_doctor_window.title("Add Doctor")
        
        ttk.Label(add_doctor_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        first_name_entry = ttk.Entry(add_doctor_window)
        first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        last_name_entry = ttk.Entry(add_doctor_window)
        last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        email_entry = ttk.Entry(add_doctor_window)
        email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Password:").grid(row=3, column=0, padx=5, pady=5)
        password_entry = ttk.Entry(add_doctor_window, show="*")
        password_entry.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Contact Number:").grid(row=4, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_doctor_window)
        contact_entry.grid(row=4, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Speciality:").grid(row=5, column=0, padx=5, pady=5)
        speciality_entry = ttk.Entry(add_doctor_window)
        speciality_entry.grid(row=5, column=1, padx=5, pady=5)
        
        ttk.Label(add_doctor_window, text="Clinic:").grid(row=6, column=0, padx=5, pady=5)
        clinic_var = tk.StringVar()
        clinic_combobox = ttk.Combobox(add_doctor_window, textvariable=clinic_var)
        clinic_combobox.grid(row=6, column=1, padx=5, pady=5)

        # Populate clinic combobox
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("SELECT ClinicName FROM Clinics")
        clinics = [clinic[0] for clinic in c.fetchall()]
        conn.close()
        clinic_combobox['values'] = clinics
        
        def submit_doctor():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            contact = contact_entry.get()
            speciality = speciality_entry.get()
            clinic = clinic_var.get()
            
            if not all([first_name, last_name, email, password, contact, speciality, clinic]):
                messagebox.showerror("Error", "All fields are required")
                return
            
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            try:
                c.execute('''INSERT INTO Doctors 
                             (FirstName, LastName, Email, Password, ContactNumber, Speciality) 
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                          (first_name, last_name, email, password, contact, speciality))
                doctor_id = c.lastrowid
                
                c.execute("SELECT ClinicID FROM Clinics WHERE ClinicName = ?", (clinic,))
                clinic_id = c.fetchone()[0]
                
                c.execute("INSERT INTO ClinicDoctors (ClinicID, DoctorID) VALUES (?, ?)", (clinic_id, doctor_id))
                
                conn.commit()
                messagebox.showinfo("Success", "Doctor added successfully")
                add_doctor_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already exists")
            finally:
                conn.close()
        
        ttk.Button(add_doctor_window, text="Submit", command=submit_doctor).grid(row=7, column=1, pady=10)

    def remove_doctor(self):
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        
        c.execute("SELECT DoctorID, FirstName, LastName FROM Doctors")
        doctors = c.fetchall()
        
        if not doctors:
            messagebox.showinfo("No Doctors", "There are no doctors to remove")
            conn.close()
            return
        
        doctor_list = [f"{doctor[0]}: {doctor[1]} {doctor[2]}" for doctor in doctors]
        
        selected_doctor = simpledialog.askstring("Remove Doctor", "Select a doctor to remove:", 
                                                 initialvalue=doctor_list[0],
                                                 parent=self.master)
        
        if selected_doctor:
            doctor_id = int(selected_doctor.split(':')[0])
            
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to remove this doctor?")
            if confirm:
                c.execute("DELETE FROM Doctors WHERE DoctorID = ?", (doctor_id,))
                conn.commit()
                messagebox.showinfo("Success", "Doctor removed successfully")
        
        conn.close()

    def add_clinic(self):
        clinic_name = simpledialog.askstring("Add Clinic", "Enter clinic name:", parent=self.master)
        
        if clinic_name:
            conn = sqlite3.connect('hospital.db')
            c = conn.cursor()
            
            try:
                c.execute("INSERT INTO Clinics (ClinicName) VALUES (?)", (clinic_name,))
                conn.commit()
                messagebox.showinfo("Success", "Clinic added successfully")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Clinic name already exists")
            finally:
                conn.close()

    def logout(self):
        self.logout_callback()

    def destroy(self):
        self.frame.destroy()
        
root = tk.Tk()
app = AdminPage(root, " ")
root.mainloop()