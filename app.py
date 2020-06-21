from flask import Flask, render_template, make_response, request, url_for, redirect

app = Flask(__name__)
app.debug = True


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/globe", methods=["GET", "POST"])
def globe():
    return render_template("globe_view.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
