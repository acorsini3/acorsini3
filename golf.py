import flask
app = flask.Flask("golf")
from statistics import mean
import re

def get_html(page_name):
    html_file = open (page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_txt(txt_name): #get any .txt file and return a list
    golfdb = open (txt_name)
    content = golfdb.read()
    golfdb.close
    txt = content.split("\n") 
    txt.pop() #remove the last item of the list which is an empty line
    return txt

def get_only_scores(user):#get all the scores for a specific user
    result = ""
    golfdb = open ("scores.txt")
    content = golfdb.read() #format (username + space + score) \n (new line)
    golfdb.close
    lines = content.split("\n") # return a list of (username + space + score), etc...
    for line in lines:
        if line.split('  :  ',1)[0].lower() == user.lower(): #if the username is correct
            result += line.split ('  :  ',1)[1] + " " #keep the score
    return result.split()  #return a list

def add_score(a,b): #add the score into scores.txt
    golfdb = open ("scores.txt","a")
    golfdb.write(a + "  :  " + b + "\n") 
    golfdb.close()

def add_ranking(a,b): #add index and username into ranking.txt
    golfdb = open ("ranking.txt","a")
    golfdb.write(a + "  :  " + b + "\n") 
    golfdb.close()

def update_index(old,new): #update old index by new index
    golfdb = open ("ranking.txt","r+")
    content = golfdb.read() #one big string not splitted
    content = re.sub(str(old),str(new),content) #replacing old by new
    golfdb.seek(0)
    golfdb.write(content)
    golfdb.truncate()

def check(index,user): #check if an index already exist for the user
    elements = get_txt("ranking.txt")
    value = 0
    for element in elements: #look through the list
        if element.split ("  :  ",1)[1].lower() == user: #if the username exist already in the ranking
            update_index(element.split ("  :  ",1)[0],index) #update the index
            value = 1
    return(value)
    
def reset_score(): # reset all scores
    golfdb = open ("scores.txt","w")
    golfdb.truncate(0)
    golfdb.close
    
@app.route("/") #homepage
def homepage():
    return get_html("golf") 

@app.route("/add") 
def add():
    html_page = get_html("display")
    score = str(flask.request.args.get("score")) #from html
    username = str(flask.request.args.get("aname")) #from html
    if score.isnumeric():
        if int(score) > 71 and int(score) < 137: #score should be a number between 72 and 136
            add_score(username, score)
            message = "Score succesfully added, please go back and click on CALCULATE INDEX" #confirming the score is added
            return html_page.replace("TEMP", message)
        else:   
            message = "Are you sure ? Please enter your score again !" #managing error
            return html_page.replace("TEMP", message)
    else:
        message = "Sorry but this is not considered as a score ! Please try again." #managing error
        return html_page.replace("TEMP", message)

@app.route("/calculate")
def calculate():
    html_page = get_html("display")
    filter = flask.request.args.get("cname").lower() #avoid case sensitive
    scores = get_only_scores(filter)#a collection of strings that contains all the scores of this player
    ranking = get_txt("ranking.txt") #a list that contains all the rank
    index = "" 
    calcul = ""
    par = 72 #the lower score you can do in golf.(if you are a pro)

    if not scores:
        index = "You did not enter any score yet !" 
        return html_page.replace("TEMP", index)

    else:
        calcul = str("{:.1f}".format(mean((int(score)-int(par)) for score in scores)))  #1 decimal mean of all scores - "par"
        index = "Your updated golf index is now: " + calcul + " !"

        if not ranking: #if the list is empty
            add_ranking (calcul, filter.upper()) #add the first index
        else:
            if check(calcul, filter)==0: # if the list is not empty check if user exist already and update its index
                add_ranking(calcul, filter.upper()) # if the list not empty and user does not exist create the new rank in ranking.txt
        return html_page.replace("TEMP", index) 

@app.route("/scores")
def scores():
    html_page = get_html("display")
    scores = get_txt("scores.txt")
    actual_values = "NAME : SCORE" #header

    if not scores:
        actual_values = "You did not enter any score yet !"
        return html_page.replace("TEMP", actual_values)
    else :
        for score in scores:
            actual_values += "<p>" + score.upper() + "</p>"
        return html_page.replace("TEMP", actual_values)

@app.route("/ranking")
def rank():
    html_page = get_html("display")
    ranking = get_txt("ranking.txt") #a list that contains all the rank
    actual_values = "INDEX : NAME"  #header

    if not ranking:
        actual_values = "Please calculate at least one index to see the ranking"
        return html_page.replace("TEMP", actual_values)
    else :
        ranking.sort(key = lambda x: float(x.split('  :  ')[0]))#use the index with float as a number to rank the users
        for rank in ranking:
            actual_values += "<p>" + rank + "</p>"
        return html_page.replace("TEMP", actual_values)

@app.route("/reset")
def reset():
    html_page = get_html("display")
    result = "All your scores were succesfully deleted !" #confirming the scores were deleted
    reset_score()
    return html_page.replace("TEMP", result)

#$env:FLASK_APP="golf.py" 
#flask run