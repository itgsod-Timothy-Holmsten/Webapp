from webapp import app
from flask import render_template, request
from tinydb import TinyDB, where
from webapp.models.formula import Formula
from webapp import preloaded_db
from webapp.models.search import Search


@app.route("/formula=<formula_id>", methods=["GET"])
def show_formula(formula_id):
    search = Search(preloaded_db, "formulas")

    formula = search.get_formula_from_id(formula_id)

    formula = formula[0]

    for i in range(0, len(formula['variables'])):
        formula['variables'][i] = formula['variables'][i].capitalize()


    return render_template("layout.html", formula=formula)


