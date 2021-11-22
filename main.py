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
    id = int(request.form['id'])
    paper = fetch_paper(id)
    print(paper)
    if(paper==None or len(paper)==0):
        return "Paper not found"
    flags = fetch_flags(id)
    if flags == None:
        flags =[]
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


@app.route("/addFlag")
def addFlag():
    return render_template("addFlag.html")





# @app.route("/addFlag")
# def searchQuery():
#     return render_template("addPaperQuery.html")


# @app.route("/productQuery")
# def productQuery():
#     # get distinct color values etc from the db
#     # pass it n below
#     # colors = ['Blue','Yellow']
#     # sizes = ['M','XL']
#     # categories = ['jeans','shirt']
#     # fabrics = ['cotton','polyester']
#     # below = [200,500,1000,2000]
#     # orders = ["price"]
    
#     colors = fetch_colors()
#     sizes = fetch_sizes()
#     categories = fetch_categories()
#     fabrics = fetch_fabrics()
#     below = [200,500,1000,2000]
#     orders = ["price"]
    
#     return render_template("productQuery.html",colors = colors, sizes = sizes, fabrics = fabrics, categories = categories, below = below, orders = orders)



# @app.route("/userQuery")
# def userQuery():
#     # ages = [18,19,20]
#     # colleges = ["nift delhi","nift patna"]
    
#     ages = fetch_ages()
#     colleges = fetch_colleges()
    
#     orders = ["rank","age","num products","num matches"]
#     return render_template("userQuery.html",ages=ages,colleges = colleges,orders=orders)



# @app.route("/userUpdate")
# def userUpdate():
#     types = ["Add","Delete","Update"]
#     return render_template("userUpdate.html",types = types)



# @app.route("/productUpdate")
# def productUpdate():
#     types = ["Add","Delete","Update"]
#     return render_template("productUpdate.html",types = types)



# @app.route("/matchingUpdate")
# def matchingUpdate():
#     types = ["Add","Delete","Update"]
#     return render_template("matchingUpdate.html",types = types)



# @app.route("/wardrobe")
# def wardrobe():
#     orders = ["Total Stars","Total Price"]
#     return render_template("wardrobe.html",orders = orders)




# @app.route('/getProductQuery',methods = ['POST'])  
# def getProductQuery():  
#     category=request.form['category']
#     if category == "None":
#         category = None

#     color=request.form['color']
#     if color == "None":
#         color = None
    
#     size=request.form['size']
#     if size == "None":
#         size = None
    
#     fabric=request.form['fabric']
#     if fabric == "None":
#         fabric = None
    
#     below = request.form['below']
#     if below == "None":
#         below = None
#     #   if uname=="ayush" and passwrd=="google":
#     pid = request.form['id']
#     if pid == "None":
#         pid = None
#     else:
#         try:
#             pid1 = int(pid)
#         except:
#             return "Invalid Product Id given (not an integer)"

#     data = [["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"]]

#     return render_template("pShow.html",data = data, len = len(data))



# @app.route('/getUserQuery',methods = ['POST'])  
# def getUserQuery():  
#     age=request.form['age']
#     college = request.form['college']
#     uid = request.form['id']
#     if uid != "None":
#         try:
#             uid1 = int(uid)
#         except:
#             return "Invalid User Id given (not an integer)"
    
#     data = [["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"],["asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","asdqwd","qwd","asfasf","Asdawd"]]

#     return render_template("uShow.html",data = data, len = len(data))



# @app.route('/getUpdateUser',methods = ['POST'])
# def getUpdateUser():
#     type_query = request.form['type']
#     uid = request.form['id']
#     name = request.form['name']
#     age = request.form['age']
#     address = request.form['address']
#     college = request.form['college']
#     about = request.form['about']  

#     if type_query == "None":
#         return "Select type of query"
    
#     elif type_query == "Add":
#         if uid != "None":
#             return "Don't give user id when inserting a user"
        
#         if name == "None" or age == "None" or address == "None" or college == "None" or about == "None":
#             return "Please fill full information"
        
#         if age != "None":
#             try:
#                 age1 = int(age)
#             except:
#                 return "Invalid age given (not an integer)"


#     elif type_query == "Delete":
#         if uid == "None":
#             return "Give user id for delete"
#         try:
#             uid1 = int(uid)
#         except:
#             return "Invalid user id given (not an integer)"

#         if name != "None" or age != "None" or address != "None" or college != "None" or about != "None":
#             return "Please don't fill unnecessary information"
        

#     elif type_query == "Update":
#         if uid == "None":
#             return "Please give user id when updating a user"
#         try:
#             uid1 = int(uid)
#         except:
#             return "Invalid userid given (not an integer)"

#         if age != "None":
#             try:
#                 age1 = int(age)
#             except:
#                 return "Invalid age given (not an integer)"


#     return redirect(url_for('userUpdate'))



# @app.route('/getUpdateProduct',methods = ['POST'])
# def getUpdateProduct():
#     type_query = request.form['type']
#     pid = request.form['id']
#     name = request.form['name']
#     category = request.form['category']
#     color = request.form['color']
#     description = request.form['description']
#     fabric = request.form['fabric']
#     size = request.form['size']
#     price = request.form['price']
#     url = request.form['url']
#     user = request.form['user']
#     imageURL = request.form['imageURL']
#     # do something with the data obtained
#     if type_query == "None":
#         return "Select type of query"
    
#     elif type_query == "Add":
#         if pid != "None":
#             return "Don't give product id when inserting a user"
        
#         if name == "None" or category == "None" or color == "None" or description == "None" or fabric == "None" or size == "None" or price == "None" or url == "None" or user == "None" or or imageURL == "None":
#             return "Please fill full information"
        
#         if price != "None":
#             try:
#                 p1 = int(price)
#             except:
#                 return "Invalid price given (not an integer)"


#     elif type_query == "Delete":
#         if pid == "None":
#             return "Give user id for delete"
#         try:
#             pid1 = int(pid)
#         except:
#             return "Invalid product id given (not an integer)"

#         if name != "None" or category != "None" or color != "None" or description != "None" or fabric != "None" or size != "None" or price != "None" or url != "None" or user != "None" or or imageURL != "None":
#             return "Please don't fill unnecessary information"
        

#     elif type_query == "Update":
#         if pid == "None":
#             return "Please give user id when updating a user"
#         try:
#             pid1 = int(pid)
#         except:
#             return "Invalid userid given (not an integer)"

#         if price != "None":
#             try:
#                 price1 = int(price)
#             except:
#                 return "Invalid price given (not an integer)"

#     return redirect(url_for('productUpdate'))




if __name__ == "__main__":
    app.run(debug=True)