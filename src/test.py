from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    cmd = ["python", "helloworld.py", "helloworld.txt"]
    return render_template('index.html')
