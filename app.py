from flask import Flask , render_template , request


app =Flask(__name__)

@app.route("/")
def hello():
    
    return render_template("index.html")

@app.route("/submit")
def submit():
    #HTML -> .py
    if request.method == ["POST"]:
        Applicant=request.form["Income"]
        CoApplicant=request.form["Co applicant Income"]
        LoanAmount=request.form["Enter loan amount"]
    #.py->HTML
    return render_template("sub.html", n = Applicant,p=CoApplicant,q=LoanAmount)


if __name__=="__main__":
    app.run(debug=True)