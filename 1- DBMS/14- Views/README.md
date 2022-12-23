<h2>Views</h2>

-> Views in SQL are considered as a virtual table.
-> To create the view, we can select the fields from single or multiple tables present in the database.
-> A view can either have specific rows based on certain condition or all the rows of a table.

-> Deleting a row from a view deletes the row from the table on which the view was created.

# Advantages

-> Views are used to only display the required data to the users by keeping sensitive data safe.
-> it simplifies the complexity of the query.

# Creating view from single table

CREATE VIEW view_name AS  
SELECT column1, column2.....  
FROM table_name  
WHERE condition;

# Creating view from multiple table

CREATE VIEW MarksView AS  
SELECT Student_Detail.NAME, Student_Detail.ADDRESS, Student_Marks.MARKS  
FROM Student_Detail, Student_Mark  
WHERE Student_Detail.NAME = Student_Marks.NAME;

# Deleting View

DROP VIEW view_name;
