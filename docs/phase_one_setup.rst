Phase One
=========

Table of Contents

1.  `Scope`_
*.  `Setup`_

Scope
-----

Phase One sets up Atlanta as the main controller over an assemblage of RabbitMQ, Supervisor, Git, ``LPM`` and Mongo to create a REST server that allows the client to add messages to a local message queue.  The messages are, then processed by the respective, responding components and the client can trigger events on the server like the creation of a new Git repository.

Setup
-----

**Required Tools**

-  Git: `sudo apt-get install git`
-  Supervisor: `sudo apt-get install supervisor`.  See `config settings`_
-  RabbitMQ: `sudo apt-get install rabbitmq-server`