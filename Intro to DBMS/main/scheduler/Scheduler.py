from model.Vaccine import Vaccine
from model.Caregiver import Caregiver
from model.Patient import Patient
from model.Appointment import Appointment
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql
import datetime


'''
objects to keep track of the currently logged-in user
Note: it is always true that at most one of currentCaregiver and currentPatient is not null
        since only one user can be logged-in at a time
'''
current_patient = None

current_caregiver = None


def create_patient(tokens):
    # create_patient <username> <password>
    # check 1: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Failed to create user.")
        return

    username = tokens[1]
    password = tokens[2]

    # check 2: check if the username has been taken already
    if username_exists_patient(username):
        print("Username taken, try again!")
        return

    salt = Util.generate_salt()
    hash = Util.generate_hash(password, salt)

    # create the caregiver
    patient = Patient(username, salt=salt, hash=hash)

    # save to caregiver information to our database
    try:
        patient.save_to_db()
    except pymssql.Error as e:
        print("Failed to create user.")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Failed to create user.")
        print(e)
        return
    print("Created user ", username)

def username_exists_patient(username):
    cm = ConnectionManager()
    conn = cm.create_connection()

    select_username = "SELECT * FROM Patients WHERE Username = %s"
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select_username, username)
        #  returns false if the cursor is not before the first record or if there are no rows in the ResultSet.
        for row in cursor:
            return row['Username'] is not None
    except pymssql.Error as e:
        print("Error occurred when checking username")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Error occurred when checking username")
        print("Error:", e)
    finally:
        cm.close_connection()
    return False


def create_caregiver(tokens):
    # create_caregiver <username> <password>
    # check 1: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Failed to create user.")
        return

    username = tokens[1]
    password = tokens[2]
    # check 2: check if the username has been taken already
    if username_exists_caregiver(username):
        print("Username taken, try again!")
        return

    salt = Util.generate_salt()
    hash = Util.generate_hash(password, salt)

    # create the caregiver
    caregiver = Caregiver(username, salt=salt, hash=hash)

    # save to caregiver information to our database
    try:
        caregiver.save_to_db()
    except pymssql.Error as e:
        print("Failed to create user.")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Failed to create user.")
        print(e)
        return
    print("Created user ", username)


def username_exists_caregiver(username):
    cm = ConnectionManager()
    conn = cm.create_connection()

    select_username = "SELECT * FROM Caregivers WHERE Username = %s"
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select_username, username)
        #  returns false if the cursor is not before the first record or if there are no rows in the ResultSet.
        for row in cursor:
            return row['Username'] is not None
    except pymssql.Error as e:
        print("Error occurred when checking username")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Error occurred when checking username")
        print("Error:", e)
    finally:
        cm.close_connection()
    return False


def login_patient(tokens):
    # login_patient <username> <password>
    # check 1: if someone's already logged-in, they need to log out first
    global current_patient
    if current_caregiver is not None or current_patient is not None:
        print("User already logged in.")
        return

    # check 2: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Login failed.")
        return

    username = tokens[1]
    password = tokens[2]

    patient = None
    try:
        patient = Patient(username, password=password).get()
    except pymssql.Error as e:
        print("Login failed.")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Login failed.")
        print("Error:", e)
        return

    # check if the login was successful
    if patient is None:
        print("Login failed.")
    else:
        print("Logged in as: " + username)
        current_patient = patient


def login_caregiver(tokens):
    # login_caregiver <username> <password>
    # check 1: if someone's already logged-in, they need to log out first
    global current_caregiver
    if current_caregiver is not None or current_patient is not None:
        print("User already logged in.")
        return

    # check 2: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Login failed.")
        return

    username = tokens[1]
    password = tokens[2]

    caregiver = None
    try:
        caregiver = Caregiver(username, password=password).get()
    except pymssql.Error as e:
        print("Login failed.")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Login failed.")
        print("Error:", e)
        return

    # check if the login was successful
    if caregiver is None:
        print("Login failed.")
    else:
        print("Logged in as: " + username)
        current_caregiver = caregiver


def search_caregiver_schedule(tokens):

    global current_caregiver, current_patient
    if current_patient is None and current_caregiver is None:
        print("Please login first!")
        return
    
    if(len(tokens)!=2):
        print("Please try again!")
        return
    
    date = tokens[1]

    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict=True)

    select_date = "Select c.Username as CaregiverUsername, Name as Vaccinename, Doses From Caregivers c, Availabilities a, Vaccines Where c.Username = a.Username AND Time = %s Order by c.Username"

    try:
        cursor.execute(select_date, date)

        for row in cursor:
            print(row['CaregiverUsername'], row['Vaccinename'], row['Doses'])

    except pymssql.Error as e:
        print("Please try again")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Please try again")
        return
    finally:
        cm.close_connection()


def reserve(tokens):
    
    global current_patient, current_caregiver
    if current_patient is None and current_caregiver is None:
        print("Please login first!")
        return
    elif current_patient is None:
        print("Please login as a patient!")
        return
    
    if(len(tokens)!=3):
        print("Please try again!")
        return
    
    date = tokens[1]
    vaccine = tokens[2]

    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict=True)

    available_caregiver = "select TOP 1 c.Username From Caregivers c, Availabilities a Where a.Username = c.Username AND a.Time = %s Order by c.Username"
    available_vaccine = "select Doses From Vaccines Where Name = %s"

    try:
        cursor.execute(available_caregiver, date)
        caregiver_row = cursor.fetchone()

        cursor.execute(available_vaccine, vaccine)
        vaccine_row = cursor.fetchone()

        patient_username  = current_patient.get_username()
        appointment = None

        id = "SELECT a.Appointment_id from Appointment a Where a.Date = %s AND a.patient_username = %s AND a.caregiver_username = %s"

        if vaccine_row is None or vaccine_row['Doses'] == 0:
            print("Not enough available doses!")
        elif caregiver_row is None:
            print("No caregiver is available!")
        else:
            try:
                caregiver_username = caregiver_row['Username']
                appointment = Appointment(date, caregiver_username, patient_username, vaccine)
                appointment.save_to_db()

                cursor.execute(id,(date,patient_username,caregiver_username))
                appointment_id = cursor.fetchone()['Appointment_id']
                print(f"Appointment ID: {appointment_id}, Caregiver username: {caregiver_username}")

                delete_availability = "Delete from Availabilities Where Username = %s AND Time = %s"
                cursor.execute(delete_availability, (caregiver_username, date))
                
                conn.commit()
            except pymssql.Error as e:
                print("Please try again!")
                print(e)
                return
    except pymssql.Error as e:
        print("Please try again!")
        print(e)
        return
    finally:
        cm.close_connection()

def upload_availability(tokens):
    #  upload_availability <date>
    #  check 1: check if the current logged-in user is a caregiver
    global current_caregiver
    if current_caregiver is None:
        print("Please login as a caregiver first!")
        return

    # check 2: the length for tokens need to be exactly 2 to include all information (with the operation name)
    if len(tokens) != 2:
        print("Please try again!")
        return

    date = tokens[1]
    # assume input is hyphenated in the format mm-dd-yyyy
    date_tokens = date.split("-")
    month = int(date_tokens[0])
    day = int(date_tokens[1])
    year = int(date_tokens[2])
    try:
        d = datetime.datetime(year, month, day)
        current_caregiver.upload_availability(d)
    except pymssql.Error as e:
        print("Upload Availability Failed")
        print("Db-Error:", e)
        quit()
    except ValueError:
        print("Please enter a valid date!")
        return
    except Exception as e:
        print("Error occurred when uploading availability")
        print("Error:", e)
        return
    print("Availability uploaded!")


def cancel(tokens):
    
    global current_caregiver, current_patient
    if current_patient is None and current_caregiver is None:
        print("Please login first!")
        return
    
    if len(tokens) != 2:
        print("Please try again!")
        return
    
    id = tokens[1]

    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict=True)

    cancel_appointment = "Delete from Appointment Where Appointment_id = %s"
    cancel_caregiver_date = "Select Date, caregiver_username from Appointment Where Appointment_id = %s"
    Date_update = "INSERT INTO Availabilities Values (%s, %s)"

    try:
        cursor.execute(cancel_caregiver_date, id)
        Cancel_rows = cursor.fetchall()

        if Cancel_rows:
            for row in Cancel_rows:
                Time = row['Date']
                Username = row['caregiver_username']

            cursor.execute(Date_update, (Time, Username))
            cursor.execute(cancel_appointment, id)
            print("Appointment_id: ", id , "has been canceled")
            conn.commit()
        
        else:
            print("No data found for the appointment ID.")
    except pymssql.Error as e:
        print("Please try again!")
        print(e)
        return
    except pymssql.Error as e:
        print("Please try again!")
        print(e)
        return
    finally:
        cm.close_connection()

def add_doses(tokens):
    #  add_doses <vaccine> <number>
    #  check 1: check if the current logged-in user is a caregiver
    global current_caregiver
    if current_caregiver is None:
        print("Please login as a caregiver first!")
        return

    #  check 2: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return

    vaccine_name = tokens[1]
    doses = int(tokens[2])
    vaccine = None
    try:
        vaccine = Vaccine(vaccine_name, doses).get()
    except pymssql.Error as e:
        print("Error occurred when adding doses")
        print("Db-Error:", e)
        quit()
    except Exception as e:
        print("Error occurred when adding doses")
        print("Error:", e)
        return

    # if the vaccine is not found in the database, add a new (vaccine, doses) entry.
    # else, update the existing entry by adding the new doses
    if vaccine is None:
        vaccine = Vaccine(vaccine_name, doses)
        try:
            vaccine.save_to_db()
        except pymssql.Error as e:
            print("Error occurred when adding doses")
            print("Db-Error:", e)
            quit()
        except Exception as e:
            print("Error occurred when adding doses")
            print("Error:", e)
            return
    else:
        # if the vaccine is not null, meaning that the vaccine already exists in our table
        try:
            vaccine.increase_available_doses(doses)
        except pymssql.Error as e:
            print("Error occurred when adding doses")
            print("Db-Error:", e)
            quit()
        except Exception as e:
            print("Error occurred when adding doses")
            print("Error:", e)
            return
    print("Doses updated!")


def show_appointments(tokens):

    global current_caregiver, current_patient
    if current_patient is None and current_caregiver is None:
        print("Please login first!")
        return
    
    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict = True)

    show_caregiver = "Select Appointment_id, vaccine_name, Date, patient_username From Appointment a Where a.caregiver_username = %s Order by Appointment_id"
    show_patient = "Select Appointment_id, vaccine_name, Date, caregiver_username From Appointment a Where a.patient_username = %s Order by Appointment_id"

    try:
        if current_caregiver is not None:
            caregiver_username = current_caregiver.get_username()
            cursor.execute(show_caregiver, caregiver_username)
            for row in cursor:
                print(row['Appointment_id'], row['vaccine_name'], row['Date'], row['patient_username'])

        else:
            patient_username = current_patient.get_username()
            cursor.execute(show_patient, patient_username)
            for row in cursor:
                print(row['Appointment_id'], row['vaccine_name'], row['Date'], row['caregiver_username'])

    except pymssql.Error as e:
        print("Please try again!")
        print("Error", e)
        quit()
    except Exception as e:
        print("Please try again!")
        print("Error", e)
        quit()
    finally:
        cm.close_connection()
    return False




def logout(tokens):
    global current_caregiver, current_patient
    if current_patient is None and current_caregiver is None:
        print("Please login first.")
        return
    elif current_patient is not None or current_caregiver is not None:
        current_caregiver = None
        current_patient = None
        print("Successfully logged out!")
        return
    else:
        print("Please try again!")
        return



def start():
    stop = False
    print()
    print(" *** Please enter one of the following commands *** ")
    print("> create_patient <username> <password>")  # //TODO: implement create_patient (Part 1)
    print("> create_caregiver <username> <password>")
    print("> login_patient <username> <password>")  # // TODO: implement login_patient (Part 1)
    print("> login_caregiver <username> <password>")
    print("> search_caregiver_schedule <date>")  # // TODO: implement search_caregiver_schedule (Part 2)
    print("> reserve <date> <vaccine>")  # // TODO: implement reserve (Part 2)
    print("> upload_availability <date>")
    print("> cancel <appointment_id>")  # // TODO: implement cancel (extra credit)
    print("> add_doses <vaccine> <number>")
    print("> show_appointments")  # // TODO: implement show_appointments (Part 2)
    print("> logout")  # // TODO: implement logout (Part 2)
    print("> Quit")
    print()
    while not stop:
        response = ""
        print("> ", end='')

        try:
            response = str(input())
        except ValueError:
            print("Please try again!")
            break

        response = response.lower()
        tokens = response.split(" ")
        if len(tokens) == 0:
            ValueError("Please try again!")
            continue
        operation = tokens[0]
        if operation == "create_patient":
            create_patient(tokens)
        elif operation == "create_caregiver":
            create_caregiver(tokens)
        elif operation == "login_patient":
            login_patient(tokens)
        elif operation == "login_caregiver":
            login_caregiver(tokens)
        elif operation == "search_caregiver_schedule":
            search_caregiver_schedule(tokens)
        elif operation == "reserve":
            reserve(tokens)
        elif operation == "upload_availability":
            upload_availability(tokens)
        elif operation == "cancel":
            cancel(tokens)
        elif operation == "add_doses":
            add_doses(tokens)
        elif operation == "show_appointments":
            show_appointments(tokens)
        elif operation == "logout":
            logout(tokens)
        elif operation == "quit":
            print("Bye!")
            stop = True
        else:
            print("Invalid operation name!")


if __name__ == "__main__":
    '''
    // pre-define the three types of authorized vaccines
    // note: it's a poor practice to hard-code these values, but we will do this ]
    // for the simplicity of this assignment
    // and then construct a map of vaccineName -> vaccineObject
    '''

    # start command line
    print()
    print("Welcome to the COVID-19 Vaccine Reservation Scheduling Application!")

    start()
