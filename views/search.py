from webapp import app
from flask import render_template, request
from webapp.models.search import Search
from webapp import preloaded_db
from webapp.models.formula import Formula

@app.route("/search", methods=["POST", "GET"])
def get_search():
    if request.method == "POST":
        search_input = request.form.get("search")

        return search(search_input)

    return render_template("layout.html")


#@app.route("/search=<search_id>", methods=["GET"])
def search(search_id):
    search = Search(preloaded_db, "formulas")
    formulas = search.get_formulas_from_variables(search_id)

    forms = []
    unsolvable_forms = []

    for formula in formulas:
        form = Formula(
                formula['name'],
                formula['unities'],
                formula['formula'],
                formula['explanation'],
                formula['information']['name_added_by'],
                formula['information']['date'])

        form.id = formula['id']
        if not formula['missing_unities'] > 1:
            forms.append(form)
        else:
            unsolvable_forms.append(form)

    return render_template("layout.html", search=search_id, formulas=forms, unsolvable_formulas=unsolvable_forms)


