<h3> long-term scheduler (job scheduler) </h3>

- it takes the processes from creation state and put it into ready state to be executed.
- more formally, it selects processes from those submitted by the user and loads them into the memory.

<h3> short-term scheduler (CPU scheduler) </h3>

- it takes the program from ready state and puts it to the running state using some scheduling algorithms.
- more formally, it selects one of the processes in the memory and allocates the CPU to it.

<h3> middle-term scheduler </h3>

- if any process requires to do some I/O operation during its running state then mts removes that process from running state to waiting state.
- removes processes from the memory and from the competition for the CPU, thus reducing the degree of multiprogramming.

<h3> What is the zombie process? </h3>

- A process that has finished the execution but still has an entry in the process table to report to its parent process is known as a zombie process.

- The parent process reads the exit status of the child process which reaps off the child process entry from the process table.

<h3> What are orphan processes? </h3>

- A process whose parent process no more exists i.e. either finished or terminated without waiting for its child process to terminate is called an orphan process.
