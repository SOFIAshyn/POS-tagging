from flask import Flask, render_template, url_for, request, redirect, Response, send_file, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
# import networkx as nx
# from io import BytesIO
import matplotlib.pyplot as plt
from src.get_country import get_predicted_country
import json
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example_db.db' # sqlite://root:''@localhost/example_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.app = app
db.drop_all()
db.create_all()
db.session.commit()
main_path = ''
flag_file_names = ['china.png', 'germany.png', 'italy.png', 'usa.png']
dict_country_path = {country_path.split('.')[0]: os.path.join(main_path, country_path) for country_path in flag_file_names}


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(20), nullable=False)
    probability = db.Column(db.Integer, nullable=False)
    flag_photo_path = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Country %d>' % self.id


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50000), nullable=False)

    def __repr__(self):
        return '<Article %d>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        db.drop_all()
        db.create_all()

        task_content = request.form['content']
        # print(len(task_content))

        if len(task_content) < 500:
            article = Article(content=task_content)
            db.session.add(article)
            db.session.commit()

            return redirect("/")

        countries, probs = get_predicted_country(task_content)
        try:
            article = Article(content=task_content)
            db.session.add(article)

            for i in range(len(countries)):
                cur_country = Country(country_name=countries[i], probability=probs[i], \
                                      flag_photo_path=dict_country_path[countries[i].lower()])
                db.session.add(cur_country)
            db.session.commit()

            return redirect('/')
        except:
            return 'There was an issue finding a country of the text.'
    else:
        lst_countries_objects = Country.query.all()
        article = Article.query.all()
        return render_template('index.html', pred_countries=lst_countries_objects, image=True, article=article, )


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    app.run(debug=True)