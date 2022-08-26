<h3> 1st Normal Form (1NF) </h3>

-> atomicity means values in the table should not be further divided
-> In simple terms, a single cell cannot hold multiple values.
-> Suppose in a table, we can clearly see that the Phone Number column has two values. Thus it violated the 1st NF.

<h3> 2nd Normal Form (2NF) </h3>

-> The first condition in the 2nd NF is that the table has to be in 1st NF. The table also should not contain partial dependency.
-> Here partial dependency means the proper subset of candidate key determines a non-prime attribute.
-> for eg. suppose a table has three columns Emplyoee ID, Department ID and Office.
-> This table has a composite primary key Emplyoee ID, Department ID. The non-key attribute is Office Location.
-> To bring this table to Second Normal Form, we need to break the table into two parts. Emplyoee ID and Department ID in one table and Department ID and Office Location in another table.

<h3> 3rd Normal Form (3NF) </h3>

-> the table has to be in 2NF before proceeding to 3NF
-> The other condition is there should be no transitive dependency for non-prime attributes.
-> That means non-prime attributes (which doesn’t form a candidate key) should not be dependent on other non-prime attributes in a given table.
-> Suppose a table has 5 columns Student ID, Student name, Subject ID, Subject, Address
-> In the above table, Student ID determines Subject ID, and Subject ID determines Subject. This implies that we have a transitive functional dependency, and this structure does not satisfy the third normal form.
->  we need to break the table into two parts. In the first table, columns Student Name, Subject ID and Address are only dependent on Student ID. In the second table, Subject is only dependent on Subject ID.

<h3> Boyce Codd Normal Form (BCNF) </h3>

-> Its the higher version 3NF and was developed by Raymond F. Boyce and Edgar F. Codd.
-> Before proceeding to BCNF the table has to satisfy 3rd Normal Form.
-> In BCNF, if every functional dependency A → B, then A has to be the Super Key of that particular table.
-> Suppose there is a table Student ID, Subject, Professor.
-> As you can see Student ID, and Subject form the primary key, which means the Subject column is a prime attribute. But, there is one more dependency, Professor → Subject.
-> And while Subject is a prime attribute, Professor is a non-prime attribute, which is not allowed by BCNF.
-> Now in order to satisfy the BCNF, we will be dividing the table into two parts. One table will hold Student ID which already exists and newly created column Professor ID.