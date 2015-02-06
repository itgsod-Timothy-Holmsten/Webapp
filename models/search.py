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
        units = {}
        units['Length'] = {"length": "length", "meter": "length", "radius": "length", "cm": "length", "centimeter": "length"}
        units['Velocity'] = {"velocity": "velocity", "m/s": "velocity", "c": "velocity"}
        units['Time'] = {"time": "time", "hour": "time", "seconds": "time"}
        units['Energy'] = {"energy": "energy", "joule": "energy"}
        units['Mass'] = {"mass": "mass", "kg": "mass", "kilogram": "mass"}
        units['Force'] = {"force": "force", "newton": "force"}
        units['Work'] = {"work": "work", "w": "work"}
        units['Acceleration'] = {"acceleration": "acceleration", "m/s^2": "acceleration", "gravity": "acceleration"}
        units['Constant'] = {"constant": "constant", "pi": "constant", "c": "constant"}
        units['Area'] = {"area": "area"}

        merged_unit_dict = {}
        for unit in units:
            merged_unit_dict.update(units[unit])

        # The search must be a list of a string
        search = str(search_id)
        # This is the search we are going to use with TinyDB
        formula_search = []
        for word in search.split(", "):
            if word.isalpha():
                # Add the word to the formula_search so we can later use it with TinyDB
                formula_search.append(merged_unit_dict[word.lower()])


        # Are we searching a table
        if self.using_table():
            formulas = self.database_table.search( where('units').all(formula_search) )

            for formula in formulas:
                formula['missing_units'] = len(formula['units']) - len(formula_search)

            # return the formulas we got from the database
            return list(formulas)