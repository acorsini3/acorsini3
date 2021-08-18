import flask
app = flask.Flask("note3")

def get_html(page_name):
    html_file = open (page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_note():
    notedb = open ("notes3.txt")
    content = notedb.read()
    notedb.close
    notes = content.split("\n") #collection of splitted names
    return notes

def add_note(a):
    notedb = open ("notes3.txt","a")
    notedb.write("\n" + a + "\n")
    notedb.close()
    
    
#This is the homepage
@app.route("/")
def homepage():
    return get_html("WebNoteApp3") 

#This is the dynamic notes page 
@app.route("/notes3")
def note():
    html_page = get_html("notes3")
    notes = get_note()#a collection that contains all contacts name
    actual_values = "" #empty string

    for note in notes:
        actual_values += "<p>" + note + "</p>"
    return html_page.replace("NOTES", actual_values)

#this is the add note page
@app.route("/add")
def add():
    html_page = get_html("notes3")
    query = flask.request.args.get("n")
    add_note(query)
    result = "note succesfully added" #string
    return html_page.replace("NOTES", result)

#this is the search page
@app.route("/search")
def search():
    html_page = get_html("notes3")
    query = flask.request.args.get("q")
    notes = get_note()#a collection that contains all contacts name
    result = ""#empty string

    for note in notes:
        if note.lower().find(query.lower()) != -1:
            result += "<p>" + note + "</p>"
    if result == "":
        result = "<p> No result found </p>"
    return html_page.replace("NOTES", result)

#cd notes3
#cd ..
#this is the command to run flask
 #$env:FLASK_APP="note3.py" 
 #flask run