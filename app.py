#Lots of things to do here. This is just a draft.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>GREATEST E-COMMERCE WEB SITE EVER IS ABOUT BE PUBLISHED<\h1>"



if __name__ == '__main__':
    app.run(debug=True)