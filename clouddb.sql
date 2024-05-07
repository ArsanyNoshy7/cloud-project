create table team(
student_id int primary key,
   name VARCHAR(255) NOT NULL,
   age INT,
   cgpa DECIMAL(3, 2)
);


INSERT INTO team (student_id, name, age, cgpa) VALUES
    (22010116, 'Seif', 20, 3.6),
    (22010252, 'Mariem', 20, 3.6),
    (22010055, 'Alaa', 20, 3.6),
    (22010194, 'Krolos', 20, 3.6),
    (22010046, 'Arsany', 20, 3.6);

 select * from team;
