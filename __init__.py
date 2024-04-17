from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy
app = Flask(__name__)
app.config['SLQALCHEMY_DATABASE_URI'] ='sqlite:///crud.db'
db = SQLALchemy(app)
#from app.models.products import Products
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")