import sqlite3

with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()

    # إنشاء جدول Appointment إذا لم يكن موجودًا
    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointment (
        AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        PatientID INTEGER,
        DoctorID INTEGER,
        DateTime TEXT,
        Status TEXT,
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
        FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
    )''')
    connection.commit()

class Appointment:
    # تمكن المريض من حجز موعد جديد مع الطبيب.
    @staticmethod
    def book_appointment(patient_id, doctor_id, datetime):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Appointment (PatientID, DoctorID, DateTime, Status) VALUES (?, ?, ?, ?)",
                           (patient_id, doctor_id, datetime, 'Booked'))
            connection.commit()
            print("Appointment booked successfully!")
            

    #تتيح للمريض تعديل موعده
    @staticmethod
    def edit_appointment(appointment_id, new_datetime):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE Appointment SET DateTime = ? WHERE AppointmentID = ?", (new_datetime, appointment_id))
            connection.commit()
            print("Appointment updated successfully!")


    #تسمح للمريض بحذف موعده
    @staticmethod
    def delete_appointment(appointment_id):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Appointment WHERE AppointmentID = ?", (appointment_id,))
            connection.commit()
            print("Appointment deleted successfully!")


    #تعرض جميع المواعيد الخاصة بالمريض
    @staticmethod
    def display_appointments_for_patient(patient_id):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE PatientID = ?", (patient_id,))
            appointments = cursor.fetchall()
            if appointments:
                for appointment in appointments:
                    print(f"AppointmentID: {appointment[0]}, DoctorID: {appointment[2]}, DateTime: {appointment[3]}, Status: {appointment[4]}")
            else:
                print("No appointments found.")


    #تعرض جميع المواعيد الخاصة بطبيب معين
    @staticmethod
    def display_appointments_for_doctor(doctor_id):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE DoctorID = ?", (doctor_id,))
            appointments = cursor.fetchall()
            if appointments:
                for appointment in appointments:
                    print(f"AppointmentID: {appointment[0]}, PatientID: {appointment[1]}, DateTime: {appointment[3]}, Status: {appointment[4]}")
            else:
                print("No appointments found.")
                
    
    #ستسمح للطبيب بتحديث الموعد
    @staticmethod
    def update_appointment(appointment_id, doctor_id, new_datetime, new_status):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            
            # التحقق أولاً من حالة الموعد إذا كان الطبيب هو المسؤول عن الموعد
            cursor.execute("SELECT * FROM Appointment WHERE AppointmentID = ? AND DoctorID = ?", (appointment_id, doctor_id))
            appointment = cursor.fetchone()

            if appointment:
                # إذا كان الموعد موجودًا ومرتبطًا بالطبيب، نقوم بتحديثه
                current_status = appointment[4]
                
                if current_status == "Booked":  # السماح بالتحديث فقط إذا كانت الحالة "محجوز"
                    cursor.execute("UPDATE Appointment SET DateTime = ?, Status = ? WHERE AppointmentID = ?", (new_datetime, new_status, appointment_id))
                    connection.commit()
                    print(f"Appointment {appointment_id} updated successfully by doctor {doctor_id}.")
                else:
                    print("Cannot update the appointment because it is already executed or cancelled.")
            else:
                print("This appointment does not belong to the specified doctor.")


# حجز موعد للمريض
Appointment.book_appointment(patient_id=1, doctor_id=2, datetime="2024-12-25 10:00:00")

# تعديل الموعد
Appointment.edit_appointment(appointment_id=1, new_datetime="2024-12-26 12:00:00")


# حذف الموعد
Appointment.delete_appointment(appointment_id=1)


# عرض جميع المواعيد الخاصة بالمريض
Appointment.display_appointments_for_patient(patient_id=1)



# عرض جميع المواعيد الخاصة بالطبيب
Appointment.display_appointments_for_doctor(doctor_id=2)



















import sqlite3

# إنشاء الاتصال بقاعدة البيانات
def create_connection():
    connection = sqlite3.connect("database.db")
    return connection

class Patient:
    def __init__(self):
        pass

    # عرض معلومات المريض بناءً على كلمة المرور
    @staticmethod
    def display_patient_info(password):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Patient WHERE Password = ?", (password,))
        data = cursor.fetchall()
        connection.close()

        return data  # data هنا هي قائمة تحتوي على معلومات المريض

    # تسجيل الدخول باستخدام اسم المستخدم وكلمة المرور
    @staticmethod
    def login(username, password):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT Username, Password, Linked_id, Role FROM Users WHERE Username = ?", (username,))
        data = cursor.fetchall()
        connection.close()

        for usern, pasw, linked_id, role in data:
            if username == usern and password == pasw and role == "patient":
                return linked_id  # إعادة معرّف المريض المرتبط
        return None  # إذا كانت البيانات غير صحيحة

    # إنشاء حساب مريض جديد
    @staticmethod
    def create_new_account(fname, lname, email, username, password, phone, birth, gender, height, weight):
        connection = create_connection()
        cursor = connection.cursor()

        # إضافة المريض إلى جدول Patient
        cursor.execute("INSERT INTO Patient (FirstName, LastName, Email, Password, ContactNumber, DateOfBirth, Gender, Height, Weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (fname, lname, email, password, phone, birth, gender, height, weight))
        patient_id = cursor.lastrowid

        # إضافة المستخدم إلى جدول Users مع ربطه بالمريض
        role = "patient"
        cursor.execute("INSERT INTO Users (Username, Password, Role, Linked_id) VALUES (?, ?, ?, ?)",
                       (username, password, role, patient_id))
        connection.commit()
        connection.close()

        print("Account created successfully!")

# ربط المواعيد
class Appointment:
    # حجز موعد جديد للمريض
    @staticmethod
    def book_appointment(patient_id, doctor_id, datetime):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Appointment (PatientID, DoctorID, DateTime, Status) VALUES (?, ?, ?, ?)",
                       (patient_id, doctor_id, datetime, 'Booked'))
        connection.commit()
        connection.close()
        print("Appointment booked successfully!")

    # تعديل الموعد
    @staticmethod
    def edit_appointment(appointment_id, new_datetime):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE Appointment SET DateTime = ? WHERE AppointmentID = ?", (new_datetime, appointment_id))
        connection.commit()
        connection.close()
        print("Appointment updated successfully!")

    # حذف الموعد
    @staticmethod
    def delete_appointment(appointment_id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Appointment WHERE AppointmentID = ?", (appointment_id,))
        connection.commit()
        connection.close()
        print("Appointment deleted successfully!")

    # عرض المواعيد الخاصة بالمريض
    @staticmethod
    def display_appointments_for_patient(patient_id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE PatientID = ?", (patient_id,))
        appointments = cursor.fetchall()
        connection.close()

        if appointments:
            for appointment in appointments:
                print(f"AppointmentID: {appointment[0]}, DoctorID: {appointment[2]}, DateTime: {appointment[3]}, Status: {appointment[4]}")
        else:
            print("No appointments found.")

    #تعرض جميع المواعيد الخاصة بطبيب معين
    @staticmethod
    def display_appointments_for_doctor(doctor_id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE DoctorID = ?", (doctor_id,))
        appointments = cursor.fetchall()
        connection.close()

        if appointments:
            for appointment in appointments:
                print(f"AppointmentID: {appointment[0]}, PatientID: {appointment[1]}, DateTime: {appointment[3]}, Status: {appointment[4]}")
        else:
            print("No appointments found.")









# # تسجيل الدخول
# patient_id = Patient.login('nourahmed2', 'no122or')

# if patient_id:
#     print("Login successful!")

#     # عرض مواعيد المريض
#     Appointment.display_appointments_for_patient(patient_id)

#     # حجز موعد جديد
#     Appointment.book_appointment(patient_id, doctor_id=1, datetime="2024-12-20 10:00:00")

#     # تعديل موعد
#     Appointment.edit_appointment(appointment_id=1, new_datetime="2024-12-21 10:00:00")

#     # حذف موعد
#     Appointment.delete_appointment(appointment_id=1)
# else:
#     print("Invalid username or password.")
