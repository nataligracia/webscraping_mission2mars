#Flask, pymongo, and python file scrape_mars, 

from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)


#Use flask_pymongo to set up mongo connection, 'mars_app" is created
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#302
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrapeaction")
def scrapeaction():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.replace_one({}, mars_data, upsert=True)
    return ""


@app.route("/scrape")
def scrape():
    return render_template("scrape.html")


if __name__ == "__main__":
    app.run()