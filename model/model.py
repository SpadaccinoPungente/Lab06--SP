from database.DAO import DAO


class Model:

    def __init__(self):
        pass

    def get_all_years(self):
        DAO.get_all_years()