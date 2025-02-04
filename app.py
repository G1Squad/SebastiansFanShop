from flask import Flask, render_template
from flask_migrate import Migrate, upgrade
from dotenv import load_dotenv
import os
import logging
from models import db, seedData, Category, Product
import mysql.connector

# Ladda miljövariabler
load_dotenv()

# Skapa Flask-app
app = Flask(__name__)

# Hämta DB-konfig och skriv ut (utan lösenord)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")

print(f"🔍 Ansluter till MySQL: {DB_USER}@{DB_HOST}/{DB_DATABASE}")

# Konfigurera SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initiera databasen
db.app = app
db.init_app(app)
migrate = Migrate(app, db)

# Kontrollera MySQL-anslutning innan migration
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"✅ Ansluten till databas: {db_name[0]}")
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Fel vid anslutning till MySQL: {err}")
    exit(1)

# Flask routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

# Starta applikationen
if __name__ == "__main__":
    with app.app_context():
        try:
            print("📌 Kör migrationer...")
            upgrade()
            print("✅ Migrationer uppdaterade!")
        except Exception as e:
            print(f"❌ Migration ERROR: {e}")

        try:
            print("📌 Kör seedData...")
            seedData(db)
            print("✅ seedData kördes!")
        except Exception as e:
            print(f"❌ seedData ERROR: {e}")

    print("🚀 Startar Flask-server...")
    app.run(debug=True)
