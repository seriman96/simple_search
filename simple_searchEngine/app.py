from flask import Flask, render_template, request, redirect, url_for, session
from search import search 

app = Flask(__name__)
app.secret_key = "#$%#$%^%^BFGBFGBSFGNSGJTNADFHH@#%$%#T#FFWF$^F@$F#$FW"

@app.route("/")
def user():
	return render_template("User.html")

@app.route("/index", methods=["POST", "GET"])
def index():
	pwd = 'today@123'
	pwdU = request.form["pass"]
	# print(pwdU)
	mnU = request.form["name"]
	msg = 'successfully logged!'
	session["nmU"] = mnU
	session["msg"] = msg
	if pwdU != pwd:
		return redirect(url_for("user"))
	return render_template("index.html", nm=session["nmU"], mg=session["msg"])


@app.route("/search", methods=["POST", "GET"])
def searchr():
	if request.method == "POST":
		query = request.form["query"]
		results = search(query, num_results=10)# 35
		ln = []
		ln1 =[]
		ln2 =[]
		for i in results:
			p = list(i)
			ln.append(p[0])
			ln1.append(p[1])
			ln2.append(p[2])
		session["results"] = ln
		session["ln1"] = ln1
		session["ln2"] = ln2
		# session["results"] = results
		session["query"] = query
		return redirect(url_for("searchr"))
	return render_template("search.html", results=session["results"], query=session["query"], mdes= session["ln1"],tle=session["ln2"],zip=zip) 


if __name__ == '__main__':
	app.run(debug=True)