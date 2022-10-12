from flask import Flask 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

from apps import views