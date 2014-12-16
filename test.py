from tinydb import TinyDB, where

database = "formulas_db.json"

db = TinyDB(database)

_dict = {"length": "length", "meter": "length", "m/s": "velocity", "seconds": "time", "hour": "time"}

search_id = "meter"

# The search must be a list of a string
search = str(search_id)
# This is the search we are going to use with TinyDB
formula_search = []
for word in search.split(" "):
    # Add the word to the formula_search so we can later use it with TinyDB
    formula_search.append(_dict["hour"].lower())


# Are we searching a table

formulas = db.table("formulas").search( where('variables').all(formula_search) )
