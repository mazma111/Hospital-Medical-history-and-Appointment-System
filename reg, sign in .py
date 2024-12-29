import tkinter as tk  
from tkinter import messagebox  
from classes import *

# Main GUI Class  
class MedicalManagementSystem:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Medical Management System")  
        self.root.geometry("800x500")  
        self.root.configure(bg="white")  
        self.current_frame = None  

        # Display Register Page First  
        self.show_register_page()  

    def clear_frame(self):  
        """Destroy any current frame to replace with a new one."""  
        if self.current_frame:  
            self.current_frame.destroy()  

    # Register Page for Users Only  
    def show_register_page(self):  
        self.clear_frame()  
        self.current_frame = tk.Frame(self.root, bg="white", bd=2, relief="ridge")  
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=500)  

        # Title  
        title = tk.Label(self.current_frame, text="Create Account", font=("Helvetica", 18, "bold"), bg="white", fg="#4682B4")  
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Input Fields  
        fields = ["First Name", "Last Name", "Email","Username", "Password", "Confirm Password", "Phone", "Birth Date", "Gender", "Height", "Weight"]  
        self.entries = {}  

        for index, field in enumerate(fields):  
            lbl = tk.Label(self.current_frame, text=f"{field}:", font=("Helvetica", 12), bg="white")  
            lbl.grid(row=index + 1, column=0, sticky="w", padx=20, pady=2)
            entry = tk.Entry(self.current_frame, font=("Arial", 12), bg="#F0F8FF", relief="groove",  
                             show="*" if "Password" in field else "")  
            entry.grid(row=index + 1, column=1, padx=20, pady=5, sticky="ew")
            entry.config(highlightbackground="#87CEFA", highlightthickness=1, bd=0)  
            self.entries[field] = entry  

            # Bind Enter key to move to the next field  
            entry.bind("<Return>", lambda event, idx=index: self.focus_next_field(idx))  

        # Register Button  
        register_btn = tk.Button(self.current_frame, text="Register", font=("Helvetica", 14, "bold"), bg="#4682B4", fg="white",  
                                 activebackground="#5A9BD3", relief="flat", cursor="hand2",  
                                 command=self.register_user)  
        register_btn.grid(row=len(fields) + 1, column=0, columnspan=2, pady=15)

        # Sign In Link  
        signin_btn = tk.Button(self.current_frame, text="Already have an account? Sign In", font=("Helvetica", 10, "underline"),  
                               bg="white", fg="#4682B4", cursor="hand2", relief="flat",  
                               command=self.show_signin_page)  
        signin_btn.grid(row=len(fields) + 2, column=0, columnspan=2)

    def focus_next_field(self, index):  
        """Focus on the next entry field based on the current index."""  
        if index + 1 < len(self.entries):  # Check if there is a next field  
            next_field = list(self.entries.values())[index + 1]  
            next_field.focus_set()  

    def register_user(self):  
        """Register user details."""  
        first_name = self.entries["First Name"].get()  
        last_name = self.entries["Last Name"].get()  
        email = self.entries["Email"].get()  
        password = self.entries["Password"].get()  
        confirm_password = self.entries["Confirm Password"].get()  
        username = self.entries["Username"].get()
        phone = self.entries["Phone"].get()
        birth = self.entries["Birth Date"].get()
        gender = self.entries["Gender"].get()
        height = self.entries["Height"].get()
        weight = self.entries["Weight"].get() 

        if not all([first_name, last_name, email, password, confirm_password,phone,birth,gender,height,weight]):  
            messagebox.showerror("Error", "All fields are required!")  
        elif password != confirm_password:  
            messagebox.showerror("Error", "Passwords do not match!")  
        else:  
            Patient.create_new_account(first_name, last_name, email, username, password, phone, birth, gender, height, weight)
            messagebox.showinfo("Success", "Registration Successful!")  
            self.show_signin_page()  

    # Sign-In Page for All Roles  
    def show_signin_page(self):  
        self.clear_frame()  
        self.current_frame = tk.Frame(self.root, bg="white", bd=2, relief="ridge")  
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=450)  

        # Title  
        title = tk.Label(self.current_frame, text="Sign In", font=("Helvetica", 18, "bold"), bg="white", fg="#4682B4")  
        title.pack(pady=10)  

        # Role Selector  
        lbl_role = tk.Label(self.current_frame, text="Select Role:", font=("Helvetica", 12), bg="white")  
        lbl_role.pack(anchor="w", padx=20, pady=5)  

        self.role_var = tk.StringVar(value="User")  
        role_frame = tk.Frame(self.current_frame, bg="white")  
        role_frame.pack(pady=5)  

        roles = ["User", "Doctor", "Admin"]  
        for role in roles:  
            btn = tk.Button(role_frame, text=role, font=("Helvetica", 12, "bold"), width=10,  
                            bg="#E0F7FF", fg="black", relief="flat", bd=0,  
                            activebackground="#ADD8E6", cursor="hand2",  
                            command=lambda r=role: self.role_var.set(r))  
            btn.pack(side="left", padx=5)  

        # Email and Password Fields  
        lbl_email = tk.Label(self.current_frame, text="Email:", font=("Helvetica", 12), bg="white")  
        lbl_email.pack(anchor="w", padx=20, pady=2)  
        self.email_entry = tk.Entry(self.current_frame, font=("Arial", 12), bg="#F0F8FF")  
        self.email_entry.pack(fill="x", padx=20, pady=5)  
        self.email_entry.bind("<Return>", lambda event: self.password_entry.focus_set())  # Focus on password entry  

        lbl_password = tk.Label(self.current_frame, text="Password:", font=("Helvetica", 12), bg="white")  
        lbl_password.pack(anchor="w", padx=20, pady=2)  
        self.password_entry = tk.Entry(self.current_frame, font=("Arial", 12), bg="#F0F8FF", show="*")  
        self.password_entry.pack(fill="x", padx=20, pady=5)  

        # Sign-In Button  
        signin_btn = tk.Button(self.current_frame, text="Sign In", font=("Helvetica", 14, "bold"), bg="#4682B4", fg="white",  
                               relief="flat", activebackground="#5A9BD3", cursor="hand2",  
                               command=self.signin_user)  
        signin_btn.pack(pady=20)  

        # Register Link  
        register_btn = tk.Button(self.current_frame, text="Don't have an account? Register", font=("Helvetica", 10, "underline"),  
                                 bg="white", fg="#468                                  2B4", cursor="hand2", relief="flat",  
                                 command=self.show_register_page)  
        register_btn.pack()  

    def signin_user(self):  
        """Sign-In action handler."""  
        role = self.role_var.get()  
        email = self.email_entry.get()  
        password = self.password_entry.get()  

        if not email or not password:  
            messagebox.showerror("Error", "Please enter email and password.")  
        else:  
            messagebox.showinfo("Success", f"Welcome {role}! You have signed in successfully.")  

# Main Application Execution  
if __name__ == "__main__":  
    root = tk.Tk()  
    app = MedicalManagementSystem(root)  
    root.mainloop()
