import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql

class Appointment:
    def __init__(self, Date, caregiver_username, patient_username, vaccine_name):
        self.Date = Date
        self.caregiver_username = caregiver_username
        self.patient_username = patient_username
        self.vaccine_name = vaccine_name
    
    def get_appointment_date(self):
        return self.Date
    
    def get_appointment_caregiver(self):
        return self.caregiver_username
    
    def get_appointment_patient(self):
        return self.patient_username
    
    def get_appointment_vaccine(self):
        return self.vaccine_name
    
    def save_to_db(self):

        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        add_patients = "INSERT INTO Appointment (Date, caregiver_username, patient_username, vaccine_name) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(add_patients, (self.Date, self.caregiver_username, self.patient_username, self.vaccine_name))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            raise
        finally:
            cm.close_connection()
