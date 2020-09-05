from flask import (
    Flask,
    render_template,
    make_response,
    request,
    url_for,
    redirect,
    session,
)
import yaml

with open(r"config.yaml") as f:
    keys = yaml.full_load(f)

app = Flask(__name__)
app.debug = True
app.secret_key = keys['secret_key']


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
        country = request.form["countrydata"]
        with open("results.txt", "w") as f:
            f.write(country + "\n")
    return "fish_null_return"


if __name__ == "__main__":
    app.run()
