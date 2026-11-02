CREATE DATABASE companyDB;
USE companyDB;

CREATE TABLE Department (
    Dep_Code INT PRIMARY KEY,
    Dep_Name VARCHAR(20)
);

CREATE TABLE Emp (
    Sr_No INT,
    Emp_Code INT PRIMARY KEY,
    Emp_Name VARCHAR(20),
    Dep_Code INT,
    FOREIGN KEY (Dep_Code) REFERENCES Department(Dep_Code)
);

INSERT INTO Department VALUES
(101, 'IT'),
(102, 'HR'),
(103, 'Sales');

INSERT INTO Emp VALUES
(1, 1001, 'Preet', 101),
(2, 1002, 'Rahul', 102),
(3, 1003, 'Aman', 103);

-- Merge Two Tables
SELECT Emp.Sr_No, Emp.Emp_Code, Emp.Emp_Name,
Department.Dep_Code, Department.Dep_Name
FROM Emp
INNER JOIN Department
ON Emp.Dep_Code = Department.Dep_Code;