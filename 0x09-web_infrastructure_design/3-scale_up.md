Description:
This web setup is an expanded version of the previously described infrastructure. In this rendition, all single points of failure (SPOFs) have been eradicated, and the significant elements (web server, application server, and database servers) have been allocated to separate GNU/Linux servers. The SSL safeguarding isn't halted at the load-balancer level, and each server's network is fortified with a firewall while also being under surveillance.

Details About This Setup:

Firewall Addition for Server Protection:
A firewall has been introduced for each server. This shields individual servers from undesired and unauthorized access, enhancing security across the board rather than concentrating on just one server's defense.
Issues Present in This Setup:

Elevated Maintenance Expenses:
The decision to allocate each major component to its own server leads to escalated maintenance costs. This move necessitates acquiring more servers, causing an increase in electricity expenses for the company. Procuring, operating, and maintaining the additional servers require allocating funds from the company's budget.
