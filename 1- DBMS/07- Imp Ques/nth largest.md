<h1>Find Nth Highest salary of a employee<h1>

<b> formula -: Select salary from employee order by salary desc limit n-1,1 </b>

<b> Select salary from employee order by salary desc limit 1,1 </b>
OR
<b> select salary from employee where salary=(select Max(salary) from employee); </b>

<h1>Find 2nd Highest salary of a employee<h1>

<b> select salary from employee group by salary order by salary desc limit 1,1; </b>
OR
<b>SELECT name, MAX(salary) AS salary FROM employee WHERE salary <> (SELECT MAX(salary) FROM employee); </b>

<h1>Find 3rd Highest salary of a employee<h1>

<b> SELECT salary FROM employee order by salary desc limit 2,1 </b>
OR
<b>SELECT name, MAX(salary) AS salary FROM employee WHERE salary < (SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) FROM employee) ); </b>
