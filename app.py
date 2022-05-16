from datetime import timedelta
from flask import Flask ,redirect,url_for,render_template,request,session,flash
from test import tong
app= Flask(__name__)

app.config['SECRET_KEY'] = "DUNGHHH"
app.permanent_session_lifetime = timedelta(minutes=1)




   
@app.route("/home")
@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method =="POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name :
            session["user"] = user_name
            flash ("You login in succesesfully !","info")
            return render_template("user.html",user=user_name)
    if "user" in session:
        user_name = session["user"]
        flash ("You have already logged in!","info")
        return render_template("user.html",user=user_name)
        
        
        
    return render_template("login.html")

@app.route("/user")
def hello_user():
    if "user" in session:
        name = session["name"]
        return render_template("user.html",user = name)
    else:
        flash("you haven't already logged in","error")
        return redirect(url_for("login"))

@app.route("/logout")
def log_out():
    session.pop("user",None)
    flash ("You logout ","info")
    
    return redirect(url_for("login"))


@app.route("/sum",methods = ["POST","GET"])
def tinh_tong():
    
    if request.method =="POST":
        a_ = request.form["name"]
        b_ = request.form["b"]
        return render_template("user.html",user=f"ab : {tong(int(b_),int(a_))}")
    else:
        return render_template("login.html")
        
    



if __name__ =="__main__":
    app.run(debug=True)