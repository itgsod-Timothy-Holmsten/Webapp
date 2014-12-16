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
            return formula

    def get_formulas_from_variables(self, search_id):
        #Replace this with a database and dont forget to cache it later
        unitys = {}
        unitys['Length'] = {"length": "length", "meter": "length"}
        unitys['Velocity'] = {"velocity": "velocity", "m/s": "velocity"}
        unitys['Time'] = {"time": "time", "hour": "time", "seconds": "time"}
        unitys['Energy'] = {"energy": "energy", "joule": "energy"}
        unitys['Mass'] = {"mass": "mass", "kg": "mass", "kilogram": "mass"}
        unitys['Force'] = {"force": "force", "newton": "force"}
        unitys['Work'] = {"work": "work", "w": "work"}
        unitys['Acceleration'] = {"acceleration": "acceleration", "m/s^2": "acceleration", "gravity": "acceleration"}

        merged_unity_dict = {}
        for unity in unitys:
            merged_unity_dict.update(unitys[unity])

        # The search must be a list of a string
        search = str(search_id)
        # This is the search we are going to use with TinyDB
        formula_search = []
        for word in search.split(" "):
            # Add the word to the formula_search so we can later use it with TinyDB
            formula_search.append(merged_unity_dict[word.lower()])


        # Are we searching a table
        if self.using_table():
            formulas = self.database_table.search( where('unities').all(formula_search) )

            for formula in formulas:
                formula['missing_unities'] = len(formula['unities']) - len(formula_search)
                print(formula['missing_unities'])

            # return the formulas we got from the database
            return list(formulas)