import sqlite3
def create_tables():
        conn = sqlite3.connect('MedicalCentre.db')
        cursor = conn.cursor()
        Doctors_Table_Query=('''
        CREATE TABLE IF NOT EXISTS Doctors (
            Doctor_Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,               
            Specialization TEXT NOT NULL,
            Clinic_Id INTEGER NOT NULL,
            FOREIGN KEY (clinic_Id) REFERENCES Clinic(Id) ON DELETE CASCADE
        )
        ''')
        Users_Table_Query=('''
        CREATE TABLE IF NOT EXISTS Users (
            User_Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            User_Name VARCHAR NOT NULL ,        
            PassWord VARCHAR NOT NULL UNIQUE ,
            Clinic_Id INTEGER NOT NULL,
            Linked_ID INTEGER NOT NULL,               
            Role TEXT NOT NULL,
            FOREIGN KEY (Clinic_Id) REFERENCES Clinic(Id) ON DELETE CASCADE
        )
        ''')
        cursor.execute(Doctors_Table_Query)
        cursor.execute(Users_Table_Query)
        conn.commit()
        conn.close()
def get_connection():
    conn = sqlite3.connect('MedicalCentre.db')
    return conn


    
    