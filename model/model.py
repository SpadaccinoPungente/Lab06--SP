from database import DAO


class Model:
    def __init__(self):
        # Queste sono le tue Identity Map
        self._retailers_map = {}
        self._products_map = {}

    def get_retailers(self):
        """Restituisce tutti i retailer. Se la mappa è vuota, la fa popolare dal DAO."""
        if not self._retailers_map:
            DAO.fill_retailers_map(self._retailers_map)
        return self._retailers_map.values()  # Restituisce solo la lista degli oggetti

    def get_brands(self):
        """Usa il DAO per farsi dare solo la lista dei brand unici"""
        return DAO.get_all_brands()

    def get_years(self):
        """Usa il DAO per farsi dare solo la lista degli anni unici"""
        return DAO.get_all_years()

    def get_vendite_filtrate(self, anno, brand, retailer_code):
        """
        Chiama il DAO passando i filtri e le mappe.
        Le mappe servono al DAO per 'agganciare' i riferimenti agli oggetti
        già esistenti in memoria invece di ricrearli da zero!
        """
        # Assicurati che le mappe siano popolate prima di usarle
        if not self._retailers_map: self.get_retailers()
        if not self._products_map: DAO.fill_products_map(self._products_map)

        return DAO.get_sales(anno, brand, retailer_code, self._retailers_map, self._products_map)

# from database import DAO
#
#
# class Model:
#
#     def __init__(self):
#         self._id_map_products = {}
#         self._id_map_retailers = {}
#         self._id_map_sales = {}
#
#     def get_all_years(self):
#         return DAO.get_all_years()
#
#     def get_all_brands(self):
#         return DAO.get_all_brands()
#
#     def get_all_retailers(self):
#         return DAO.fill_all_retailers(self._id_map_retailers)