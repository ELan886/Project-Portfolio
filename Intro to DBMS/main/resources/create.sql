CREATE TABLE Caregivers (
    Username varchar(255),
    Salt BINARY(16),
    Hash BINARY(16),
    PRIMARY KEY (Username)
);

CREATE TABLE Availabilities (
    Time date,
    Username varchar(255) REFERENCES Caregivers,
    PRIMARY KEY (Time, Username)
);

CREATE TABLE Vaccines (
    Name varchar(255),
    Doses int,
    PRIMARY KEY (Name)
);

CREATE TABLE Patients (
    Username varchar(255),
    Salt BINARY(16),
    Hash BINARY(16),
    PRIMARY KEY (Username)
);

CREATE TABLE Appointment (
    Date date,
    caregiver_username varchar(255) REFERENCES Caregivers(Username),
    patient_username varchar(255) REFERENCES Patients(Username),
    vaccine_name varchar(255) REFERENCES Vaccines(Name),
    PRIMARY KEY (caregiver_username, patient_username, vaccine_name, Date)
);