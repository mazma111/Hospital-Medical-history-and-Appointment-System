import sqlite3

def create_tables():

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Patient table

        patient_table_query = """ CREATE TABLE IF NOT EXISTS Patient (
        PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email TEXT NOT  NULL,
        Password TEXT NOT NULL,
        ContactNumber TEXT NOT NULL,
        DateOfBirth DATE,
        Gender TEXT NOT NULL,
        Height REAL,
        Weight REAL
        )                                           
        """ 


     
        # users table 
        users_table_query = """ CREATE TABLE IF NOT EXISTS users(
        UserID  INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL,
        Role TEXT NOT NULL CHECK (role IN ('doctor', 'patient', 'admin')),
        Linked_id INTEGER ,
        FOREIGN KEY (linked_id) REFERENCES Doctor(DoctorID) ON DELETE SET NULL,
        FOREIGN KEY (linked_id) REFERENCES Patient(PatientID) ON DELETE SET NULL,
        FOREIGN KEY (linked_id) REFERENCES Admin(AdminID) ON DELETE SET NULL
        )
        """
        
      

        cursor.execute(patient_table_query) 
        cursor.execute(users_table_query)
        
        connection.commit()
        connection.close()
create_tables()        


