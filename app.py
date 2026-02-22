from flask import Flask, request, render_template


app=Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def homepage():
    return render_template("indexn.html")

@app.route("/faculty",methods=["GET", "POST"])
def faculty():
    return render_template("faculty.html")


if __name__=="__main__":
    app.run(debug=True)