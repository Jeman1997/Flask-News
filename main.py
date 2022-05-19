from flask import Flask, render_template,request
import requests as req

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/results",methods=['POST'])
def res():
    ress = req.get(f"https://newsapi.org/v2/everything?q={request.form['searchbox']}&apiKey=41510b90095c4a249ba950dcb4bf283b").json()
    return render_template("results.html",ress = ress,srch = request.form['searchbox'])

if __name__=='__main__':
    app.run(debug=True)
