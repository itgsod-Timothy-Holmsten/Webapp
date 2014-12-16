from tinydb import TinyDB

class Formula(object):
    def __init__(self, name, variables, formula, explanation, name_added_by, date):
        self.id = None
        self.name = str(name)
        self.variables = list(variables)
        self.formula = str(formula)
        self.explanation = str(explanation)
        self.name_added_by = str(name_added_by)
        self.date = str(date)

    def add_to_db(self, db, table):
        database = TinyDB(str(db))
        tbl = database.table(str(table))

        id = len(tbl) # The id of the formula, auto incrementing

        tbl.insert({
            "id": id,
            "name": self.name,
            "variables": self.variables,
            "formula": self.formula,
            "explanation": self.explanation,
            "information": {"name_added_by": self.name_added_by, "date": self.date}
        })