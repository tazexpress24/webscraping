from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import sys
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# @app.route("/")
# def index():
#     mars = mongo.db.mars.find_one()
#     print(mars, file=sys.stderr)

#     return render_template("index.html", mars = mars)

# @app.route("/scrape")
# def scrape():
#     mars = mongo.db.mars 
#     mars_data = scrape_mars.scrape()
#     mars.update({}, mars_data, upsert=True)
#     return redirect("http://localhost:5000/", code=302)

# if __name__ == "__main__":
#     app.run(debug=True)



# create mongo connection
# client = pymongo.MongoClient()
db = mongo.db
#collection = db.mars_data_entries
print("after mongodb section")

@app.route("/")
def home():
    mars_data = db.mars.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def web_scrape():
    db.collection.remove({})
    mars_data = scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)   