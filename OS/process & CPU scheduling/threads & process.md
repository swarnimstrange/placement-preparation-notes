<h3> Processs <h3>

-> A process is a program in execution. 
-> The terms process and job are used interchangeably.
-> For example, a Web Browser is a process, a shell (or command prompt) is a process.

<h3> What are a process and process table?   </h3>

-> any program that is in execution state can be called as process.

-> The operating system is responsible for managing all the processes that are running on a computer and allocates each process a certain amount of time to use the processor and also allocates various resources like memory, disks, etc.

-> To keep track of the state of all the processes, the operating system maintains a table known as the process table. Inside this table, every process is listed along with the resources the process is using and the current state of the process

<h3> What are the different states of the process? </h3>

-> So, basically there are three types of processes Running state, Ready state and waiting state.
-> runnning state is the one which goes into the main memory for execution and they have been permitted by the operating system and they have been given every resource they need.
-> ready state is the state where processes wait to be approved so that they can enter the running state.
-> waiting state is the state where processes are sent by operating system if they need to some task before it's execution like I/O operation.

<h3> What is a Thread? </h3>

-> Thread is a sequential flow of tasks within a process.
-> there can be more than one thread inside a process.Each thread of the same process makes use of a separate program counter and a stack of activation records
-> Thread is often referred to as a lightweight process.
-> For example, in a browser, many tabs can be viewed as threads.

<h3> What are the differences between process and thread? </h3>

-> there can be multiple threads within a process, whereas process is just one.
-> processes have separate address spaces, whereas threads share their address space
-> multiple threads use the same code section, data section, and OS resources but different processes use different cs, ds and os resources.
-> A thread has its own program counter (PC), a register set, and a stack space.
-> threads are easy and quick to make. where making new processes take resources
-> threads are called lightweight processes.