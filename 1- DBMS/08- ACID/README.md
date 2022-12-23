<h2> Transaction </h2>

-> A transaction is a single logical unit of work that accesses and possibly modifies the contents of a database.
-> In order to maintain consistency in a database, before and after the transaction, certain properties are followed. These are called ACID properties.

# Atomicity

-> we mean that either the entire transaction takes place at once or doesn’t happen at all.
-> There is no midway i.e. transactions do not occur partially.

# Consistency

-> This means that integrity constraints must be maintained so that the database is consistent before and after the transaction
-> For example if we sent money so our account should lessen that money and account where we send it should update that amount.

# Isolation

-> This property ensures that multiple transactions can occur concurrently without leading to the inconsistency of the database state.
-> one transaction shouldn't get mixed with other transactions

# Durability

-> This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs.
