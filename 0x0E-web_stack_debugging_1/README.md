# Web stack debugging #1

In this project, I continued to debug the configuration of the web server
issued in project 0x0F. Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. 

## Tasks :page_with_curl:

* **0. Nginx likes port 80**
* [0-nginx_likes_port_80](./0-nginx_likes_port_80): Ubuntu container’s Nginx installation from listening on port 80
	* Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
	* Write a Bash script that configures a server to the above requirements

* **1. Make it sweet and short**
* [1-debugging_made_short](./1-debugging_made_short):Using what you did for task #0, make your fix short and sweet.
* Requirements:
	* Your Bash script must be 5 lines long or less
	* There must be a new line at the end of the file
	* You must respect usual Bash script requirements
	* You cannot use ;
	* You cannot use &&
	* You cannot use wget
	* You cannot execute your previous answer file (Do not include the name of the previous script in this one)
	* service (init) must say that nginx is not running ← for real

