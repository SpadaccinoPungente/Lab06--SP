import flet as ft


class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

        self.selected_retailer = None

    def fill_dd_year(self):
        """Metodo per popolare _dd_year"""

        years = self._model.get_all_years()

        for year in years:
            self._view.dd_year.options.append(ft.dropdown.Option(year))

        self._view.update_page()

    def fill_dd_brand(self):
        """Metodo per popolare _dd_brand"""

        brands = self._model.get_all_brands()

        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))

        self._view.update_page()

    # def fill_dd_retailer(self):
    #     """Metodo per popolare _dd_retailer"""
    #
    #     retailers = self._model.get_all_retailers()
    #
    #     for retailer in retailers:
    #         self._view.dd_retailer.options.append(ft.dropdown.Option(retailer))
    #
    #     self._view.update_page()

    def fill_dd_retailer(self):
        """Metodo per popolare _dd_retailer"""

        retailers = self._model.get_all_retailers()  # Che restituisce i values della mappa
        for r in retailers:
            self._view.dd_retailer.options.append(
                ft.dropdown.Option(
                    key=str(r.Retailer_code),
                    text=r.Retailer_name,
                    data=r,
                    on_click=self.read_retailer
                )
            )
        self._view.update_page()

    def read_retailer(self, e):
        self.selected_retailer = e.control.data

    def handle_top_sales(self):
        pass

    def handle_analyze_sales(self):
        pass