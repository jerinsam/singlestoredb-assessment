## Install singlestoredb, pip install singlestoredb

import singlestoredb as s2
conn = s2.connect(host='127.0.0.1', port='3306', user='root',password='jerin', database='test_ss')

with conn.cursor() as cur:
    cur.execute("show variables like '%auto%'")
    for row in cur.fetchall():
        print(row)

conn.close()