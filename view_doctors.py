import tkinter as tk

# قائمة الأطباء مع أسمائهم وتخصصاتهم
doctors = [
    {"name": "Dr.Ahmed", "specialty": "Cardiology"},
    {"name": "Dr.Amr", "specialty": "Cardiology"},
    {"name": "Dr.Mona", "specialty": "Neurology"},
    {"name": "Dr.Maha", "specialty": "Neurology"},
    {"name": "Dr.Sara", "specialty": "Dermatology"},
    {"name": "Dr.Omar", "specialty": "Dermatology"},
    {"name": "Dr.Adel", "specialty": "Pediatrics"},
    {"name": "Dr.Hana", "specialty": "Pediatrics"}
]

# إنشاء النافذة الرئيسية مع تحديد الحجم
root = tk.Tk()
root.title("view doctors - Medical Management System")
root.geometry("800x600")
root.configure(bg="#f0f8ff")
top_frame = tk.Frame(root, bg="#4682b4", height=50)
top_frame.pack(fill=tk.X)
logo_placeholder = tk.Label(top_frame, text="LOGO", bg="#4682b4", fg="white", font=("Arial", 16))
logo_placeholder.pack(side=tk.LEFT, padx=20, pady=10)
nav_buttons = ["Home", "Clinics", "contact us"]
for button in nav_buttons:
    btn = tk.Button(top_frame, text=button, bg="#87cefa", fg="black", font=("Arial", 12), relief="flat")
    btn.pack(side=tk.LEFT, padx=10)
notification_btn = tk.Button(top_frame, text="\ud83d\udd14", bg="#4682b4", fg="white", font=("Arial", 16), relief="flat")
notification_btn.pack(side=tk.RIGHT, padx=10) 

# إنشاء إطار لعرض الأطباء
frame = tk.Frame(root)
frame.pack(pady=20)

# دالة لعرض الملف الشخصي للطبيب
def view_profile(doctor_id):
    # هنا يمكنك تنفيذ وظيفة عرض الملف الشخصي للطبيب
    print(f"عرض الملف الشخصي للطبيب {doctor_id}")

# دالة لحذف الطبيب
def delete_doctor(doctor_id):
    # هنا يمكنك تنفيذ وظيفة حذف الطبيب من القائمة أو قاعدة البيانات
    print(f"حذف الطبيب {doctor_id}")

# إنشاء مربعات لعرض كل طبيب
row = 0
col = 0
for doctor in doctors:
    # إنشاء إطار لكل طبيب
    doctor_frame = tk.Frame(frame, padx=40, pady=70, borderwidth=1, relief="solid",bg='#4682b4')
    doctor_frame.grid(row=row, column=col)

    # إضافة اسم الطبيب وتخصصه
    label = tk.Label(doctor_frame, text=f"{doctor['name']}\n{doctor['specialty']}", font=("Helvetica", 12),bg="#4682b4", fg="white")
    label.pack()

    # إضافة زر لعرض الملف الشخصي
    view_button = tk.Button(doctor_frame, text="profile",bg='white')
    view_button.pack(side="left")

    # إضافة زر لحذف الطبيب
    delete_button = tk.Button(doctor_frame, text="delete",bg='red',fg='white')
    delete_button.pack(side="right")

    # الانتقال إلى الصف التالي بعد كل طبيبين
    col += 1
    if col == 4:
        row += 1
        col = 0

# إضافة زر لإضافة طبيب جديد
add_button = tk.Button(root, text=" Add doctor", font=("Helvetica", 12),bg="#4682b4",fg='white')
add_button.pack()

root.mainloop()