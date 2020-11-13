from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return "jeojfdigb"

@app.route("/<name>")
def user(name):
    return "hello"+name

@app.route("/home")
def back():
    return redirect(url_for("user",name="Amin"))

if __name__=="__main__":
    app.run()
