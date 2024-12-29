import tkinter as tk
from tkinter import messagebox, Toplevel

# قائمة مواعيد قابلة للتعديل
appointments = [
    {"name": "Dr. Reem", "specialty": "Cardiologist", "time": "1:00 PM", "price": "100 EGP"},
    {"name": "Dr. Sarah", "specialty": "Dentist", "time": "3:00 PM", "price": "200 EGP"},
]

def create_gradient(canvas, color1, color2):
    """Create a gradient background."""
    steps = 100
    for i in range(steps):
        ratio = i / steps
        r1, g1, b1 = root.winfo_rgb(color1)
        r2, g2, b2 = root.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * ratio) // 256
        g = int(g1 + (g2 - g1) * ratio) // 256
        b = int(b1 + (b2 - b1) * ratio) // 256
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_rectangle(0, i * 6, 800, (i + 1) * 6, outline="", fill=color)

def show_appointments_page():
    """Display the appointments page."""
    clear_right_side()  # Clear the right section to show updated appointments
    tk.Label(canvas, text="Appointments", font=("Arial", 16), bg="#CCE5FF").place(x=300, y=60)

    global appointments  # Use the global appointments list to display it

    y_position = 100
    for appointment in appointments:
        frame = tk.Frame(canvas, bg="white", bd=2, relief="solid")
        frame.place(x=300, y=y_position, width=400, height=150)

        # Appointment details
        tk.Label(frame, text=appointment["name"], font=("Arial", 12), bg="white").pack(pady=5)
        tk.Label(frame, text=appointment["specialty"], font=("Arial", 10), bg="white").pack()
        tk.Label(frame, text=f"Time: {appointment['time']}", font=("Arial", 10), bg="white").pack()
        tk.Label(frame, text=f"Price: {appointment['price']}", font=("Arial", 10), bg="white").pack()

        # Edit and Delete buttons
        button_frame = tk.Frame(frame, bg="white")
        button_frame.pack(side="bottom", pady=10)

        # Edit Button
        edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 10), bg="#CCE5FF", relief="flat", bd=0, command=lambda appointment=appointment: edit_appointment(appointment))
        edit_button.pack(side="left", padx=10)

        # Delete Button
        delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 10), bg="#FFCCCC", relief="flat", bd=0, command=lambda appointment=appointment: delete_appointment(appointment))
        delete_button.pack(side="right", padx=10)

        y_position += 160

def edit_appointment(appointment):
    """Dynamically edit the appointment details."""
    print(f"Editing appointment with Dr. {appointment['name']} ({appointment['specialty']}) at {appointment['time']}")

    edit_popup = Toplevel()
    edit_popup.title("Edit Appointment")
    edit_popup.geometry("300x250")

    tk.Label(edit_popup, text="Edit Appointment", font=("Arial", 14)).pack(pady=10)
    tk.Label(edit_popup, text=f"Doctor: {appointment['name']}").pack()
    tk.Label(edit_popup, text=f"Specialty: {appointment['specialty']}").pack()
    tk.Label(edit_popup, text=f"Time: {appointment['time']}").pack()
    tk.Label(edit_popup, text=f"Price: {appointment['price']}").pack()

    # Add input fields for modification (for example, modify time and price)
    tk.Label(edit_popup, text="New Time:").pack(pady=5)
    new_time_entry = tk.Entry(edit_popup)
    new_time_entry.pack(pady=5)
    new_time_entry.insert(0, appointment['time'])

    tk.Label(edit_popup, text="New Price:").pack(pady=5)
    new_price_entry = tk.Entry(edit_popup)
    new_price_entry.pack(pady=5)
    new_price_entry.insert(0, appointment['price'])

    # Save Button
    save_button = tk.Button(edit_popup, text="Save Changes", bg="#4682b4", fg="white", font=("Arial", 12),
                            command=lambda: save_appointment_changes(appointment, new_time_entry.get(), new_price_entry.get(), edit_popup))
    save_button.pack(pady=10)

    edit_popup.mainloop()

def save_appointment_changes(appointment, new_time, new_price, edit_popup):
    """Save the changes made to the appointment."""
    print(f"Saving changes for Dr. {appointment['name']}: New Time = {new_time}, New Price = {new_price}")

    # Update the appointment details in the list
    appointment["time"] = new_time
    appointment["price"] = new_price

    # Show a confirmation message after saving changes
    confirmation_popup = Toplevel()
    confirmation_popup.title("Changes Saved")
    confirmation_popup.geometry("200x100")
    tk.Label(confirmation_popup, text="Appointment updated successfully!", font=("Arial", 12)).pack(pady=10)

    # Close confirmation popup after a short delay
    confirmation_popup.after(2000, confirmation_popup.destroy)

    # Close the edit popup
    edit_popup.destroy()

    # Refresh the appointments page
    show_appointments_page()

def delete_appointment(appointment):
    """Delete the appointment."""
    global appointments  # Access the global appointments list

    print(f"Deleting appointment with Dr. {appointment['name']} ({appointment['specialty']}) at {appointment['time']}")

    confirmation = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the appointment with Dr. {appointment['name']}?")
    if confirmation:
        appointments = [appt for appt in appointments if appt != appointment]  # Remove the appointment from the list
        print("Appointment deleted.")
        show_appointments_page()  # Update the appointments view

def clear_right_side():
    """Clear all widgets on the right side of the canvas."""
    for widget in canvas.winfo_children():
        if widget.winfo_x() >= 300:
            widget.destroy()

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600")
root.resizable(False, False)

# Create the canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, "#007BFF", "#00BFFF")

# Left-side Profile Section
buttons = [
    ("Appointments", show_appointments_page),
    ("Log Out", lambda: print("Log Out clicked!"))
]

y_position = 180
for text, command in buttons:
    tk.Button(canvas, text=text, font=("Arial", 12), bg="#CCE5FF", relief="flat", bd=4, width=15,
              command=command).place(x=30, y=y_position)
    y_position += 50

# Show initial appointment page
show_appointments_page()

root.mainloop()
