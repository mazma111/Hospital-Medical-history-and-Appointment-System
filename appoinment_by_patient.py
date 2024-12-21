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