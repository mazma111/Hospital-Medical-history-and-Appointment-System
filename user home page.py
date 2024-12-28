import tkinter as tk
from tkinter import PhotoImage

# Function to handle Book Appointment button click
def book_appointment():
    print("Redirecting to appointment booking...")  # Replace with actual functionality

# Function to handle notifications
def view_notifications():
    print("Opening notifications...")  # Replace with actual functionality

# Main Window
root = tk.Tk()
root.title("Medical Management System - Home Page")
root.geometry("900x600")  # Set window size
root.configure(bg="#ffffff")  # White background for the main window

# Colors
header_bg = "#004aad"  # Dark Blue
main_bg = "#ffffff"  # White
accent_bg = "#e0f7fa"  # Light Teal
button_bg = "#007bff"  # Bright Blue
button_fg = "#ffffff"  # White Text

# Header Frame
header_frame = tk.Frame(root, bg=header_bg, height=80)
header_frame.pack(fill="x")

# Logo Placeholder
logo_label = tk.Label(header_frame, text="LOGO", bg="#ffffff", fg=header_bg, font=("Arial", 14, "bold"), width=10, height=2)
logo_label.place(x=20, y=20)
# Uncomment and replace the following line with your logo image:
# logo_img = PhotoImage(file="path/to/your/logo.png")
# logo_label = tk.Label(header_frame, image=logo_img)

# Navigation Buttons
nav_frame = tk.Frame(header_frame, bg=header_bg)
nav_frame.place(x=300, y=20)

home_button = tk.Button(nav_frame, text="Home", font=("Arial", 12), bg=button_bg, fg=button_fg, padx=10, pady=5)
home_button.grid(row=0, column=0, padx=10)

about_button = tk.Button(nav_frame, text="About Us", font=("Arial", 12), bg=button_bg, fg=button_fg, padx=10, pady=5)
about_button.grid(row=0, column=1, padx=10)

contact_button = tk.Button(nav_frame, text="Contact Us", font=("Arial", 12), bg=button_bg, fg=button_fg, padx=10, pady=5)
contact_button.grid(row=0, column=2, padx=10)

# User Controls (Notifications and Profile Photo)
notification_button = tk.Button(header_frame, text="🔔", font=("Arial", 16), bg=header_bg, fg=button_fg, borderwidth=0, command=view_notifications)
notification_button.place(x=750, y=20)

profile_photo_label = tk.Label(header_frame, text="Profile", bg="#ffffff", fg=header_bg, font=("Arial", 12), width=8, height=2)
profile_photo_label.place(x=800, y=20)
# Uncomment and replace the following line with your profile photo:
# profile_img = PhotoImage(file="path/to/profile/photo.png")
# profile_photo_label = tk.Label(header_frame, image=profile_img)

# Welcome Frame
welcome_frame = tk.Frame(root, bg=accent_bg, height=100)
welcome_frame.pack(fill="x", pady=10)

welcome_label = tk.Label(welcome_frame, text="Welcome, [User's Name]!", font=("Arial", 18, "bold"), bg=accent_bg, fg=header_bg)
welcome_label.pack(pady=10)

# Main Content Frame
main_frame = tk.Frame(root, bg=main_bg)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Placeholder for User Information
info_label = tk.Label(main_frame, text="Here you can manage your appointments, view medical history, and more.", 
                      font=("Arial", 14), bg=main_bg, fg=header_bg, wraplength=700, justify="center")
info_label.pack(pady=20)

# Book Appointment Button
book_button = tk.Button(main_frame, text="Book Appointment", font=("Arial", 16), bg=button_bg, fg=button_fg, padx=20, pady=10, command=book_appointment)
book_button.pack(pady=10)

# Footer Frame
footer_frame = tk.Frame(root, bg=header_bg, height=50)
footer_frame.pack(fill="x")

footer_label = tk.Label(footer_frame, text="© 2024 Medical Management System. All Rights Reserved.", font=("Arial", 10), bg=header_bg, fg=button_fg)
footer_label.pack(pady=10)

# Run the main event loop
root.mainloop()
