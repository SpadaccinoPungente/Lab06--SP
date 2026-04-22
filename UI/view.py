import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):

        super().__init__()

        self._page = page
        self._page.title = "Lab 06 - TDP 2026"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK

        # Controller -> non inizializzato, viene fatto nel main dopo la creazione.
        self._controller = None

        # Definizione degli elementi grafici.

        # Titolo.
        self._title = None
        # ROW 1.
        self.dd_year = None
        self.dd_brand = None
        self.dd_retailer = None
        # ROW 2.
        self.btn_top_sales = None
        self.btn_analyze_sales = None
        self.txt_result = None

    def load_interface(self):

        # Titolo.
        self._title = ft.Text("Analisi Database go_sales", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1: dropdown per anno, brand, retailer.
        self.dd_year = ft.Dropdown(
            label="Anno",
            hint_text="Selezionare un anno",
            width=300,
            options=[ft.dropdown.Option(key="None", text="Nessun filtro")]
        )
        self._controller.fill_dd_year()

        self.dd_brand = ft.Dropdown(
            label="Brand",
            hint_text="Selezionare un brand",
            width=300,
            options=[ft.dropdown.Option(key="None", text="Nessun filtro")]
        )
        self._controller.fill_dd_brand()

        self.dd_retailer = ft.Dropdown(
            label="Retailer",
            hint_text="Selezionare un retailer",
            width=300,
            options=[ft.dropdown.Option(key="None", text="Nessun filtro")]
        )
        self._controller.fill_dd_retailer()

        # Creazione row1.
        row1 = ft.Row(
            controls=[self.dd_year, self.dd_brand, self.dd_retailer],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # ROW 2: bottone per top sales, analyze sales.
        self.btn_top_sales = ft.ElevatedButton(
            text="Top vendite",
            on_click=self._controller.handle_top_sales,
            width=200
        )
        self.btn_analyze_sales = ft.ElevatedButton(
            text="Analizza vendite",
            on_click=self._controller.handle_analyze_sales,
            width=200
        )

        # Creazione row2.
        row2 = ft.Row(
            controls=[self.btn_top_sales, self.btn_analyze_sales],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Allineamento -> column invece di self.lv_out = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.txt_result = ft.Column(
            expand=True,
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )

        self._page.controls.extend([row1, row2, self.txt_result])
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
