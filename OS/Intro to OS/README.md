<h3> Operating System </h3>

-> Operating is a software tool which works as a interface between user and the hardware.
-> Designed to be convenient and efficient
-> provides the means for proper use of the resources in the operation of the computer system

<h3> Types of operating systems – </h3>
- <b> Single process operating system. </b>

- <b> Batch-processing operating system. </b> -> similar kinds of job batches are provided to operator ( next job doest'nt get executed until first one is finished. this was used in earlier days of computer system.)

- <b> Multiprogramming operating system. </b> 
  - increases CPU utilization by keeping multiple jobs (code and data) in the memory so that the CPU always has one to execute
  - The idea is to keep multiple jobs in main memory. If one job gets occupied with IO, CPU can be assigned to other job. 

- <b> Multitasking operating system. </b> -> 
  - Multitasking is a logical extension of multiprogramming. CPU executes multiple tasks by switching among them. The switching is very fast. Response time should be minimal. 

<h3> System Call </h3>

-> User programs typically do not have permission to perform operations like accessing I/O devices and communicating other programs.
-> A user program invokes system calls when it requires such services.
-> System calls provide an interface between a program and the operating system. 
-> System calls are of different types. e.g. – fork, exec, getpid, getppid, wait, exit.

<h3> Kernel </h3>

-> A kernel is that part of the operating system which interacts directly with the hardware and performs the most crucial tasks.

<h3> Microkernel </h3>

-> A microkernel is much smaller in size than a conventional kernel and supports only the core operating system functionalities.

<h3> Shell </h3>

-> A shell, also known as a command interpreter, is that part of the operating system that receives commands from the users and gets them executed. 

<h3> Booting </h3>

-> Booting is the process of starting the computer and loading the kernel. 
