-- Question 1 Create the 'student' table
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- Question 2 Insert at least 3 records into the 'student' table
INSERT INTO student (id, fullName, age)
VALUES (1, 'Student One', 18);

INSERT INTO student (id, fullName, age)
VALUES (2, 'Student Two', 19);

INSERT INTO student (id, fullName, age)
VALUES (3, 'Student Three', 21);

-- Question 3 Update the age of the student with ID = 2
UPDATE student
SET age = 20
WHERE id = 2;
