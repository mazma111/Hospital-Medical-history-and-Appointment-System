import tkinter as tk
from tkinter import messagebox

def create_calendar_popup(doctor_name):
    """Creates a popup window with a calendar for booking appointments."""
    popup = tk.Toplevel()
    popup.title("Book Appointment")
    popup.geometry("400x300")
    popup.configure(bg="#f0f8ff")

    # Doctor name label
    doctor_label = tk.Label(popup, text=f"Dr. {doctor_name}", font=("Arial", 14, "bold"), bg="#f0f8ff")
    doctor_label.pack(pady=10)

    # Calendar placeholder
    calendar_label = tk.Label(popup, text="Calendar", font=("Arial", 12, "italic"), bg="#f0f8ff")
    calendar_label.pack(pady=20)

    # Available/Unavailable slots
    slots_frame = tk.Frame(popup, bg="#f0f8ff")
    slots_frame.pack(pady=10)

    # Example time slots
    time_slots = ["10:00 AM", "12:00 PM", "2:00 PM", "4:00 PM"]
    for slot in time_slots:
        btn_color = "green" if "12:00 PM" != slot else "red"  # Mark 12:00 PM as unavailable
        slot_btn = tk.Button(slots_frame, text=slot, bg=btn_color, fg="white", width=10, font=("Arial", 10))
        slot_btn.pack(side=tk.LEFT, padx=5)

    # Confirm booking button
    confirm_btn = tk.Button(popup, text="Confirm", bg="#4682b4", fg="white", font=("Arial", 12), command=lambda: messagebox.showinfo("Booking Confirmed", "Your appointment is booked!"))
    confirm_btn.pack(pady=20)

    popup.mainloop()

def create_doctor_gui():
    """Creates and displays the patient GUI for booking appointments."""

    # Initialize the main window
    root = tk.Tk()
    root.title("Book Appointment Page - Medical Management System")
    root.geometry("800x600")
    root.configure(bg="#f0f8ff")

    # Create a frame for the top navigation bar
    top_frame = tk.Frame(root, bg="#4682b4", height=50)
    top_frame.pack(fill=tk.X)

    # Add a logo placeholder
    logo_placeholder = tk.Label(top_frame, text="LOGO", bg="#4682b4", fg="white", font=("Arial", 16))
    logo_placeholder.pack(side=tk.LEFT, padx=20, pady=10)

    # Add navigation buttons
    nav_buttons = ["Home", "Clinics", "Contact Us"]
    for button in nav_buttons:
        btn = tk.Button(top_frame, text=button, bg="#87cefa", fg="black", font=("Arial", 12), relief="flat")
        btn.pack(side=tk.LEFT, padx=10)

    # Add a notification button (bell icon)
    notification_btn = tk.Button(top_frame, text="\ud83d\udd14", bg="#4682b4", fg="white", font=("Arial", 16), relief="flat")
    notification_btn.pack(side=tk.RIGHT, padx=10)

    # Create a frame for clinic categories
    clinic_frame = tk.Frame(root, bg="#f0f8ff")
    clinic_frame.pack(pady=20)

    clinic_buttons = ["Cardiology", "Neurology", "Dermatology", "Pediatrics"]
    for clinic in clinic_buttons:
        btn = tk.Button(clinic_frame, text=clinic, bg="#87cefa", fg="black", font=("Arial", 12), relief="flat")
        btn.pack(side=tk.LEFT, padx=15)

    # Create doctor frames
    doctor_frame = tk.Frame(root, bg="#f0f8ff")
    doctor_frame.pack(pady=40)

    # List of doctors
    doctors = [
        {"name": "Ahmed", "specialty": "Cardiologist", "price": "100 EGP"},
        {"name": "Sara", "specialty": "Neurologist", "price": "150 EGP"},
        {"name": "Mohamed", "specialty": "Dermatologist", "price": "120 EGP"},
        {"name": "Laila", "specialty": "Pediatrician", "price": "110 EGP"}
    ]

    # Dynamically create doctor frames
    for i, doctor in enumerate(doctors):
        frame = tk.Frame(doctor_frame, bg="#4682b4", width=200, height=300)
        frame.grid(row=i // 2, column=i % 2, padx=20, pady=20)

        doctor_label = tk.Label(frame, text=f"Dr. {doctor['name']}\n{doctor['specialty']}\n{doctor['price']}", fg="white", bg="#4682b4", font=("Arial", 10, "bold"))
        doctor_label.place(x=30, y=20)

        book_button = tk.Button(frame, text='Book', bg="#87cefa", fg="black", font=("Arial", 12), command=lambda doctor_name=doctor['name']: create_calendar_popup(doctor_name))
        book_button.place(x=60, y=200)

    root.mainloop()

create_doctor_gui()
