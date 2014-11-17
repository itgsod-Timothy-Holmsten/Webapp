from tinydb import TinyDB, where

class Search(object):
    def __init__(self, database, table=""):
        self.database = TinyDB(str(database))
        self.database_table = self.database.table(table)

    def using_table(self):
        if len(self.database_table) > 0:
            return True

    def get_formulas_from_variables(self, search_id):
        # The search must be a list of a string
        search = [str(search_id)]
        # This is the search we are going to use with TinyDB
        formula_search = []
        for char in search:
            # Is the char a letter in the alphabet
            if char.isalpha():
                # Add the char to the formula_search so we can later use it with TinyDB
                formula_search.append(char)

        # Are we searching a table
        if self.using_table():
            formulas = self.database_table.search( where('variables').all(search_id) )
            # return the formulas we got from the database
            return list(formulas)