<h3> Bankers Algorithm </h3>

- This algorithm can be used in a bank to ensure that the bank never allocates the available money in a way that it could no longer satisfy the needs of all its clients.

- The banker’s algorithm is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation for predetermined maximum possible amounts of all resources, then makes an “s-state” check to test for possible activities, before deciding whether allocation should be allowed to continue.

- In bankers algorithm, the processes which want to get resources from os have to already define the no of resources they want and currently no of resources they have.

- suppose process one comes in and its already using some resources and demands lots of reources and os doesn't have that many resources avaiable at the moment. And suppose second process comes in and its using several resources and demands fewer one that the os can allocate, so os allocates it the resources and when the process terminates it takes the resouces that were allocated before by os and also the resources that it was already using, and now it can satisfy the need of older process.
