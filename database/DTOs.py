from dataclasses import dataclass
from datetime import datetime

# Prima le classi base che non dipendono da altre.
@dataclass(frozen=True)
class Product:
    # Primary key
    Product_number: int

    Product_line: str
    Product_type: str
    Product: str
    Product_brand: str
    Product_color: str
    Unit_cost: float
    Unit_price: float

    def __str__(self):
        return f"{self.Product_number} - {self.Product_brand} ({self.Product})"

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Product_number)


@dataclass(frozen=True)
class Retailer:
    # Primary key
    Retailer_code: int

    Retailer_name: str
    Type: str
    Country: str

    def __str__(self):
        return f"{self.Retailer_code} - {self.Retailer_name}"

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code

    def __hash__(self):
        return hash(self.Retailer_code)


# Classe Sale che comprende le altre due.
@dataclass(frozen=True)
class Sale:
    # Oggetti interi invece del solo ID.
    Retailer: Retailer
    Product: Product

    # Mantengo entrambi i valori di Order_method (richiede una JOIN tra go_methods e go_daily_sales).
    Order_method_code: int
    Order_method_type: str

    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    # Property per calcolare il ricavo.
    @property
    def ricavo(self):
        return self.Unit_sale_price * self.Quantity

    def __str__(self):
        return f"Vendita del {self.Date} | Prodotto: {self.Product.Product_number} | Retailer: {self.Retailer.Retailer_code}"

    def __eq__(self, other):
        return (self.Retailer == other.Retailer
                and self.Product == other.Product
                and self.Order_method_code == other.Order_method_code)

    def __hash__(self):
        # Passare una tupla invece di una somma evita collisioni.
        return hash((self.Retailer.Retailer_code, self.Product.Product_number, self.Order_method_code))


