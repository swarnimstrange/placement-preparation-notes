<h3> Race Condition </h3>

- there is a condition that occurs when multiple processes are using or sharing same resources. this lead to irrelevant modificaion or deadlock of proocesses.

- that's why we use process synchrniation to handle the race condition.

<h3> Critical Section Problem </h3>

- there are n processes, viz. P0, P1, P2 … Pn-1
- each process has a section of code, called the critical section, in which the process changes 
common variables and files
- the problem is to ensure that when one process is executing in its critical section then no other process can execute its own critical section.(if one process is executing within critical section so no other problem can enter the critical section )

<h3> Producer Consumer Problem </h3>

- this problem arises when the speed of producing of producer is more than speed of consuming of consumer or the speed of consuming of consumer is more than speed of producing of producer.

<h3> Reader Writer Problem </h3>

- suppose there is a shared resource for example notice paper. So, multiple readers can read (access) the resource at same time but a writer and a reader cannot access the shared resource as it can happen that suppose reader is reading the notice and he is on 5th line but then after writer came and made a change at 2nd line so this can cause problem.

- two writer also cannot access the resource at same time.

<h3> Dining Philosopher Problem </h3>

- suppose there is a round table and 5 person (process) are there and in between thare is a rice bowl. these persons can either think or eat at the one time and there are 2 spoons in each process side. but suppose they all are hungry at the same time so they can't eat all at a time because if the person 1 takes 2 spoon of it's side then person 2 cannot take one spoonso he has to wait.

- so only two person can eat at one time out of 5 processes.

<pre> 
                          p2  
                      -       -
                  -              p3 
               p1         R           -
                  -               p4
                      -        -
                          p5
</pre>
