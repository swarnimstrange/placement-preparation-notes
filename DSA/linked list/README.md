<h3> Linked List </h3>

-> A linked list is a linear data structure, in which the elements are not stored at contiguous(adjacent) memory locations.

-> Nodes are the building blocks of Linked List where the first node is Head node and if it has no value then it is assigned as null.

-> Each node in a list consists of at least two parts:
<ul>
<li> Data in node </li>
<li> Reference to the next node </li>
</ul>

-> Suppose we made our first node as head so the reference of head would be on the first node and the next reference of node would be empty because there is no next node created yet.
  
    llist.head                 
        |      
        |      
    +----+------+ 
    | 1 | None |  
    +----+------+ 

-> Now we want to add a new node to the the Linked List. So, what we will do is we will reference it to the next node and save it's data.

    llist.head      head.next       
        |             |       
        |             |       
    +----+------+     +----+------+  
    | 1 | o-------->| 2 | null |     
    +----+------+     +----+------+  
