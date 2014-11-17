from webapp import app
from flask import render_template, request
from webapp.models.search import Search
from webapp import preloaded_db
from webapp.models.formula import Formula

@app.route("/search", methods=["POST", "GET"])
def get_search():
    if request.method == "POST":
        search_for = request.form.get("search_for")
        search_have = request.form.get("search_have")

        print(search_have)

        _search = search_for + search_have

        print(_search)

        return search(_search)
    return "ej"


@app.route("/search=<search_id>", methods=["GET"])
def search(search_id):
    search = Search(preloaded_db, "formulas")
    formulas = search.get_formulas_from_variables(search_id)

    if not len(formulas) > 0:
        return render_template("layout.html")

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

    return render_template("layout.html", search=search_id, formulas=forms)


