import sqlite3 as lite

con = None
try:
    con = lite.connect("morosobot.db")
    cur = con.cursor()
except lite.Error, e:
    print "Error %s" % e.args[0]

def query(q):
    cur.execute(q)
    return cur.fetchall()
