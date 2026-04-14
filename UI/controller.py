import flet as ft


class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

    def fill_dd_year(self):
        """Metodo per popolare _dd_year"""

        years = self._model.get_all_years()
        # va bene farlo così o mi conviene salvare gli oggetti come sales e riempire le opzioni con solo gli anni?

        for year in years:
            self._view.dd_year.options.append(ft.dropdown.Option(year))

        self._view.update_page()

    def fill_dd_brand(self):
        pass

    def fill_dd_retailer(self):
        pass

    def handle_top_sales(self):
        pass

    def handle_analyze_sales(self):
        pass