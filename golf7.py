import flask
app = flask.Flask("golf7")
from statistics import mean

def get_html(page_name):
    html_file = open (page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_scores():
    golfdb = open ("scores.txt")
    content = golfdb.read()
    golfdb.close
    scores = content.split("\n") #collection of splitted scores
    scores.pop() #remove the last item of the list which is an empty line
    return scores

def add_score(a):
    golfdb = open ("scores.txt","a")
    golfdb.write(a + "\n") 
    golfdb.close()

def reset_score():
    golfdb = open ("scores.txt","w")
    golfdb.truncate(0)
    golfdb.close
    
    
#This is the route to the homepage named "golf"
@app.route("/")
def homepage():
    return get_html("golf") 

#This is the route to the dynamic scores page named "scores"
@app.route("/scores")
def scores():
    html_page = get_html("scores")
    scores = get_scores()#a collection that contains all the scores
    actual_values = "" #empty string

    if not scores:
        actual_values = "You did not enter any score yet !"
        return html_page.replace("SCORES", actual_values)
    else :
        for score in scores:
            actual_values += "<p>" + score + "</p>"
        return html_page.replace("SCORES", actual_values)

#this is the route to the "add score" page
@app.route("/add")
def add():
    html_page = get_html("scores")
    query = flask.request.args.get("n")
    if query.isnumeric():
        if int(query) > 72 and int(query) < 136: #a golf score should be a number between 72 and 136
            add_score(query)
            result = "Your score was succesfully added !" #confirming the score is added
            return html_page.replace("SCORES", result)
        else:   
            result = "Are you sure ? Please enter your score again !" #managing error
            return html_page.replace("SCORES", result)
    else:
        result = "Sorry but this is not considered as a score ! Please try again." #managing error
        return html_page.replace("SCORES", result)

@app.route("/calculate")
def calculate():
    html_page = get_html("scores")
    scores = get_scores()#a collection of strings that contains all the scores
    index = "" 
    par = 72 #the lower score you can do in golf.
    
    #if no score was entered, index max = 64
    if not scores:
        index = "You did not enter any score yet, your index is 64 !"
        return html_page.replace("SCORES", index)
    #if one or more score was enterred, index = arithmetic mean of data
    else:
        index = "Your updated golf index is now: " + str("{:.1f}".format(mean((int(score)-int(par)) for score in scores))) + " !"
        return html_page.replace("SCORES", index) #1 decimal mean of all scores - "par"
    
@app.route("/reset")
def reset():
    html_page = get_html("scores")
    result = "All your scores were succesfully deleted !" #confirming the scores were deleted
    reset_score()
    return html_page.replace("SCORES", result)


#cd MyApp : to access the folder
#cd .. : to go back
#this is the command to run flask
#$env:FLASK_APP="golf7.py" 
#flask run