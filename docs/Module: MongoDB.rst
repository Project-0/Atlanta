===============
Module: MongoDB
===============

Abstract
++++++++

Decisions
+++++++++

**One of the principal purposes of the RESTful server will be to provide client applications with a schemaless datastore.** Given the modular nature of the application and the convenience of JSON based data storage in a RESTful environment, we have decided that we will go with a schemaless, JSON (or, more appropriately, BSON) database for our default backend.  The decision to use MongoDB is motivated by the fact that it scales well, runs on a Raspberry Pi, is free, and has no embedded alternative (I looked; nothing seems to be really feasible yet).  That said, Atlanta is modular; alternatives are welcome.
