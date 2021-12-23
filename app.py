from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

# display page with checklist of ingredients
@app.route('/list')
def list():
    return False

# function to display results based on selection of ingredients
@app.route('/results')
def result():
    return True

if __name__ == "__main__":
    app.run()