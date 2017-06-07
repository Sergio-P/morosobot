import sqlite3 as lite

con = None
try:
    con = lite.connect("morosobot.db", check_same_thread=False)
    cur = con.cursor()
except lite.Error, e:
    print "Error %s" % e.args[0]
    
def insert(query):
    assert(query.startswith("INSERT ") or query.startswith("insert "))
    try:
        cur.execute(query)
        con.commit()
    except lite.Error, e:
        return -1
    return 0

def get(query):
    assert(query.startswith("SELECT ") or query.startswith("select "))
    cur.execute(query)
    return cur.fetchall()
