from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY']="josaseoojqwerklmafaf1324141241"
from app import routes