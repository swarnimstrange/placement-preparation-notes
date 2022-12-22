<h3> Physical Layer </h3>

- The main functionality of the physical layer is to transmit the individual bits from one node to another node.
- It establishes, maintains and deactivates the physical connection.
- several functions are -:
    - It defines the way how two or more devices can be connected physically.
    - It defines the transmission mode between the two devices on the network.
    - It determines the type of the signal used for transmitting the information.

<h3> Data-Link Layer </h3>

- This layer is responsible for the error-free transfer of data frames.
- It defines the format of the data on the network.

- It contains two sub layer
    - Logical Link Control Layer -: It is responsible for transferring the packets to the Network layer of the receiver that is receiving.
    - Media Access Control Layer -: It is used for transferring the packets over the network. (link btwn physical and logical link layer)

- several functions are -:
    - error control -: If any error seems to occurr, then the receiver sends the acknowledgment for the retransmission of the corrupted frames.
    - flow control -: it is the technique through which the constant data rate is maintained on both the sides so that no data get corrupted.
    - physical addressing: The Data link layer adds a header to the frame that contains a destination address. The frame is transmitted to the destination address mentioned in the header.

<h3> Network Layer </h3>

- It is a layer that manages device addressing, tracks the location of devices on the network.
- it determines the best path to move data from source to the destination based on the network conditions, the priority of service, and other factors.
- Routers are specified in this layer and used to provide the routing services within an internetwork.
- The protocols used to route the network traffic are known as Network layer protocols. Examples of protocols are IP and Ipv6.

- several functions are -:
    - Internetworking -: An internetworking is the main responsibility of the network layer. It provides a logical connection between different devices.
    - Routing.
    - addressing.

<h3> Transport Layer </h3>

- Transport layer ensures that messages are transmitted in the order in which they are sent and there is no duplication of data.
- The main responsibility of the transport layer is to transfer the data completely.
- It receives the data from the upper layer and converts them into smaller units known as segments.
- This layer can be termed as an end-to-end layer as it provides a point-to-point connection between source and destination to deliver the data reliably.

- several functions are -:
    - Segmentation and reassembly
    - Flow control
    - addressing.

