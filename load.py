import psycopg2
conn = psycopg2.connect(host="localhost", database="sil", user="postgres", password="hello")
# cur = conn.cursor()

cur = conn.cursor()
insert_query = "INSERT INTO citations VALUES (3,1,3);"
cur.execute(insert_query)

# CREATE TABLE citationsList(id1 integer, id2 integer);

# CREATE TABLE papers(id integer PRIMARY KEY,title text);

# CREATE TABLE flag(id integer PRIMARY KEY, name text,distance integer,paper_id integer);

conn.commit()
cur.close()
