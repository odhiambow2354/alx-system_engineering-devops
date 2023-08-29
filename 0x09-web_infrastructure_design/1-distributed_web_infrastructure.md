Description:
Presented here is a distributed web infrastructure meticulously designed to alleviate the burden on the primary server by distributing a portion of the workload to a replica server, facilitated by a load balancer responsible for skillfully distributing the load between the primary and replica servers.

Insights Into This Infrastructure:

Load Balancer's Distribution Algorithm:
The HAProxy load balancer is skillfully configured with the Round Robin distribution algorithm. This algorithm efficiently alternates the use of servers behind the load balancer based on their assigned weights. The process ensures a harmonious and equitable distribution of processing time. Being a dynamic algorithm, Round Robin permits real-time adjustments to server weights, optimizing load distribution.

Enabled Setup by the Load Balancer:
The HAProxy load balancer empowers an Active-Passive setup, differing from an Active-Active configuration. In an Active-Active setup, the load balancer allocates workloads across all nodes to prevent any one node from becoming overloaded. This approach boosts throughput and response times by capitalizing on multiple available nodes. Conversely, an Active-Passive setup entails that not all nodes are active simultaneously. For instance, in a two-node scenario, while the first node is active, the second node remains passive or standby. The subsequent passive node transitions to active mode if the preceding node becomes inactive.

Database Primary-Replica (Master-Slave) Cluster Dynamics:
The Primary-Replica framework designates one server as the Primary, and another as a Replica of the Primary. While the Primary server engages in read/write operations, the Replica server solely undertakes read requests. Synchronization of data between the Primary and Replica servers occurs whenever the Primary server executes a write operation.

Distinct Roles of Primary and Replica Nodes:
The Primary node bears the responsibility for all write operations essential to the website's functioning. On the other hand, the Replica node specializes in executing read operations. This delegation minimizes read traffic directed at the Primary node, thereby optimizing its efficiency.

Issues Associated With This Infrastructure:

Presence of Single Points of Failure (SPOFs):
Vulnerabilities stem from multiple single points of failure. For instance, if the Primary MySQL database server experiences an outage, the entire site loses the ability to effect changes, including user management. The server hosting the load balancer and the application server connected to the primary database server also represent potential SPOFs.

Security Vulnerabilities:
The absence of SSL encryption exposes transmitted data to potential eavesdropping by unauthorized entities. Furthermore, the absence of a firewall across all servers renders the infrastructure susceptible to unauthorized access.

Lack of Monitoring:
The absence of a monitoring mechanism prevents the assessment of each server's operational status. The lack of monitoring restricts the timely identification of issues and performance bottlenecks.
