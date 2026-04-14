# Va bene fare una singola classe che contiene tutti i DTO?

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sale:
    # primary key
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    # Order_method_type: str ???
    # Come devo fare per rappresentare bene le relazioni? Posso salvarmi Order_method_type qui visto che la tabella
    # è nella forma codice - stringa e sono pochi valori?

    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

@dataclass
class Product:
    # primary key
    Product_number: int

    Product_line: str
    Product_type: str
    Product: str
    Product_brand: str
    Product_color: str
    Unit_cost: float
    Unit_price: float

@dataclass
class Retailer:
    # primary key
    Retailer_code: int

    Retailer_name: str
    Type: str
    Country: str

