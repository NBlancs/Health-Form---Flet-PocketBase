import flet as ft
import flet as ft
from views.AppPage import AppPage

class MainPage (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.did_mount = self.did_mount

  
    def get_page(self) -> ft.View:
        self.page.controls = [
            ft.FilledButton(                
                text="Patient",
                icon=ft.icons.PERSON_ROUNDED,
                on_click=lambda _: self.root.go('/form'),
            ),
            ft.Text(value="OR", 
                    size = 12),
            ft.FilledButton(
                text="Doctor",
                icon=ft.icons.HEALTH_AND_SAFETY,
                on_click=lambda _: self.root.go('/login'),
            ),
        ]


        return self.page

    def did_mount(self):
        pass

    