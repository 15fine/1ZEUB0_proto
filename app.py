from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# main home page
@app.route('/')
def index():
    return render_template("home.html")

# function to display results based on selection of ingredients
@app.route('/results')
def result():
    return render_template("results.html")

if __name__ == "__main__":
    app.run()