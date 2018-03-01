from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command()
def init_db():
    db.drop_all()
    db.create_all()
    print("Database created")


if __name__ == '__main__':
    app.run()
