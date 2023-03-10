from flask import Flask

app = Flask(__name__)

app.secret_key = "Secret 1234"

DATABASE = "belt_exam"