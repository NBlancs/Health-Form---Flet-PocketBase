import flet as ft
import flet as ft
from views.AppPage import AppPage

class ThankYou (AppPage):

    # Required
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
    def get_page(self) -> ft.View:
        self.page.controls = [
            ft.Text(value= "THANK YOU FOR SUBMITTING", size= 64),
            ft.FilledButton(text="Menu",on_click=lambda _: self.root.go('/'))
        ]

        return self.page

    def did_mount(self):
        pass