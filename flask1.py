from flask import Flask

app = Flask(__name__)#creating the Flask object
@app.route('/') #decorator drfines the

def home():
    return "Hello, this is our first flask website "

if __name__ == '__main__':
    app.run(debug=True)

