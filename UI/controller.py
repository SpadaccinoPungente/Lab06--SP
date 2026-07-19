import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

        # Variabili di stato per i filtri correnti
        self._sel_year = None
        self._sel_brand = None
        self._sel_retailer = None

    def fill_dd_year(self):
        years = self._model.get_years()
        for y in years:
            self._view.dd_year.options.append(
                ft.dropdown.Option(
                    key=str(y),
                    text=str(y),
                    on_click=self.read_year))
        self._view.update_page()

    def fill_dd_retailer(self):
        retailers = self._model.get_retailers()
        for r in retailers:
            # Come da slide: text stringa visibile, data=oggetto intero
            self._view.dd_retailer.options.append(
                ft.dropdown.Option(
                    key=str(r.Retailer_code),
                    text=r.Retailer_name,
                    data=r,
                    on_click=self.read_retailer))
        self._view.update_page()

    # --- HANDLER DEI DROPDOWN ---
    def read_year(self, e):
        val = e.control.key
        self._sel_year = int(val) if val != "None" else None

    def read_retailer(self, e):
        if e.control.key == "None":
            self._sel_retailer = None
        else:
            self._sel_retailer = e.control.data  # Estraggo l'OGGETTO Retailer salvato prima

    def read_brand(self, e):
        val = e.control.key
        self._sel_brand = str(val) if val != "None" else None

    # --- HANDLER DEI BOTTONI ---
    def handle_top_sales(self, e):
        # 1. Recupero codice retailer se esiste
        ret_code = self._sel_retailer.Retailer_code if self._sel_retailer else None

        # 2. Interrogo il model passando i filtri attuali
        vendite = self._model.get_vendite_filtrate(self._sel_year, self._sel_brand, ret_code)

        # 3. Ordino per ricavo (grazie alla property che hai messo in Sale!)
        vendite.sort(key=lambda x: x.ricavo, reverse=True)
        top_5 = vendite[:5]

        # 4. Pulisco e aggiorno la UI
        self._view.txt_result.controls.clear()
        for v in top_5:
            self._view.txt_result.controls.append(ft.Text(
                f"Data: {v.Date}; Ricavo: {v.ricavo}; Retailer: {v.Retailer.Retailer_code}; Product: {v.Product.Product_number}"
            ))
        self._view.update_page()

    def handle_analyze_sales(self, e):
        # Stessa chiamata a model usata per top_sales
        # Poi cicli su 'vendite' per calcolare somma ricavi, set di retailer, set di prodotti
        pass

# import flet as ft
#
#
# class Controller:
#
#     def __init__(self, view, model):
#         self._view = view
#         self._model = model
#
#         self.selected_retailer = None
#
#     def fill_dd_year(self):
#         """Metodo per popolare _dd_year"""
#
#         years = self._model.get_all_years()
#
#         for year in years:
#             self._view.dd_year.options.append(ft.dropdown.Option(year))
#
#         self._view.update_page()
#
#     def fill_dd_brand(self):
#         """Metodo per popolare _dd_brand"""
#
#         brands = self._model.get_all_brands()
#
#         for brand in brands:
#             self._view.dd_brand.options.append(ft.dropdown.Option(brand))
#
#         self._view.update_page()
#
#     # def fill_dd_retailer(self):
#     #     """Metodo per popolare _dd_retailer"""
#     #
#     #     retailers = self._model.get_all_retailers()
#     #
#     #     for retailer in retailers:
#     #         self._view.dd_retailer.options.append(ft.dropdown.Option(retailer))
#     #
#     #     self._view.update_page()
#
#     def fill_dd_retailer(self):
#         """Metodo per popolare _dd_retailer"""
#
#         retailers = self._model.get_all_retailers()  # Che restituisce i values della mappa
#         for r in retailers:
#             self._view.dd_retailer.options.append(
#                 ft.dropdown.Option(
#                     key=str(r.Retailer_code),
#                     text=r.Retailer_name,
#                     data=r,
#                     on_click=self.read_retailer
#                 )
#             )
#         self._view.update_page()
#
#     def read_retailer(self, e):
#         self.selected_retailer = e.control.data
#
#     def handle_top_sales(self):
#         pass
#
#     def handle_analyze_sales(self):
#         pass