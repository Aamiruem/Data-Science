create database student;


create table student.academic(
	student_id int,
    firstname varchar(255),
    remarks varchar(255)
    );
    
    insert into student.academic
    values  (1,'A','GOOD'),
			(1,'A','POOR'),
            (2,'B','GOOD'),
            (2,'B','EXCELLENT'),
            (2,'B','GOOD'),
            (3,'C','GOOD');
            
	 SELECT student_id, GROUP_CONCAT( remarks ) as "REMARK", COUNT(*) as 'Number of remarks' 
	 FROM student.academic group by student_id;
     
     SELECT student_id, GROUP_CONCAT( DISTINCT remarks ) as "REMARK",COUNT(*) as 'Number of remarks'
	 FROM student.academic group by student_id;