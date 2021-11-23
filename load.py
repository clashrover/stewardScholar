import psycopg2
conn = psycopg2.connect(host="localhost", database="sil", user="postgres", password="hello")
# cur = conn.cursor()


# cur = conn.cursor()
# query = "CREATE TABLE papers(id integer PRIMARY KEY, title text, authors text);"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE paper_flag_edge(paper_id integer, flag_id integer);"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE flags(id integer PRIMARY KEY, title text, type integer, description text, email text, super_id integer);"
# cur.execute(query)

# cur = conn.cursor()
# query = "ALTER TABLE paper_flag_edge ADD CONSTRAINT id_x_fk FOREIGN KEY (flag_id) REFERENCES flags (id) ON DELETE CASCADE;"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE super_flags(id integer PRIMARY KEY, source_id integer);"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE citations(id1 integer, id2 integer);"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE debates(id integer PRIMARY KEY, flag_id integer, email text, content text);"
# cur.execute(query)

# cur = conn.cursor()
# query = "ALTER TABLE debates ADD CONSTRAINT id_deb_fk FOREIGN KEY (flag_id) REFERENCES flags (id) ON DELETE CASCADE;"
# cur.execute(query)

# cur = conn.cursor()
# query = "CREATE TABLE flag_counter(counter integer);"
# cur.execute(query)

# cur = conn.cursor()
# query = "INSERT INTO flag_counter VALUES (0);"
# cur.execute(query)


conn.commit()
cur.close()
