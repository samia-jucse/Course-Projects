CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- Create Doctors Table
CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create Patients Table
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Phone VARCHAR(15) NOT NULL
);

-- Create Appointments Table
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(50) NOT NULL,
    DoctorID INT,
    PatientID INT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);
INSERT INTO Departments (DepartmentID, Name, Location)
VALUES (1, 'Cardiology', 'First Floor'),
       (2, 'Neurology', 'Second Floor'),
       (3, 'Orthopedics', 'Third Floor'),
       (4, 'Dermatology', 'Fourth Floor'),
       (5, 'Pediatrics', 'Fifth Floor');
INSERT INTO Doctors (DoctorID, Name, Specialization, Phone, DepartmentID)
VALUES (1, 'Dr. John Smith', 'Cardiologist', '1234567890', 1),
       (2, 'Dr. Emma Johnson', 'Neurologist', '9876543210', 2),
       (3, 'Dr. David Williams', 'Orthopedic', '5556667777', 3),
       (4, 'Dr. Olivia Brown', 'Dermatologist', '8889990000', 4),
       (5, 'Dr. Liam Garcia', 'Pediatrician', '4443332222', 5);
INSERT INTO Patients (PatientID, Name, Age, Gender, Phone)
VALUES (1, 'Alice Green', 30, 'Female', '1112223333'),
       (2, 'Bob White', 45, 'Male', '2223334444'),
       (3, 'Charlie Black', 25, 'Male', '3334445555'),
       (4, 'Diana Blue', 35, 'Female', '4445556666'),
       (5, 'Evan Gray', 28, 'Male', '5556667777');
INSERT INTO Appointments (AppointmentID, Date, Time, Status, DoctorID, PatientID)
VALUES (1, '2024-12-20', '09:00:00', 'Confirmed', 1, 1),
       (2, '2024-12-21', '10:30:00', 'Pending', 2, 2),
       (3, '2024-12-22', '11:00:00', 'Cancelled', 3, 3),
       (4, '2024-12-23', '12:15:00', 'Confirmed', 4, 4),
       (5, '2024-12-24', '14:00:00', 'Pending', 5, 5);
