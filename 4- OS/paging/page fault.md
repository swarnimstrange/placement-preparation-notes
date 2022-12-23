<h3> Page Fault </h3>

- when a processor want to acccess a page, and that particular page is not currently present in the main memory then the page fault occurs.

- when page fault occcurs then and the page is not in main memory and page table so, cpu will now send and error message to os that page is not present then os will check that is the page is available in seconary memory or not. if it's present then it will send a message that yes it's present in secondary memory so whenever any page comes out of main memory then that page will take its place

<h3> Thrasing </h3>

- Thrashing occurs when a system spends more time processing page faults than executing transactions.

- While processing page faults is necessary in order to appreciate the benefits of virtual memory, thrashing has a negative effect on the system

<h3> Belady’s Anomaly </h3>

- Belady’s Anomaly is the phenomenon of increasing the number of page faults on increasing the number of frames in main memory.
