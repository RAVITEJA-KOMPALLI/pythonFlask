from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname=='ravi'and passwrd=="ravi":
        return"Welcome %s" %uname
    else:
        return "invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)
