from flask import Flask, render_template,request
from clarifai_api.client import ClarifaiApi
import requests,json

token = "a010c8418f86e4bee30358ac4812b7beee9772e8"
clarifai_api = ClarifaiApi()

app = Flask(__name__)
app.config["DEBUG"] = True #Only for testing!!

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry bruh, this page ain't here", 404

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
    return "Your Name"

@app.route("/website")
def website():
    return "https://github.com/kendurkin"

@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        url = "https://api.github.com/search/repositories?q=" + request.form["user_search"] + "&access_token=" + token
        response_dict = requests.get(url).json()
        return render_template("results.html",api_data=response_dict)
    else: # request.method == "GET"
        return render_template("search.html")

@app.route("/add/<x>/<y>")
def add(x,y):
    return str(int(x)+int(y))

@app.route("/pics/<picture>")
def pics(picture):
    result = clarifai_api.tag_images(open('/home/ken/Pictures/'+picture+'.jpg'))
    thetags = (result["results"][0]["result"]["tag"]["classes"])
    return json.dumps(thetags,sort_keys=True,indent=4,separators=(',',': '))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
