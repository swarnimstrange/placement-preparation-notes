<h3> Deadlock </h3>

- Deadlock is a situation where a set of processes are are blocked because each process is holding a resource and waiting for some other resource aquired by another process.

- for eg 

              r1
        (A) /    \ (D)
           p1     p2
        (D) \   / (A)
              r2

- A represents allocated and D represents Demanding. So, p1 process has r1 resource allocated but it's demanding for another resource r2 and r2 is allocated to p2 and its demanding resource r1. No process is ready to leave a resource this causes Deadlock problem.


<h3> Necessary conditions for deadlocks </h3>

- Mutual exclusion -> one or more non-sharable resources 
- Hold and wait -> a process is holding some resources and waiting for other resources. 
- No preemption -> a resource cannot be taken from a process unless the process releases that resource itself.
- Circular wait -> a set {P0, P1, P2 … Pn} exist such that P0 is waiting for resources held by P1, P1 is waiting for resources held by P2, and so on, and Pn is waiting for resources held by P0.

<h3> How to recover from a deadlock? </h3>

- We can recover from a deadlock by following methods:

- Process termination
  - Abort all the deadlock processes
  - Abort one process at a time until the deadlock is eliminated

- Resource preemption
  - Rollback 
  - Selecting a victim
