import psycopg2

def connect():
    c = psycopg2.connect("dbname=flask-sql user=danielstallworth")
    return c

def get_all_toys():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from toys")
    toys = cur.fetchall()
    cur.close()
    conn.close()
    return toys

def add_toy(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into toys (name) values (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()