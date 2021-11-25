from flask import *
from queries import *

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/searchPaper")
def searchPaper():
    return render_template("searchPaper.html")

@app.route("/getPaper",methods = ['POST'])
def getPaper():
    title = request.form['title']
    paper = fetch_paper(title)
    print(paper)
    if(paper==None or len(paper)==0):
        return "Paper not found"
    flags = fetch_flags(paper[0][0])
    if flags == None:
        flags =[]
    
    # print(flags)
    return render_template("displayPaper.html",paper = paper, flags = flags, len = len(flags))



@app.route("/addPaper")
def addPaper():
    return render_template("addPaper.html")


@app.route("/getAddPaper",methods = ['POST'])
def getAddPaper():
    id = int(request.form['id'])
    title = request.form['name']
    # print(title)
    paper = fetch_paper(id)
    if(len(paper)>0):
        return "Paper already exists"
    
    insert_paper(id,title)

    paper = fetch_paper(id)

    return "Paper Added"


@app.route("/addFlag/<int:pid>")
def addFlag(pid):
    return render_template("addFlag.html", pid = pid)


@app.route("/getAddFlag/<int:pid>",methods = ['POST'])
def getAddFlag(pid):
    email = request.form['email']
    content = request.form['content']
    title = request.form['title']
    counter = fetch_counter()
    sup_id = counter
    insert_flag(counter,title,0,content,email,sup_id)
    insert_edge(pid,counter)

    insert_super_flag(counter,counter)
    
    # The causal reason logic
    print("pid is:", pid)
    q = []
    q.append((pid,0))
    max_dis = 3
    expanded = set()
    while(len(q)>0):
        a = q[0]
        print("a is : ",a)
        q.pop(0)
        expanded.add(a[0])
        if(a[1]>max_dis):
            break
        
        neighbours = fetch_neighbours(a[0])
        print("A is :",a, "N are:",neighbours)
        if neighbours == None:
            return "No neighbours"
        for n in neighbours:
            n = n[0]
            if n not in expanded:
                counter_child = fetch_counter()
                insert_flag(counter_child,title,a[1]+1,content,email,sup_id)
                insert_edge(n,counter_child)
                q.append((n,a[1]+1))


    return redirect(url_for('searchPaper'))


@app.route("/viewFlag/<int:id>-<string:title>-<int:type>-<string:desc>-<string:email>-<int:super_id>")
def viewFlag(id,title, type, desc, email, super_id):
    flag = [id,title,type,desc,email,super_id]
    print(flag)
    debates = fetch_debates(id)
    # print(flag)
    # print(debates)
    return render_template("viewFlag.html", flag = flag, debates = debates, len=len(debates))


@app.route("/trackFlag/<int:sid>")
def trackFlag(sid):
    print(sid)
    paper = fetch_source(sid)
    if(paper==None or len(paper)==0):
        return "Paper not found"
    flags = fetch_flags(paper[0][0])
    if flags == None:
        flags =[]
    
    # print(flags)
    return render_template("displayPaper.html",paper = paper, flags = flags, len = len(flags))



@app.route("/addDebate/<int:fid>",methods = ['POST'])
def addDebate(fid):
    email = request.form['email_addr']
    content = request.form['content']
    counter = fetch_counter()
    insertDebate(int(counter), int(fid), email, content)
    
    # The causal reason logic

    return redirect(url_for('searchPaper'))


if __name__ == "__main__":
    app.run(debug=True)