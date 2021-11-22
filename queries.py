import psycopg2
CONNECTQUERY="host='localhost' dbname='sil' user='postgres' password='hello'"

def fetch_citations():
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="""
        SELECT * 
        FROM citations;
        """
    try:
        cur.execute(SQL)
        ans = cur.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()
    return ans


def fetch_paper(id):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT id,title FROM papers WHERE id = {};".format(id)
    
    try:
        cur.execute(SQL)
        ans = cur.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()
    return ans


def fetch_flags(id):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT id,name,distance,paper_id FROM flag WHERE paper_id = {};".format(id)
    
    try:
        cur.execute(SQL)
        ans = cur.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()
    return ans

def insert_paper(id,title):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(id, title)
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="INSERT INTO papers VALUES ({},'{}');".format(int(id),title)
    print(SQL)
    try:
        cur.execute(SQL)
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    

    conn.commit()
    cur.close()
    conn.close()
