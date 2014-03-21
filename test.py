#!/usr/bin/env python

import cx_Oracle

db = cx_Oracle.connect('kyuho', 'YourPassWordHere', 'oracle.cise.ufl.edu/orcl')

c = db.cursor()

c.execute('select * from city')
for result in c:
    print result

db.close()
