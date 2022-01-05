from flask import Flask, redirect, render_template, request, url_for
import time

app = Flask(__name__)

# main home page
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        ingredients = request.form.getlist('ingredient')
        occasion = request.form.getlist('occasion')
        diet = request.form.getlist('diet')
        print(ingredients)
        if ingredients == []:
            return render_template("all.html")
        for i in range(len(ingredients)):
            if ingredients[i] == "1":
                return render_template("chicken.html")
            elif ingredients[i] == "3":
                return render_template("salmon.html")
            elif ingredients[i] == "2":
                return render_template("egg.html")
            elif ingredients[i] == "4":
                return render_template("carrot.html")
    else:
        return render_template("home.html")

# results
@app.route('/results', methods=["POST", "GET"])
def results(resultid):
    if request.method == "GET":
        if resultid == 1:
            return "Chicken"
        elif resultid == 3:
            return "Salmon"
        elif resultid == 2:
            return "Egg"
        elif resultid == 4:
            return "Carrots"
    
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run()