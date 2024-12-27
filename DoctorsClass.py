import DataBase as db
import sqlite3
class Doctor:
    @staticmethod
    def LogIn(UserName,PassWord):
        try: 
           conn = db.get_connection()
           cursor = conn.cursor()

           Doctor_LogIn_Query=('''
           SELECT User_Name,PassWord FROM Users WHERE  User_Name=? AND PassWord=?''')
           cursor.execute(Doctor_LogIn_Query,(UserName,PassWord)) 
         #   conn.commit() SELECT doesn't need commit 
           result=cursor.fetchone()

           if result:
             return True
           else:
            return False
        except Exception as e:
           print("Error during Log In!!!",e)
           return False
        finally:
         conn.close()
    @staticmethod
    def add_user(username, password, clinic_id, role,linked_id):
       try:
          con= db.get_connection()
          cursor = con.cursor()   
          add_user_Query=('''
           INSERT INTO Users (User_Name, PassWord, Clinic_Id, Role, Linked_ID)
           VALUES(?,?,?,?,?)
            ''')
            
          cursor.execute(add_user_Query,(username, password, clinic_id, role,linked_id))
          con.commit()
          return True
        

       except sqlite3.IntegrityError:
           print("Error: User already exists!")
           return False
       

       except Exception as e:
            print("Error while adding user:", e)
            return False
          
       finally:
          con.close() 
    @staticmethod      
    def delete_all():
       con= db.get_connection()
       cursor = con.cursor()
       cursor.execute("DELETE FROM Users")
       con.commit()
       con.close() 
       
    @staticmethod
    def display_doctor_info(FirstName,LastName):
      try:
         conn = db.get_connection()
         conn.row_factory = sqlite3.Row #deals as a dictionary
         cursor = conn.cursor()

         Doctor_Info_Query=(''' 
         SELECT First_Name,Last_Name,Specialization FROM Doctors WHERE First_Name=? AND Last_Name=?''' )
         cursor.execute( Doctor_Info_Query,(FirstName,LastName))
         #   conn.commit() SELECT doesn't need commit 
         result=cursor.fetchone()
         if result:

            print("Doctor Info is: ")
            for key in result.keys():
               print(f"{key}: {result[key]}")
            return dict(result) # convert result  into dictionary
         else:
            print("No doctor found with the provided information.")
            return None
      except Exception as e:
           print("Error during display doctor data!!!",e)
           return None
      finally:
         conn.close()


    def get_medical_records(patient_id):
      try:
        
        conn = db.get_connection()
        conn.row_factory = sqlite3.Row  # عرض النتائج كمصفوفة مفاتيح (Dictionary)
        cursor = conn.cursor()

        query = '''
        SELECT MedicalRecordID, RecordDate, MainDiagnosis, Prescription, Cured, DoctorNotes
        FROM MedicalRecords
        INNER JOIN Appointments ON MedicalRecords.AppointmentID = Appointments.AppointmentID
        WHERE Appointments.PatientID = ?
        '''
        cursor.execute(query, (patient_id,)) 

        
        records = cursor.fetchall()

        if not records:
            print("No medical records found for this patient.")
            return None

        print("Medical Records for Patient ID:", patient_id)
        for record in records:
            print(dict(record)) 

        return records  
      except Exception as e:
        print("Error retrieving medical records:", e)
        return None

      finally:
        conn.close()
    



         





           

         

db.create_tables()# creating tables one time in this file only not another 
# Doctor.delete_all()
# add_users_result=Doctor.add_user("Roba","2385","8","doctor","3")
# if add_users_result:
#     print("Done!....Your account created successfully!")
# else:
#     print("Sorry!! Data isn't inserted!!")
     
# UserName=input("User Name: ").strip()
# PassWord=input("Password: ").strip()
# Doctor.LogIn(UserName,PassWord)  
# if Doctor.LogIn(UserName, PassWord):
#    print("Logged in successfully!")
# else:
#    print("Failed!!check your entered information please!")
# add_users_result=Doctor.add_user("Roba","2385","8","doctor","3")       
# if add_users_result:
#     print("Done!....Your account created successfully!")
# else:
#     print("Sorry!! Data isn't inserted!")     
# result=Doctor.display_doctor_info("Ahmed","Waleed")
# if result:
#     print("Doctor Data Retrieved Successfully!")
# else:
#     print("Doctor not found!")

patient_id = 101 
records = Doctor.get_medical_records(patient_id)

if records:
    print("Records Retrieved Successfully!")
else:
    print("No records found or an error occurred.")
