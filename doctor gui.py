import tkinter as tk
from PIL import ImageTk, Image

def create_doctor_gui():
  """Creates and displays the admin GUI."""

  # Initialize the main window
  root = tk.Tk()
  root.title("Doctor Page - Medical Management System")
  root.geometry("800x600")
  root.configure(bg="#f0f8ff")  # Light blue background

  # Create a frame for the top navigation bar
  top_frame = tk.Frame(root, bg="#4682b4", height=50)
  top_frame.pack(fill=tk.X)

  # Add a logo placeholder
  logo_placeholder = tk.Label(top_frame, text="LOGO", bg="#4682b4", fg="white", font=("Arial", 16))
  logo_placeholder.pack(side=tk.LEFT, padx=20, pady=10)

  #frames
  left_frame = tk.Frame(root)
  left_frame.pack(side="left", fill="both", expand=True)
  right_frame = tk.Frame(root)
  right_frame.pack(side="right", fill="both", expand=True)

  # Add navigation buttons
  nav_buttons = ["Home", "Clinics", "Patients"]
  for button in nav_buttons:
    btn = tk.Button(top_frame, text=button, bg="#87cefa", fg="black", font=("Arial", 12), relief="flat")
    btn.pack(side=tk.LEFT, padx=10)

  # Add a notification button (bell icon)
  notification_btn = tk.Button(top_frame, text="\ud83d\udd14", bg="#4682b4", fg="white", font=("Arial", 16), relief="flat")
  notification_btn.pack(side=tk.RIGHT, padx=10)
  # Add a welcome message
  welcome_label = tk.Label(left_frame, text="Welcome, Doctor!",fg="#4682b4", font=("Arial", 20, "bold"))
  #welcome_label.pack(pady=20)
  welcome_label.place(x=100, y=250)

  

  # Add a hospital photo placeholder (replace with your hospital image)
 
  #img = Image.open("C:/Users/dd/OneDrive/Desktop/programming/python/gui/doctor.jpeg")
  img = Image.open("C:/Users/dd/OneDrive/Desktop/programming/python/gui/Functional.png")
  
  new_img = img.resize((400, 590))

    # حفظ الصورة المعدلة (اختياري)
  #new_img.save("C:/Users/dd/OneDrive/Desktop/programming/python/gui/doctor_resized.jpeg")
  new_img.save("C:/Users/dd/OneDrive/Desktop/programming/python/gui/Functional.png")

    # تحويل الصورة إلى PhotoImage وعرضها
  photo = ImageTk.PhotoImage(new_img)
  hospital_image = tk.Label(right_frame, image=photo, bg="#f0f8ff")
  hospital_image.pack(side=tk.RIGHT, padx=0, pady=0, anchor=tk.CENTER)
  hospital_image.place(x=20, y=0)

  

  # Run the main event loop
  root.mainloop()

# Call the function to create the admin GUI
create_doctor_gui()