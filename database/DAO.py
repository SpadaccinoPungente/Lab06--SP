from database.DB_connect import DBConnect
from database.DTOs import Retailer, Product, Sale


def get_all_years():
    pass

def get_all_brands():
    pass

def fill_all_retailers(id_map_retailers):
    cnx = DBConnect.get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_retailers")
        for row in cursor:
            id_map_retailers[row["Retailer_code"]] = Retailer(**row)
        cursor.close()
        cnx.close()