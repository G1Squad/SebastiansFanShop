from flask import Flask, render_template
from flask_migrate import Migrate, upgrade
from dotenv import load_dotenv
import os

from models import db, seedData, Category, Product

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_DATABASE")}'
db.app = app
db.init_app(app)
migrate = Migrate(app,db)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')




if __name__ == "__main__":
    with app.app_context():
        upgrade()
        seedData(db)

    app.run(debug=True)
