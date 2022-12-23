<h3> Solving Critical Section Problem </h3>

-> for solving critical section problem it should follow 3 criterions
- mutual exclusion -> if one process has entered the critical section then other process cannot enter critical section.
- progress -> only compete between processes that want to use critical section.
- bounded wait -> there should be specific time limit for how much time a process can wait, it shouldn't be like it has been waiting for indefinite amount of time. ( Shouldn't be a problem of Sarvation )

<h3> Semaphore </h3>

- A semaphore is an integer variable that solves the problem of critical section problem and after initialisation, it can be accessed only through two atomic operations called wait() and signal().

- wait() -> if the value of semaphore is more than one then it decreases its values and if it's zero then it gets stuck in a while loop.

<pre>
  wait(s){
        while(s<=0){}
        s--;
    }
</pre>

- signal() -> it increases semaphore value with 1

<pre>
signal(s){
        s++;
    }
</pre>

<h3> Solving CS problem using semaphore </h3>

<pre>
do {
    wait(s);
    // if p1 is there then p2 has to wait
    signal(s);
    // when p1 has finished work p1 will signal that now any process can enter critical section
}(while(true))
</pre>
