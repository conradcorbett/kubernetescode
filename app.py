from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Testing testing testing -Updates made by CC'
