from tinydb import TinyDB, where

class Search(object):
    def __init__(self, database, table=""):
        self.database = TinyDB(str(database))
        self.database_table = self.database.table(table)

    def using_table(self):
        if len(self.database_table) > 0:
            return True

    def get_formula_from_id(self, formula_id):
        search = int(formula_id)

        if self.using_table():
            formula = self.database_table.search( where('id') == search )
            print(formula)
            return formula

    def get_formulas_from_variables(self, search_id):
        #Replace this with a database
        find_unity = {"length": "length", "meter": "length", "velocity": "velocity", "m/s": "velocity",
                      "time": "time", "hour": "time", "seconds": "time", "energy": "energy", "joule": "energy",
                      "mass": "mass", "kg": "mass", "kilogram": "mass", "force": "force", "newton": "force",
                      "work": "work", "w": "work"}

        # The search must be a list of a string
        search = str(search_id)
        # This is the search we are going to use with TinyDB
        formula_search = []
        for word in search.split(" "):
            # Add the word to the formula_search so we can later use it with TinyDB
            formula_search.append(find_unity[word.lower()])


        # Are we searching a table
        if self.using_table():
            formulas = self.database_table.search( where('variables').all(formula_search) )

            # return the formulas we got from the database
            return list(formulas)