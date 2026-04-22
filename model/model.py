from database import DAO


class Model:

    def __init__(self):
        self._id_map_products = {}
        self._id_map_retailers = {}
        self._id_map_sales = {}

    def get_all_years(self):
        return DAO.get_all_years()

    def get_all_brands(self):
        return DAO.get_all_brands()

    def get_all_retailers(self):
        if not self._id_map_retailers:
            DAO.fill_all_retailers(self._id_map_retailers)
        return list(self._id_map_retailers.values())