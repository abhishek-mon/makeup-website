from flask import Flask , render_template


app = Flask(__name__)
@app.route("/") ##set the route

def hello_world():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)