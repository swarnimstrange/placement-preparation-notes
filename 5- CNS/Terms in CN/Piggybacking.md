<h3> PiggyBacking </h3>

- This technique in which the outgoing acknowledgement is delayed temporarily is called piggybacking.
- Assume that A and B are users. Then the data frames from A to B are interconnected with the acknowledgement from A to B.
- When a data frame arrives, the receiver waits does not send the control frame (acknowledgement) back immediately. The receiver waits until its network layer moves to the next data packet.
- Acknowledgement is associated with this outgoing data frame. Thus the acknowledgement travels along with the next data frame.

<img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20210427232317/pb.png">
