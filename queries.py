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


def fetch_paper(title):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT * FROM papers WHERE title = '{}';".format(title)
    
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
    SQL="SELECT flags.id ,flags.title, flags.type, flags.description, flags.email, flags.super_id FROM flags, paper_flag_edge WHERE paper_flag_edge.paper_id = {} AND paper_flag_edge.flag_id = flags.id;".format(id)
    
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


def fetch_counter():
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT * FROM flag_counter;"
    
    try:
        cur.execute(SQL)
        ans = cur.fetchone()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    # cur.close()
    # conn.close()

    # print(ans[0])
    ans = int(ans[0])
    ans+=1
    ans = int(ans)
    # print(ans)
    # conn=psycopg2.connect(CONNECTQUERY)
    # cur=conn.cursor()
   
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="UPDATE flag_counter SET counter ={};".format(ans)
    
    try:
        cur.execute(SQL)
        conn.commit()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()

    return ans-1


def insert_flag(id,title,type,content,email,super_id):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(id, title)
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="INSERT INTO flags VALUES ({},'{}',{},'{}','{}',{});".format(int(id),title,int(type), content,email,int(super_id))
    # print(SQL)
    try:
        cur.execute(SQL)
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    

    conn.commit()
    cur.close()
    conn.close()


def insert_edge(paper_id,flag_id):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(id, title)
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="INSERT INTO paper_flag_edge VALUES ({},{});".format(int(paper_id),int(flag_id))
    # print(SQL)
    try:
        cur.execute(SQL)
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    

    conn.commit()
    cur.close()
    conn.close()

def insert_super_flag(id,source):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(id, title)
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="INSERT INTO super_flags VALUES ({},{});".format(int(id),int(source))
    # print(SQL)
    try:
        cur.execute(SQL)
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    

    conn.commit()
    cur.close()
    conn.close()

def fetch_debates(id):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
   
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT * FROM debates WHERE debates.flag_id = {};".format(id)
    
    try:
        cur.execute(SQL)
        ans = cur.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()
    return ans

def insertDebate(id,fid,email,content):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(id, title)
    # ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="INSERT INTO debates VALUES ({},{},'{}','{}');".format(id,fid,email,content)
    # print(SQL)
    try:
        cur.execute(SQL)
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    

    conn.commit()
    cur.close()
    conn.close()


def fetch_neighbours(pid):
    conn=psycopg2.connect(CONNECTQUERY)
    cur=conn.cursor()
    # print(pid)
    ans = None # use of None (not "None") can be used to insert NULLs. @sagar possible?
    SQL="SELECT id1 FROM citations WHERE id2 = {};".format(pid)
    
    try:
        cur.execute(SQL)
        ans = cur.fetchall()
    except psycopg2.Error as e:
        print(e.pgerror)
        conn.rollback()
    
    cur.close()
    conn.close()
    return ans