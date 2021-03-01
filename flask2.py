from flask import Flask
app= Flask(__name__) #creating the Flask object
def courses_info():
    return 'hi'
@app.route('/home')
def home():
    return "hello,welcome to KL <br> Hello <br> <h1>Welcome</h1>"

@app.route('/home/about')
def about():
    return 'Location: Hyderabad'

@app.route('/home/courses')
def courses():
    return ''+courses_info()

if __name__=="__main__":
    app.run()