<h3> Subnet Mask </h3>

- It stands for Transmission Control Protocol/Internet Protocol.
- The TCP/IP model is a concise version of the OSI model
- It contains four layers
    - Application Layer
    - Transport Layer
    - Internet Layer
    - Network Access Layer

<h3> Network Access Layer </h3>

- This layer corresponds to the combination of Data Link Layer and Physical Layer of the OSI model.
- The protocols present in this layer allows for the physical transmission of data.

<h3> Internet Layer </h3>

- This layer parallels the functions of OSI’s Network layer.
- It defines the protocols which are responsible for logical transmission of data over the entire network.
- The main protocols residing at this layer are -:
    - IP (Internet Protocol) -: Delivering packets from the source host to the destination host by looking at the IP addresses in the packet headers.
    - ICMP (Internet Control Message Protocol) -: responsible for providing hosts with information about network problems.
    - ARP (Address Resolution Protocol) -: Its job is to find the hardware address of a host from a known IP address. (ARP has several types: Reverse ARP, Proxy ARP, Gratuitous ARP and Inverse ARP.)

<h3> Host-to-Host Layer </h3>

- This layer is analogous to the transport layer of the OSI model.
- It is responsible for end-to-end communication and error-free delivery of data.
- The two main protocols present in this layer are -:
    - TCP (Transmission Control Protocol) -: It is known to provide reliable and error-free communication between end systems. It performs sequencing and segmentation of data. It also has acknowledgment feature and controls the flow of the data through flow control mechanism. 
    - UDP (User Datagram Protocol) -: It is connection-less protocol. It is the go-to protocol if your application does not require reliable transport as it is very cost-effective.

<h3> Application Layer </h3>

- This layer performs the functions of top three layers of the OSI model: Application, Presentation and Session Layer.
- It is responsible for node-to-node communication and controls user-interface specifications.
- Some of the protocols present in this layer are: HTTP, HTTPS, FTP, SMTP, etc.