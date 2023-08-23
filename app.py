from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Testingtestingtestingtesting -Updates made by CC'
