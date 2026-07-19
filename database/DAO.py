from database.DB_connect import DBConnect
from database.DTOs import Retailer, Product, Sale


def fill_retailers_map(retailers_map):
    """Interroga go_retailers e popola il dizionario passato dal Model"""
    cnx = DBConnect.get_connection()
    if cnx:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_retailers")
        for row in cursor:
            # La chiave è il codice, il valore è l'oggetto
            retailers_map[row["Retailer_code"]] = Retailer(**row)
        cursor.close()
        cnx.close()


def fill_products_map(products_map):
    """Simile a fill_retailers_map, ma per go_products"""
    pass


def get_all_years():
    """Restituisce una lista di interi. Usa SELECT DISTINCT YEAR(Date)..."""
    pass


def get_all_brands():
    """Restituisce una lista di stringhe. Usa SELECT DISTINCT Product_brand..."""
    pass


def get_sales(anno, brand, retailer_code, retailers_map, products_map):
    """
    Usa COALESCE per ignorare i filtri che sono None.
    Restituisce una lista di oggetti Sale.
    """
    cnx = DBConnect.get_connection()
    result = []
    if cnx:
        cursor = cnx.cursor(dictionary=True)
        # La query usa COALESCE: se %s è nullo, confronta il campo con se stesso (sempre vero)
        query = """
                SELECT ds.*, p.Product_brand
                FROM go_daily_sales ds
                         JOIN go_products p ON ds.Product_number = p.Product_number
                WHERE YEAR (ds.Date) = COALESCE (%s \
                    , YEAR (ds.Date))
                  AND p.Product_brand = COALESCE (%s \
                    , p.Product_brand)
                  AND ds.Retailer_code = COALESCE (%s \
                    , ds.Retailer_code) \
                """
        cursor.execute(query, (anno, brand, retailer_code))

        for row in cursor:
            # Prende i riferimenti ESISTENTI dalle mappe passate dal Model
            ret = retailers_map[row["Retailer_code"]]
            prod = products_map[row["Product_number"]]

            # Crea l'oggetto Sale assemblando i pezzi
            vendita = Sale(
                Retailer=ret,
                Product=prod,
                Order_method_code=row["Order_method_code"],
                Order_method_type="Non richiesto qui",
                Date=row["Date"],
                Quantity=row["Quantity"],
                Unit_price=row["Unit_price"],
                Unit_sale_price=row["Unit_sale_price"]
            )
            result.append(vendita)

        cursor.close()
        cnx.close()
    return result