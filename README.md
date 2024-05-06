# Assess SingleStore DB
DATA ENGINEERING SOLUTIONS - Assess SingleStoreDB

**Problem Statement** : A reporting app where, based on user selection, some complex calculations will be performed and then will be shown on the UI. SQL Server is used as the backend DB which is processing 7 + 5 Million rows in ~10-15 seconds. To keep users engaged on the app, data should be processed in sub seconds. 

**Solutions** : While looking for other DB services to speed up data processing, NewSQL concept emerged into the assessment - Apache Durby, SingleStore DB, VoltDB etc. are some of the examples of New SQL.

Since Singlestore is compatible with MYSQL wire protocol (i.e. Its similar to MYSQL, Connections and Syntax etc.) therefore SingleStore will be assessed further.

**Definition and Differences** : 

SingleStore is a NewSQL database, provides Low-latency queries i.e. Millisecond query performance.
NewSQL is a term that combines SQL and NoSQL. NewSQL is a unique database system that combines ACID compliance with horizontal scaling. The database system strives to keep the best of both worlds i.e OLTP-based transactions and the high performance of NoSQL combine in a single solution.

### NewSQL Database Features
The main features of NewSQL databases are:

- In-memory storage and data processing supply fast query results.
- Partitioning scales the database into units. Queries execute on many shards and combine into a single result.
- ACID properties preserve the features of RDBMS.
- Secondary indexing results in faster query processing and information retrieval.
- High availability due to the database replication mechanism.
- A built-in crash recovery mechanism delivers fault tolerance and minimizes downtime.


|Feature|SQL|NoSQL|NewSQL|
| -------- | ------- |-------- | ------- |
|Schema|Relational (table)|Schema-free|Both|
|SQL|Yes|Depends on the system|Yes, with enhanced features|
|ACID|Yes|No (BASE)|Yes|
|OLTP|Partial support|Not supported|Full support|
|Scaling|Vertical|Horizontal|Horizontal|
|Distributed|No|Yes|Yes|
|High availability|Custom|Auto|Built-in|
|Queries|Low complexity queries|High complexity queries|Both|