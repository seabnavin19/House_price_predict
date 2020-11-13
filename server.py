import utiil
import math
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    prices=None
    if request.method=="POST":
        area=request.form["area"]
        bath=request.form["op_bath"]
        room=request.form["op_Room"]
        location=request.form["op_location"]
        prices=utiil.predict_price(location,float(room),float(area),float(bath))
        prices=round(prices,2)
    v= utiil.location()
    return render_template("index.html",location=v,price=prices)





if __name__=="__main__":
    app.run()