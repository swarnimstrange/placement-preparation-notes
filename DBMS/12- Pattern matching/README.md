<h2>Pattern Matching</h2>

-> LIKE clause is used to perform the pattern matching task in SQL.
-> A WHERE clause is generally preceded by a LIKE clause in an SQL query.
-> % represents one or more than one character.
-> \_ represents one character only.

# Write a query to display employee details in which name starts with 'Pr'.

<b> SELECT \* FROM employee_details WHERE Name LIKE 'Pr%'; </b>

# Write a query to display employee details in which name starts with 'P' and contains only 2 digits after it.

<b> SELECT \* FROM employee_details WHERE Name LIKE 'P\_\_'; </b>
