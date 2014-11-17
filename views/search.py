from webapp import app
from flask import render_template
from webapp.models.search import Search
from webapp import preloaded_db
from webapp.models.formula import Formula

@app.route("/search=<search_id>", methods=["GET"])
def search(search_id):
    search = Search(preloaded_db, "formulas")
    formulas = search.get_formulas_from_variables(search_id)

    forms = []

    for formula in formulas:
        form = Formula(
                formula['name'],
                formula['variables'],
                formula['formula'],
                formula['explanation'],
                formula['information']['name_added_by'],
                formula['information']['date'])

        forms.append(form)

    return render_template("index.html", search=search_id, formulas=forms)


