<h1>Types of Joins in SQL<h1>

<h3> 1 Inner Join </h3>

-> The inner join is used to select all matching rows or columns in both tables or as long as the defined condition is valid in SQL.

-> for example ( Select Student_ID, StudentName, TeacherName, TeacherEmail FROM Students INNER JOIN Teachers ON Students.TeacherID = Teachers.TeacherID; )

<h3> 3 Left Join </h3>

-> The LEFT JOIN is used to retrieve all records from the left table (table1) and the matched rows or columns from the right table (table2).

-> for example ( Select ID, ProductName, CustomerName, CustomerAddress, Amount FROM Product_Details LEFT JOIN Customer_Details ON Product_Details.ID = Customer_Details.ProductID; )

<h3> 4 Right Join </h3>

-> The RIGHT JOIN is used to retrieve all records from the right table (table2) and the matched rows or columns from the left table (table1).

-> for example ( Select ID, ProductName, CustomerName, CustomerAddress, Amount FROM Product_Details RIGHT JOIN Customer_Details ON Product_Details.ID = Customer_Details.ProductID; )

<h3> 2 Full Outer Join </h3>

-> It is a combination result set of both LEFT JOIN and RIGHT JOIN. The joined tables return all records from both the tables

-> for example ( Select column_1, column_2, column(s) FROM table_1 FULL OUTER JOIN table_2 ON table_1.column_name = table_2.column_name; )

<h3> 5 Self Join </h3>

-> It is a SELF JOIN used to create a table by joining itself as there were two tables. It makes temporary naming of at least one table in an SQL statement.

-> Select TB.ID, TB.ProductName FROM Product_Details TB, Product_Details TB2 WHERE TB.AMOUNT < TB2.AMOUNT;

<h3> 6 Cross Join </h3>

-> The CROSS JOIN produces a table that merges each row from the first table with each second table row. It is not required to include any condition in CROSS JOIN.

-> for example ( Select * from table_1 cross join table_2; )
