from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# main home page
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        ingredients = request.form.getlist('ingredient')
        occasion = request.form.getlist('occasion')
        diet = request.form.getlist('diet')
        return "Done"
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run()