from webapp import app
from flask import render_template, request
from tinydb import TinyDB, where
from webapp.models.formula import Formula
import datetime
from webapp import preloaded_db


@app.route("/add", methods=["GET", "POST"])
def add_formula():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        name = request.form.get("formula_name")
        formula_written = request.form.get("formula_formula")

        # Make sure variables are letters and not ("space" " ")
        unities = str(request.form.get("formula_unities"))
        unities_list = []

        for var in unities.split(" "):
            unities_list.append(var.lower())

        explanation = request.form.get("formula_explanation")

        formula = Formula(name, unities_list, formula_written, explanation, user_name, datetime.date)
        db = preloaded_db
        table = "formulas"
        formula.add_to_db(db, table)

    return render_template("add_formula.html")


