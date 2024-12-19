import sqlite3
with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
class Patient:
    def __init__(self):
        pass

    @staticmethod
    def display_patient_info(password):
        cursor.execute(" SELECT * FROM Patient WHERE Password = ?",(password,))
        data = cursor.fetchall()

        return data    # data here is a list of one tupple that contains the info of the specific patient
    
    @staticmethod
    def login(username,password):
        cursor.execute("SELECT Username,Password FROM Users")
        data = cursor.fetchall()
        for usern,pasw in data:
            if (username == usern and password == pasw):
                return True
        return False    
    #  gui
    #  if(login(username,password)) -> now can move to patient page
    #  else -> show message in gui that it is wrong username or password


    @staticmethod
    def create_new_account(fname,lname,email,username,password,phone,birth,gender,height,weight):# I add username that i take from user in gui
        cursor.execute("INSERT INTO Patient (FirstName,LastName,Email,Password,ContactNumber,DateOfBirth,Gender,Height,Weight)VALUES(?,?,?,?,?,?,?,?,?)",(fname,lname,email,password,phone,birth,gender,height,weight))
        patient_id=cursor.lastrowid
        role="patient"
        cursor.execute("INSERT INTO Users (Username,password,Role,Linked_id) VALUES (?,?,?,?)",(username,password,role,patient_id))
        connection.commit()
 
# Patient.create_new_account('noor','ahmed','nourahmed@gmail.com','nourahmed2','no122or','01022471236',25-6-2000,'female',160,59.5) 
# Patient.create_new_account('ahmed','maher','ahmed@gmail.com','ahmedmaher1','ahmed1234','01234713834',12-12-1999,'male',180,78) 
# x = Patient.display_patient_info('no122or')
# print(x)
# y= Patient.display_patient_info('ahmed1234')
# print(y)
# print(Patient.login('nourahmed2','no122or'))
# print(Patient.login('ahmedmaher1','ahmed1234'))
# print(Patient.login('nourahmed2','no12r'))


