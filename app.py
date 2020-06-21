from flask import (
    Flask,
    render_template,
    make_response,
    request,
    url_for,
    redirect,
    session,
)

app = Flask(__name__)
app.debug = True
app.secret_key = r"8gQ<fO(QBVm]*:%"


@app.route("/")
def home():
    # session["country"] = "not a country"
    return render_template("base.html")


@app.route("/globe", methods=["GET", "POST"])
def globe():
    return render_template("globe_view.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data", methods=["POST"])
def data_value():
    if request.method == "POST":
        # if session.get("country") != request.form["numdata"]:
        country = request.form["countrydata"]
        session["country"] = country
        with open("results.txt", "w") as f:
            f.write(country + "\n")
    return "fuck"


if __name__ == "__main__":
    app.run()
