import psycopg2

conn = psycopg2.connect("dbname=flask-sql user=danielstallworth")
cur = conn.cursor()
cur.execute("drop table if exists toys")
cur.execute("create table toys (id serial primary key, name text);")

cur.execute("insert into toys (name) values (%s)", ("duplo",))
cur.execute("insert into toys (name) values (%s)", ("lego",))
cur.execute("insert into toys (name) values (%s)", ("knex",))
conn.commit()

cur.execute("select * from toys")
print(cur.fetchall())

cur.close()
conn.close()